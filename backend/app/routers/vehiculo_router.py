from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from datetime import date
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.vehiculo_schema import (
    VehiculoPaginated,
    Vehiculo,
    VehiculoCreate,
    VehiculoUpdate,
    Vehiculo_by_Anio,
    Vehiculo_by_Dependencia,
    Vehiculo_by_Condicion,   
    HistorialDependenciaSchema
    )

from ..services import vehiculo_service
from ..services.pdf_service import procesar_pdf


router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de reportes
# ========================

@router.get("/report/byAnio", response_model=list[Vehiculo_by_Anio])
def get_by_anio(db: Session = Depends(get_db)):
    return vehiculo_service.get_by_anio(db)

@router.get("/report/byDependencia", response_model=list[Vehiculo_by_Dependencia])
def get_by_dependencia(db: Session = Depends(get_db)):
    return vehiculo_service.get_by_dependencia(db)

@router.get("/report/byCondicion", response_model=list[Vehiculo_by_Condicion])
def get_by_condicion(db: Session = Depends(get_db)):
    return vehiculo_service.get_by_condicion(db)

@router.get("/report/bySituacion", response_model=list[Vehiculo_by_Condicion])
def get_by_situacion(db: Session = Depends(get_db)):
    return vehiculo_service.get_by_situacion(db)

@router.get("/report/by_vehiculo_dependencia_activos/excel")
def download_report_vehiculo_dependencia_activos(
    db: Session = Depends(get_db)
):
    return vehiculo_service.report_vehiculo_dependencia_activos(db)

# ========================
#  Reporte de la Grilla VEHICULO
# ========================
@router.get("/report/vehiculos_filtros/excel")
def download_report_vehiculo_filtros(    
    # filtros simples (DataGrid)
    filter_field: str | None = None,
    filter_value: str | None = None,

    # orden
    sort_field: str | None = None,
    sort_order: str | None = None,  # "asc" o "desc",

    # filtros avanzados
    registro_marca: bool | None = None,
    dependencia_id: int | None = None,
    situacion_id: int | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,
    db: Session = Depends(get_db)):   
        
    return vehiculo_service.get_report_vehiculo_excel(
        db=db,        
        filter_field=filter_field,
        filter_value=filter_value,
        sort_field=sort_field,
        sort_order=sort_order,
        registro_marca=registro_marca,
        dependencia_id=dependencia_id,
        situacion_id=situacion_id,
        fecha_desde=fecha_desde,
        fecha_hasta=fecha_hasta
    )
    
@router.get("/historial/dependencia/{vehiculo_id}", response_model=list[HistorialDependenciaSchema])
def get_HistorialDependencia(vehiculo_id: int, db: Session = Depends(get_db)):
    return vehiculo_service.get_historial_dependencias(vehiculo_id, db)

# ========================
#  Titulo vehiculo PDF
# ========================

@router.post("/titulo/pdf", dependencies=[Depends(require_role("admin"))])
async def extraer_pdf(file: UploadFile = File(...)):
    """
    Sube un PDF, valida que sea solo texto y devuelve el JSON automotor procesado.
    """

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Debe subir un archivo PDF.")

    return await procesar_pdf(file)

# ========================
# Sección CRUD 
# ========================

@router.get("/", response_model=VehiculoPaginated)
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
    situacion_id: int | None = None,
    fecha_desde: date | None = None,
    fecha_hasta: date | None = None,

    db: Session = Depends(get_db)):
    return vehiculo_service.get_paginated(
        db=db,
        page=page,
        page_size=page_size,
        filter_field=filter_field,
        filter_value=filter_value,
        sort_field=sort_field,
        sort_order=sort_order,
        registro_marca=registro_marca,
        dependencia_id=dependencia_id,
        situacion_id=situacion_id,
        fecha_desde=fecha_desde,
        fecha_hasta=fecha_hasta
    )

@router.get("/{id}", response_model=Vehiculo)
def get_vehiculo(id: int, db: Session = Depends(get_db)):
    return vehiculo_service.get_by_id(db, id)


@router.post("/", response_model=Vehiculo, dependencies=[Depends(require_role("admin"))])
def create_vehiculo(vehiculo: VehiculoCreate, db: Session = Depends(get_db)):  
    return vehiculo_service.create(db, vehiculo)


@router.put("/{id}", response_model=Vehiculo, dependencies=[Depends(require_role("admin"))])
def update_vehiculo(id: int, vehiculo: VehiculoUpdate, db: Session = Depends(get_db)):
    return vehiculo_service.update(db, id, vehiculo)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_vehiculo(id: int, db: Session = Depends(get_db)):
    return vehiculo_service.delete(db, id)