from sqlalchemy.orm import Session
from sqlalchemy import and_, asc, desc, cast, String, func
from ..models.vtv_model import Vtv
from ..models.vehiculo_model import Vehiculo as VehiculoModel
from ..models.vehiculo_dependencia_model import VehiculoDependencia
from datetime import date, timedelta

from ..schemas.vtv_schema import VtvCreate, VtvUpdate

def get_all(db: Session):
    return db.query(Vtv).all()

def build_vtv_query(
    db: Session,
    filter_field: str | None = None,
    filter_value: str | None = None,
    sort_field: str | None = None,
    sort_order: str | None = None,
    registro_marca: bool | None = None,
    dependencia_id: str | None = None,                
    tipo_vtvResultado_id: int | None = None,
    zona: int | None = None,
    estado: str | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
):
    # 🔗 JOIN de Vtv con Vehiculo siempre (así podés filtrar/ordenar)
    query = db.query(Vtv).join(Vtv.vehiculo)

    # =====================
    # 🔵 FILTROS AVANZADOS
    # =====================
    if registro_marca is not None:
        query = query.filter(VehiculoModel.registro_marca == registro_marca)

    if dependencia_id:
        query = query.filter(
            VehiculoModel.vehiculo_dependencias.any(
                and_(
                    VehiculoDependencia.activo.is_(True),
                    VehiculoDependencia.dependencia_id == dependencia_id
                )
            )
        )
    if tipo_vtvResultado_id:
        query = query.filter(
            Vtv.tipo_vtvResultado_id == tipo_vtvResultado_id
        )
    if zona:
        query = query.filter(
            Vtv.zona == zona
        )

    
    # ===================================
    # FILTRO POR ESTADO Y RANGO DE FECHAS
    # ===================================
    ESTADOS_VALIDOS = {"Solicitadas","Realizadas","Pendientes","Vencimiento"}

    if estado in ESTADOS_VALIDOS:

        if estado == "Pendientes":
            query = query.filter(Vtv.fecha_realizada.is_(None))

        else:
            campo_fecha = {
                "Solicitadas": Vtv.fecha_solicitud,
                "Realizadas": Vtv.fecha_realizada,
                "Vencimiento": Vtv.fecha_vto,
            }.get(estado)

            if fecha_desde and fecha_hasta:
                query = query.filter(campo_fecha.between(fecha_desde, fecha_hasta))
            elif fecha_desde:
                query = query.filter(campo_fecha >= fecha_desde)
            elif fecha_hasta:
                query = query.filter(campo_fecha <= fecha_hasta)

    # =====================
    # 🔎 FILTRO
    # =====================
    if filter_field and filter_value:
        # 🔹 1) CAMPOS RELACIONADOS
        if filter_field == "dominio":
            query = query.filter(
                Vtv.vehiculo.has(
                    VehiculoModel.dominio.ilike(f"{filter_value}%")
                )
            )
        # 🔹 2) CAMPOS DIRECTOS (fallback)
        else:
            column = getattr(Vtv, filter_field, None)
            if column is not None:
                query = query.filter(cast(column, String).ilike(f"{filter_value}%"))

    # -----------------------------------
    # ↕️ ORDENAMIENTO
    # -----------------------------------
    if sort_field:
        column = getattr(Vtv, sort_field, None)

        if column is not None:
            if sort_order == "asc":
                query = query.order_by(asc(column))
            else:
                # default cuando viene sort_field pero no order
                query = query.order_by(desc(column))
        else:
            # campo inválido → fallback
            query = query.order_by(desc(Vtv.id))
    else:
        # 👈 DEFAULT GLOBAL
        query = query.order_by(asc(Vtv.id))

    return query.distinct()


def get_paginated(
    db: Session,
    page: int,
    page_size: int,
    filter_field: str | None = None,
    filter_value: str | None = None,
    sort_field: str | None = None,
    sort_order: str | None = None,
    registro_marca: bool | None = None,
    dependencia_id: str | None = None,                
    tipo_vtvResultado_id: int | None = None,
    zona: int | None = None,
    estado: str | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
):
    query = build_vtv_query(
        db,
        filter_field,
        filter_value,
        sort_field,
        sort_order,
        registro_marca,
        dependencia_id,
        tipo_vtvResultado_id,
        zona,
        estado,
        fecha_desde,
        fecha_hasta)
    
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

def get_paginated_vtv_report(
    db: Session,  
    filter_field: str | None = None,
    filter_value: str | None = None,
    sort_field: str | None = None,
    sort_order: str | None = None,
    registro_marca: bool | None = None,
    dependencia_id: str | None = None,                
    tipo_vtvResultado_id: int | None = None,
    zona: int | None = None,
    estado: str | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
):
    query = build_vtv_query(
        db,
        filter_field,
        filter_value,
        sort_field,
        sort_order,
        registro_marca,
        dependencia_id,
        tipo_vtvResultado_id,
        zona,
        estado,
        fecha_desde,
        fecha_hasta
    )    
    return query.all()

def get_by_vehiculoId(db: Session, vehiculo_id: int):
    return (
        db.query(Vtv)
        .filter(Vtv.vehiculo_id == vehiculo_id)
        .order_by(desc(Vtv.id))
        .all()
    )

def get_by_id(db: Session, id: int):
    return db.query(Vtv).filter(Vtv.id == id).first()

def get_last_vtvId_by_vehiculo(db: Session, vehiculo_id: int):
    # 🔎 Buscar última VTV del vehículo
    return (
        db.query(Vtv)
        .filter(Vtv.vehiculo_id == vehiculo_id)
        .order_by(Vtv.id.desc())
        .first()
    )

def create(db: Session, vtv: VtvCreate):
    db_vtv = Vtv(**vtv.model_dump())
    db.add(db_vtv)

    # Actualizar Vehiculo Fecha VTV
    if vtv.fecha_vto: 
        vehiculo = db.query(VehiculoModel).filter(VehiculoModel.id == db_vtv.vehiculo_id).first()
        if vehiculo:
            vehiculo.fechaVtv = vtv.fecha_vto
    db.commit()
    db.refresh(db_vtv)
    return db_vtv

def update(db: Session, id: int, vtv: VtvUpdate):
    db_vtv = get_by_id(db, id)
    if not db_vtv:
        return None
    for field, value in vtv.model_dump(exclude_unset=True).items():
        setattr(db_vtv, field, value)
    db.commit()
    db.refresh(db_vtv)
    return db_vtv

def delete(db: Session, id: int):
    db_vtv = get_by_id(db, id)
    if db_vtv:
        db.delete(db_vtv)
        db.commit()
    return db_vtv

""" REPORTES """
def get_vtvVencidas(db: Session):
    """
    Devuelve la cantidad de vtvs vencidas.
    Ejemplo de salida: [{ "cantidad": 20 }, ...]
    """
    today = date.today()
    subq = (
        db.query(
            Vtv.vehiculo_id,
            func.max(Vtv.fecha_vto).label("ultima_vto")
        )
        .filter(Vtv.fecha_vto != None)
        .group_by(Vtv.vehiculo_id)
        .subquery()
    )

    results = (
        db.query(func.count().label("value"))
        .filter(subq.c.ultima_vto < today)
        .all()
    )
    return [{"value": r.value} for r in results]

def get_vtvVencer(db: Session):
    """
    Devuelve la cantidad de VTV que vencen en los próximos 30 días.
    """
    today = date.today()
    limite = today + timedelta(days=30)

    subq = (
        db.query(
            Vtv.vehiculo_id,
            func.max(Vtv.fecha_vto).label("ultima_vto")
        )
        .filter(Vtv.fecha_vto != None)
        .group_by(Vtv.vehiculo_id)
        .subquery()
    )
    results = (
        db.query(func.count().label("value"))
        .filter(subq.c.ultima_vto >= today)
        .filter(subq.c.ultima_vto <= limite)
        .all()
    )
    return [{"value": r.value} for r in results]