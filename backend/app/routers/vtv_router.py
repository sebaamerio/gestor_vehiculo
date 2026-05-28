from fastapi import APIRouter, Depends
from datetime import date
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.vtv_schema import Vtv, VtvCreate, VtvUpdate, VtvPaginated, vtvVencida
from ..services import vtv_service

router = APIRouter(prefix="/vtvs", tags=["Vtv"], dependencies=[Depends(get_current_user)])

@router.get("/by_vehiculo/{vehiculo_id}", response_model=list[Vtv])
def get_Vtv_by_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    return vtv_service.get_by_vehiculoId(db, vehiculo_id)

# ========================
#  Reportes
# ========================
@router.get("/report/vtv_filtros/excel", response_model=VtvPaginated)
def download_report_vtv_filtros(     
    # filtros simples (DataGrid)
    filter_field: str | None = None,
    filter_value: str | None = None,

    # orden
    sort_field: str | None = None,
    sort_order: str | None = None,  # "asc" o "desc",

    # filtros avanzados
    registro_marca: bool | None = None,
    dependencia_id: int | None = None,
    tipo_vtvResultado_id: int | None = None,
    zona: int | None = None,
    estado: str  | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
    db: Session = Depends(get_db)):
    return vtv_service.get_report_vtv_excel(
        db=db,       
        filter_field=filter_field,
        filter_value=filter_value,
        sort_field=sort_field,
        sort_order=sort_order,
        registro_marca=registro_marca,
        dependencia_id=dependencia_id,
        tipo_vtvResultado_id=tipo_vtvResultado_id,
        zona=zona,
        estado=estado,
        fecha_desde=fecha_desde,
        fecha_hasta=fecha_hasta
    )

@router.get("/report/vencidas", response_model=list[vtvVencida])
def get_vencidas(db: Session = Depends(get_db)):
    return vtv_service.get_by_vencidas(db)

@router.get("/report/by_vencer", response_model=list[vtvVencida])
def get_by_vencer(db: Session = Depends(get_db)):
    return vtv_service.get_by_vencer(db)

# ========================
# Sección CRUD 
# ========================

@router.get("/", response_model=VtvPaginated)
def list( page: int = 0,
    page_size: int = 15,

    # filtros simples (DataGrid)
    filter_field: str | None = None,
    filter_value: str | None = None,

    # orden
    sort_field: str | None = None,
    sort_order: str | None = None,  # "asc" o "desc",

    # filtros avanzados
    registro_marca: bool | None = None,
    dependencia_id: int | None = None,
    tipo_vtvResultado_id: int | None = None,
    zona: int | None = None,
    estado: str  | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,

    db: Session = Depends(get_db)):
    return vtv_service.get_paginated(
        db=db,
        page=page,
        page_size=page_size,
        filter_field=filter_field,
        filter_value=filter_value,
        sort_field=sort_field,
        sort_order=sort_order,
        registro_marca=registro_marca,
        dependencia_id=dependencia_id,
        tipo_vtvResultado_id=tipo_vtvResultado_id,
        zona=zona,
        estado=estado,
        fecha_desde=fecha_desde,
        fecha_hasta=fecha_hasta
    )

@router.get("/{id}", response_model=Vtv)
def get_vtv(id: int, db: Session = Depends(get_db)):
    return vtv_service.get_by_id(db, id)

@router.post("/", response_model=Vtv, dependencies=[Depends(require_role("admin"))])
def create_vtv(vtv: VtvCreate, db: Session = Depends(get_db)):
    return vtv_service.create(db, vtv)

@router.put("/{id}", response_model=Vtv, dependencies=[Depends(require_role("admin"))])
def update_Vtv(id: int, vtv: VtvUpdate, db: Session = Depends(get_db)):
    return vtv_service.update(db, id, vtv)

@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_vtv(id: int, db: Session = Depends(get_db)):
    return vtv_service.delete(db, id)