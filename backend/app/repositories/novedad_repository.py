from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, timedelta
from ..models.novedad_model import Novedad as NovedadModel
from ..models.tipo_novedad_model import TipoNovedad as TipoNovedadModel
from ..models.baja_model import Baja as BajaModel
from ..models.cambio_motor_model import CambioMotor as CambioMotorModel
from ..models.accidente_model import Accidente as AccidenteModel
from ..models.donacion_model import Donacion as DonacionModel
from ..models.robo_model import Robo as RoboModel
from ..models.transferencia_model import Transferencia as TransferenciaModel
from ..models.vehiculo_model import Vehiculo as VehiculoModel
from ..models.tipo_situacion_model import TipoSituacion as TipoSituacionModel
from ..models.dependencia_model import Dependencia as DependenciaModel
from ..models.cambio_chasis_model import CambioChasis as CambioChasisModel
from ..models.comodato_model import Comodato as ComodatoModel
from ..models.vehiculo_dependencia_model import VehiculoDependencia as VehiculoDependenciaModel
from ..models.infraccion_model import Infraccion as InfraccionModel

from ..schemas.novedad_schema import NovedadCreate, NovedadUpdate

# =====================================================
# 🔥 MAPA CENTRALIZADO DE TIPOS → MODELO ORM
# =====================================================

DETALLE_MODEL_MAP = {
    "baja": BajaModel,
    "cambio_motor": CambioMotorModel,
    "accidente": AccidenteModel,
    "donacion": DonacionModel,
    "transf_municipalidad": DonacionModel,
    "robo": RoboModel,
    "transferencia": TransferenciaModel,
    "cambio_chasis": CambioChasisModel,
    "comodato": ComodatoModel,
    "infraccion": InfraccionModel
}

from datetime import date, timedelta

# Alta de dependencia del vehiculo
def alta_transferencia(
    db: Session,
    vehiculo_id: int,
    nueva_dependencia_id: int
):
    hoy = date.today()
    ayer = hoy - timedelta(days=1)

    # 1. Buscar dependencia nueva (para snapshot)
    dependencia = db.query(DependenciaModel).filter(
        DependenciaModel.id == nueva_dependencia_id
    ).first()

    if not dependencia:
        raise ValueError("Dependencia no encontrada")

    # 2. Buscar dependencia activa actual
    dependencia_actual = db.query(VehiculoDependenciaModel).filter(
        VehiculoDependenciaModel.vehiculo_id == vehiculo_id,
        VehiculoDependenciaModel.activo == True
    ).first()

    # 3. Cerrar la actual
    if dependencia_actual:
        dependencia_actual.activo = False
        dependencia_actual.fecha_hasta = ayer

    # 4. Crear nueva (snapshot completo)
    nueva = VehiculoDependenciaModel(
        vehiculo_id=vehiculo_id,
        dependencia_id=nueva_dependencia_id,
        dependencia_descripcion=dependencia.descripcion,  # 📸 snapshot
        fecha_desde=hoy,
        fecha_hasta=None,
        activo=True,
        tipo_tramite_id=2  # 🔥 transferencia
    )

    db.add(nueva)

# Revertir el alta de dependencia del vehiculo
def revertir_transferencia(db: Session, vehiculo_id: int):
    # 1. Obtener la activa (la nueva creada por transferencia)
    actual = db.query(VehiculoDependenciaModel).filter(
        VehiculoDependenciaModel.vehiculo_id == vehiculo_id,
        VehiculoDependenciaModel.activo == True
    ).first()

    if actual:
        db.delete(actual)

    # 2. Buscar la anterior (la última inactiva)
    anterior = db.query(VehiculoDependenciaModel).filter(
        VehiculoDependenciaModel.vehiculo_id == vehiculo_id,
        VehiculoDependenciaModel.activo == False
    ).order_by(VehiculoDependenciaModel.fecha_hasta.desc()).first()

    if anterior:
        anterior.activo = True
        anterior.fecha_hasta = None


# Cambia la situacion (Baja o Activo) del vehiculo
def cambio_situacion_vehiculo(
    db: Session,
    vehiculo_id: int,
    descripcion_situacion: str
):
    """
    Cambia la situación del vehículo (ACTIVO, BAJA, FUERA DE USO)
    """
    vehiculo = db.query(VehiculoModel).filter(
        VehiculoModel.id == vehiculo_id
    ).first()

    if not vehiculo:
        return None

    tipo_situacion = db.query(TipoSituacionModel).filter(
        TipoSituacionModel.descripcion == descripcion_situacion
    ).first()

    if not tipo_situacion:
        return None

    vehiculo.tipo_situacion = tipo_situacion
    return vehiculo

def create(db: Session, novedad: NovedadCreate, detalle: dict):

    # =====================================
    # 1) Crear novedad principal
    # =====================================
    db_novedad = NovedadModel(**novedad.model_dump())
    db.add(db_novedad)
    db.flush()   # Obtener ID de la novedad
    db.refresh(db_novedad)

    # =====================================
    # 2) Validar tipo de detalle
    # =====================================
    detalle_tipo = detalle["tipo"]
    detalle_data = detalle["data"]
    
    ModeloDetalleORM = DETALLE_MODEL_MAP.get(detalle_tipo)

    if ModeloDetalleORM is None:
        raise ValueError(f"Tipo de detalle inválido: {detalle_tipo}")

    # =====================================
    # 3) Preparar datos del detalle
    # =====================================
    data_dict = detalle_data.model_dump(exclude_unset=True)
    data_dict["novedad_id"] = db_novedad.id

    # =====================================
    # 4) Crear detalle ORM dinámicamente
    # =====================================
    db_detalle_orm = ModeloDetalleORM(**data_dict)
    db.add(db_detalle_orm)

    # =====================================
    # 5) ACTUALIZAR VEHÍCULO: en caso que lo requiera la novedad
    # =====================================
    if detalle_tipo == "baja":
        cambio_situacion_vehiculo(
            db,
            db_novedad.vehiculo_id,
            "BAJA"
        )

    if detalle_tipo == "robo":
        # SOLO marcar como robado si NO está recuperado
        fecha_recupero = data_dict.get("fecha_recupero")

        if not fecha_recupero:
            cambio_situacion_vehiculo(
                db,
                db_novedad.vehiculo_id,
                "BAJA"
            )

    if detalle_tipo == "transf_municipalidad":
        cambio_situacion_vehiculo(
            db,
            db_novedad.vehiculo_id,
            "BAJA"
        )

    if detalle_tipo == "cambio_motor":
        nuevo_motor = data_dict.get("motor_nro_nuevo")
        if nuevo_motor:
            vehiculo = db.query(VehiculoModel).filter(VehiculoModel.id == db_novedad.vehiculo_id).first()
            if vehiculo:
                vehiculo.motor_nro = nuevo_motor

    if detalle_tipo == "cambio_chasis":
        chasis_nuevo = data_dict.get("chasis_nuevo")
        if chasis_nuevo:
            vehiculo = db.query(VehiculoModel).filter(VehiculoModel.id == db_novedad.vehiculo_id).first()
            if vehiculo:
                vehiculo.chasis_nro = chasis_nuevo

    if detalle_tipo == "transferencia":
        dependencia_id = data_dict.get("dependencia_id")     

        if dependencia_id:
            alta_transferencia(
                db,
                db_novedad.vehiculo_id,
                dependencia_id
            )

    # =====================================
    # 6) Guardar todo
    # =====================================
    db.commit()
    db.refresh(db_novedad)

    return db_novedad, db_detalle_orm

def update(db: Session, id: int, novedad: NovedadUpdate):
    db_novedad = get_by_id(db, id)
    if not db_novedad:
        return None
    for field, value in novedad.model_dump(exclude_unset=True).items():
        setattr(db_novedad, field, value)
    db.commit()
    db.refresh(db_novedad)
    return db_novedad

def delete(db: Session, novedad_id: int) -> bool:
    """
    1- Elimina la Novedad y, por cascada ORM (configurada en el modelo), 
    su detalle asociado (Baja o CambioMotor) si existe.
    2- Deshacer los cambios en el modelo Vehiculo
    """
    # Busco la novedad
    db_novedad = db.query(NovedadModel).filter(NovedadModel.id == novedad_id).first()
  
    if not db_novedad:
        return False
    
    # Busco el vehiculo relacinado a la novedad 
    vehiculo = db.query(VehiculoModel).filter(
        VehiculoModel.id == db_novedad.vehiculo_id
    ).first()

    # =====================================
    # 🔎 1. OBTENER TIPO DE NOVEDAD
    # =====================================
    tipo_novedad = db.query(TipoNovedadModel).filter(
        TipoNovedadModel.id == db_novedad.tipo_novedad_id
    ).first()

    if not tipo_novedad:
        return False

    tipo = tipo_novedad.descripcion 
    print('tipo ', tipo)

    # =====================================
    # ACCION SEGÚN NOVEDAD
    # =====================================
    if tipo == "BAJA":
        baja = db.query(BajaModel).filter(
            BajaModel.novedad_id == novedad_id
        ).first()

        if baja:
            cambio_situacion_vehiculo(
                db,
                vehiculo.id,
                "ACTIVO"
            )

    elif tipo == "ROBO":
        robo = db.query(RoboModel).filter(
            RoboModel.novedad_id == novedad_id
        ).first()

        if robo:
            cambio_situacion_vehiculo(
                db,
                vehiculo.id,
                "ACTIVO"
        )
            
    elif tipo == "TRANSF. A MUNICIPALIDAD":
        transf_muni = db.query(DonacionModel).filter(
            DonacionModel.novedad_id == novedad_id
        ).first()

        if transf_muni:
            cambio_situacion_vehiculo(
                db,
                vehiculo.id,
                "ACTIVO"
        )

    elif tipo == "CAMBIO DE MOTOR":
        cambio_motor = db.query(CambioMotorModel).filter(
            CambioMotorModel.novedad_id == novedad_id
        ).first()
        if cambio_motor and vehiculo:
            vehiculo.motor_nro = cambio_motor.motor_nro_anterior

    elif tipo == "CAMBIO DE CHASIS":
        cambio_chasis = db.query(CambioChasisModel).filter(
            CambioChasisModel.novedad_id == novedad_id
        ).first()
        if cambio_chasis and vehiculo:
            vehiculo.chasis_nro = cambio_chasis.chasis_anterior

    elif tipo == "TRANSFERENCIA":
        revertir_transferencia(db, vehiculo.id)

    # =====================================
    # 🗑️ 3. ELIMINAR
    # =====================================
    db.delete(db_novedad)
    db.commit()
    return True

def get_all(db: Session):
    return db.query(NovedadModel).all()

def get_by_id(db: Session, id: int):
    return db.query(NovedadModel).filter(NovedadModel.id == id).first()

def get_by_vehiculoId(db: Session, vehiculo_id: int):
    return (
        db.query(NovedadModel)
        .filter(NovedadModel.vehiculo_id == vehiculo_id)
        .order_by(NovedadModel.id.desc())
        .all() )

def get_by_tipo(db: Session):
    results = (
        db.query(
            TipoNovedadModel.descripcion.label("descripcion"),
            func.count(NovedadModel.id).label("value"),
        )
        .join(TipoNovedadModel, NovedadModel.tipo_novedad_id == TipoNovedadModel.id)
        .group_by(TipoNovedadModel.descripcion)
        .order_by(func.count(NovedadModel.id).desc())
        .all()
    )
    return [{"descripcion": descripcion, "value": value} for descripcion, value in results]