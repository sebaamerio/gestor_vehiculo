from sqlalchemy.orm import Session
from sqlalchemy.sql import literal
from sqlalchemy import func, asc, desc, select, literal, and_, cast, String
from typing import Optional
from datetime import date, timedelta
from ..models.vehiculo_model import Vehiculo
from ..models.vehiculo_dependencia_model import VehiculoDependencia
from ..models.tipo_condicion_model import TipoCondicion
from ..models.tipo_tramite_dependencia_model import TipoTramiteDependencia
from ..models.dependencia_model import Dependencia
from ..models.tipo_modelo_model import TipoModelo
from ..models.tipo_situacion_model import TipoSituacion
from ..models.tipo_marca_model import TipoMarca
from ..models.tipo_modelo_model import TipoModelo
from ..schemas.vehiculo_schema import VehiculoCreate, VehiculoUpdate
from ..models.vehiculo_dependencia_model import VehiculoDependencia
from ..models.dependencia_model import Dependencia

def get_all(db: Session):
    return db.query(Vehiculo).all()

def build_vehiculos_query(
    db: Session,
    filter_field: str | None = None,
    filter_value: str | None = None,
    sort_field: str | None = None,
    sort_order: str | None = None,
    registro_marca: bool | None = None,
    dependencia_id: int | None = None,
    situacion_id: int | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
):
    query = db.query(Vehiculo)

    # =====================
    # 🔵 FILTROS AVANZADOS
    # =====================
    if registro_marca is not None:
        query = query.filter(Vehiculo.registro_marca == registro_marca)

    if dependencia_id:
        query = query.filter(
            Vehiculo.vehiculo_dependencias.any(
                and_(
                    VehiculoDependencia.activo.is_(True),
                    VehiculoDependencia.dependencia_id == dependencia_id
                )
            )
        )

    if situacion_id:
        query = query.filter(Vehiculo.situacion_id == situacion_id)

    if fecha_desde and fecha_hasta:
        query = query.filter(
            Vehiculo.fecha_titulo.between(fecha_desde, fecha_hasta)
        )
    elif fecha_desde:
        query = query.filter(Vehiculo.fecha_titulo >= fecha_desde)
    elif fecha_hasta:
        query = query.filter(Vehiculo.fecha_titulo <= fecha_hasta)

    # =====================
    # 🔎 FILTRO
    # =====================
    if filter_field and filter_value:       
        # 🔹 1) CAMPOS RELACIONADOS     
        if filter_field == "marca_descripcion":
            query = query.filter(
                Vehiculo.tipo_marca.has(
                    TipoMarca.descripcion.ilike(f"{filter_value}%")
                )
            )
        elif filter_field == "modelo_descripcion":
            query = query.filter(
                Vehiculo.tipo_modelo.has(
                    TipoModelo.descripcion.ilike(f"{filter_value}%")
                )
            )
        # 🔹 2) CAMPOS DIRECTOS (fallback)
        else:
            column = getattr(Vehiculo, filter_field, None)
            if column is not None:                
                query = query.filter(cast(column, String).ilike(f"{filter_value}%"))

    # -----------------------------------
    # ↕️ ORDENAMIENTO
    # -----------------------------------
    if sort_field and sort_order in ("asc", "desc"):
        column = getattr(Vehiculo, sort_field, None)
        if column is not None:
            query = query.order_by(
                asc(column) if sort_order == "asc" else desc(column)
            )

    return query.distinct()

def get_paginated_vehiculos(
    db: Session,
    page: int,
    page_size: int,
    filter_field: str | None = None,
    filter_value: str | None = None,
    sort_field: str | None = None,
    sort_order: str | None = None,
    registro_marca: bool | None = None,
    dependencia_id: int | None = None,
    situacion_id: int | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
):
    query = build_vehiculos_query(
        db,
        filter_field,
        filter_value,
        sort_field,
        sort_order,
        registro_marca,
        dependencia_id,
        situacion_id,
        fecha_desde,
        fecha_hasta
    )
    
    # TOTAL filtrado
    total = query.count()

    data = (
        query
        .offset(page * page_size)
        .limit(page_size)
        .all()
    )

    return {
        "total": total,
        "data": data,
    }

def get_paginated_vehiculos_report(
    db: Session,  
    filter_field: str | None = None,
    filter_value: str | None = None,
    sort_field: str | None = None,
    sort_order: str | None = None,
    registro_marca: bool | None = None,
    dependencia_id: int | None = None,
    situacion_id: int | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
):
    query = build_vehiculos_query(
        db,
        filter_field,
        filter_value,
        sort_field,
        sort_order,
        registro_marca,
        dependencia_id,
        situacion_id,
        fecha_desde,
        fecha_hasta
    )

    return query.all()

def get_by_id(db: Session, id: int):
    return db.query(Vehiculo).filter(Vehiculo.id == id).first()

def get_by_registroNro(db: Session, registro_nro: int ):
    """Busca por ro (case insensitive)."""
    return db.query(Vehiculo).filter(
        Vehiculo.registro_nro == registro_nro).first()

def get_by_NroChasis(db: Session, nroChasis: str, exclude_id: int = None):
    query = db.query(Vehiculo).filter(
        Vehiculo.chasis_nro == nroChasis
    )
    if exclude_id is not None:
        query = query.filter(Vehiculo.id != exclude_id)
    return query.first()

def get_by_NroMotor(db: Session, nroMotor: String, exclude_id: int = None ): 
    query = db.query(Vehiculo).filter(
        Vehiculo.motor_nro == nroMotor)   
    if exclude_id is not None:
        query = query.filter(Vehiculo.id != exclude_id)
    return query.first()

def get_by_Dominio(db: Session, dominio: str, exclude_id: int = None):
    query = db.query(Vehiculo).filter(
        Vehiculo.dominio.ilike(dominio)
    )
    if exclude_id is not None:
        query = query.filter(Vehiculo.id != exclude_id)
    return query.first()


def create(db: Session, vehiculo: VehiculoCreate,dependencia: Optional[Dependencia] = None):

    fecha_hoy = date.today()
    fecha_ayer = fecha_hoy - timedelta(days=1)

    try:

        # 1. Crear vehículo (SIN dependencia_id ni registro_nro — se asigna post-flush)
        data = vehiculo.model_dump(
            exclude={"dependencia_id", "registro_nro"},
            exclude_none=True,
        )

        db_vehiculo = Vehiculo(**data)
        db.add(db_vehiculo)
        db.flush()  # obtiene el id generado por la DB
        db_vehiculo.registro_nro = vehiculo.registro_nro if vehiculo.registro_nro is not None else db_vehiculo.id

        # 2. Desactivar dependencias activas anteriores (si existieran)
        dependencias_activas = (
            db.query(VehiculoDependencia)
            .filter(
                VehiculoDependencia.vehiculo_id == db_vehiculo.id,
                VehiculoDependencia.activo == True
            )
            .all()
        )

        for dep in dependencias_activas:
            dep.activo = False
            dep.fecha_hasta2 = fecha_ayer

        # 3- Crear dependencia SOLO si existe
        if dependencia is not None:
            db_dependencia = VehiculoDependencia(
                vehiculo_id = db_vehiculo.id,
                dependencia_id = dependencia.id,
                dependencia_descripcion = dependencia.descripcion,
                tipo_tramite_id = 1, # 1- Alta
                fecha_desde = fecha_hoy,
                activo=True
            )
            db.add(db_dependencia)

        db.commit()        
        db.refresh(db_vehiculo)

        return db_vehiculo
    
    except Exception:
        db.rollback()      
        raise

#def update(db: Session, id: int, vehiculo: VehiculoUpdate):
#    db_vehiculo = get_by_id(db, id)
#    if not db_vehiculo:
#       return None
#    for field, value in vehiculo.model_dump(exclude_unset=True).items():
#        setattr(db_vehiculo, field, value)
#    db.commit()
#    db.refresh(db_vehiculo)
#    return db_vehiculo

def update(db: Session, id: int, vehiculo: VehiculoUpdate):
    db_vehiculo = get_by_id(db, id)

    if not db_vehiculo:
        return None

    update_data = vehiculo.model_dump(exclude_unset=True)

    # =====================================
    # 1. MANEJO DE DEPENDENCIA
    # =====================================
    nueva_dependencia_id = update_data.get("dependencia_id")

    if nueva_dependencia_id:

        dependencia = db.query(Dependencia).filter(
            Dependencia.id == nueva_dependencia_id
        ).first()

        if not dependencia:
            raise ValueError("Dependencia no encontrada")

        # buscar activa
        dependencia_activa = db.query(VehiculoDependencia).filter(
            VehiculoDependencia.vehiculo_id == id,
            VehiculoDependencia.activo == True
        ).first()

        if dependencia_activa:
            # ✔ solo si cambió
            if dependencia_activa.dependencia_id != nueva_dependencia_id:
                dependencia_activa.dependencia_id = nueva_dependencia_id
                dependencia_activa.dependencia_descripcion = dependencia.descripcion
        else:
            # ✔ no tenía → crear nueva
            nueva = VehiculoDependencia(
                vehiculo_id=id,
                dependencia_id=nueva_dependencia_id,
                dependencia_descripcion=dependencia.descripcion,
                fecha_desde=date.today(),
                fecha_hasta=None,
                activo=True,
                tipo_tramite_id = 1  # Alta
            )
            db.add(nueva)

    # =====================================
    # 2. ACTUALIZAR RESTO DE CAMPOS
    # =====================================
    for field, value in update_data.items():
        if field != "dependencia_id":  # 🔥 evitar pisar lógica
            setattr(db_vehiculo, field, value)

    # =====================================
    # 3. GUARDAR
    # =====================================
    db.commit()
    db.refresh(db_vehiculo)

    return db_vehiculo


def delete(db: Session, id: int):
    db_vehiculo = get_by_id(db, id)
    if db_vehiculo:
        db.delete(db_vehiculo)
        db.commit()
    return db_vehiculo

# Consultas
def get_by_dependencia(db: Session):
    results = (
        db.query(
            func.coalesce(
                VehiculoDependencia.dependencia_descripcion,
                literal("SIN DEPENDENCIA")
            ).label("descripcion"),
            func.count(Vehiculo.id).label("value"),
        )
        .outerjoin(
            VehiculoDependencia,
            (Vehiculo.id == VehiculoDependencia.vehiculo_id)
            & (VehiculoDependencia.activo == True)
        )
        .group_by(VehiculoDependencia.dependencia_descripcion)
        .all()
    )
    return [{"descripcion": descripcion, "value": value} for descripcion, value in results]

def get_by_anio(db: Session):
    """
    Devuelve la cantidad de vehículos agrupados por año de fabricación.
    Ejemplo de salida: [{ "descripcion": 2015, "value": 12 }, ...]
    """
    results  = (
        db.query(
            Vehiculo.anio.label("descripcion"),
            func.count(Vehiculo.id).label("value")
        )
        .outerjoin(
            VehiculoDependencia,
            (Vehiculo.id == VehiculoDependencia.vehiculo_id)
            & (VehiculoDependencia.activo == True)
        )
        .group_by(Vehiculo.anio)
        .order_by(Vehiculo.anio.asc())
        .all()
    )    
    return [{"descripcion": str(anio), "value": cantidad} for anio, cantidad in results]

def get_by_condicion(db: Session):
    """
    Devuelve la cantidad de vehículos agrupados por condicion.
    Ejemplo de salida: [{ "descripcion": "BUENO", "value": 12 }, ...]
    """
    results = (
        db.query(
            TipoCondicion.descripcion.label("descripcion"),
            func.count(Vehiculo.id).label("value")
        )
        .join(TipoCondicion, Vehiculo.condicion_id == TipoCondicion.id)
        .group_by(TipoCondicion.descripcion)
        .all()
    )
    return [{"descripcion": descripcion, "value": value} for descripcion, value in results]

def get_by_situacion(db: Session):
    results = (
        db.query(
            TipoSituacion.descripcion.label("descripcion"),
            func.count(Vehiculo.id).label("value")
        )
        .join(TipoSituacion, Vehiculo.situacion_id == TipoSituacion.id)
        .group_by(TipoSituacion.descripcion)
        .all()
    )
    return [{"descripcion": descripcion, "value": value} for descripcion, value in results]

def get_Vehiculos_dependencia_activos(db: Session):
    """
    Devuelve los vehiculos activos con su dependencia actual.
    """
    return (
        db.query(           
            Vehiculo.registro_nro.label("registro_nro"),
            Vehiculo.dominio.label("dominio"),
            TipoModelo.descripcion.label("modelo_descripcion"),
            Vehiculo.anio.label("anio"),
            TipoSituacion.descripcion.label("situacion_descripcion"),
            VehiculoDependencia.dependencia_id.label("dependencia_id"),
            func.coalesce(
                VehiculoDependencia.dependencia_descripcion,
                literal("SIN DEPENDENCIA")
            ).label("dependencia_descripcion")
        )
        .outerjoin(
            VehiculoDependencia,
            (Vehiculo.id == VehiculoDependencia.vehiculo_id)
            & (VehiculoDependencia.activo == True)
        )
        .outerjoin(
            TipoModelo,
            (Vehiculo.modelo_id == TipoModelo.id)           
        )
        .outerjoin(
            TipoSituacion,
            (Vehiculo.situacion_id == TipoSituacion.id)           
        )
        .order_by(
            VehiculoDependencia.activo.asc(),
            VehiculoDependencia.fecha_desde.asc()
        )
        .yield_per(1000)
    )

def get_historial_dependencias(vehiculo_id: int, db: Session):
    """
    Devuelve el historial completo de dependencias de un vehículo.
    """

    # -------------------------
    # SELECT 1: dependencia actual
    # -------------------------
    q1 = (
        select(
            func.concat( Vehiculo.id, "-", literal("DEP"), "-", VehiculoDependencia.id , "-", VehiculoDependencia.fecha_desde).label("id"),         
            Vehiculo.registro_nro.label("registro_nro"),
            Vehiculo.dominio.label("dominio"),
            VehiculoDependencia.activo.label("activo"),
            VehiculoDependencia.fecha_desde.label("fecha_desde"),
            VehiculoDependencia.fecha_hasta.label("fecha_hasta"),
            VehiculoDependencia.dependencia_descripcion.label("dependencia"),
            TipoTramiteDependencia.descripcion.label("tipo_tramite")
        )
        .select_from(Vehiculo)
        .join(
            VehiculoDependencia,
            Vehiculo.id == VehiculoDependencia.vehiculo_id
        )
        .join(
            TipoTramiteDependencia,
            TipoTramiteDependencia.id == VehiculoDependencia.tipo_tramite_id
        )
        .where(Vehiculo.id == vehiculo_id)
        .order_by(
            VehiculoDependencia.activo.desc(),
            VehiculoDependencia.fecha_desde.desc()
        )
    )   

    result = db.execute(q1).mappings().all()

    return result