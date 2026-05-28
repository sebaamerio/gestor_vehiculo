from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from openpyxl import Workbook
from io import BytesIO
from fastapi.responses import StreamingResponse
from ..repositories import vtv_repository
from ..schemas.vtv_schema import VtvCreate, VtvUpdate

# Consultas

def get_all(db: Session):
    return vtv_repository.get_all(db)

def get_paginated(db, page, 
                page_size,
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
                fecha_hasta):
    return vtv_repository.get_paginated(
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

def get_report_vtv_excel(db,
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
                            fecha_hasta):

    wb = Workbook(write_only=True)
    ws = wb.create_sheet("Vehículos")

    ws.append(["Tipo", "RO", "Nro. Solicitud", "F. Solicitud", "Realizado", "Vencimiento", "Resultado", "Oblea", "Dependencia_Id", "Dependencia", "Zona"])

    rows = vtv_repository.get_paginated_vtv_report(db,
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
    
    # 👇 desempaquetar las columnas
    for v in rows:
        ws.append([
            "RO" if v.vehiculo.registro_marca else "RI",           
            v.vehiculo.registro_nro,
            v.id,
            v.fecha_solicitud,
            v.fecha_realizada,
            v.fecha_vto,
            v.tipo_vtvResultado.descripcion if v.tipo_vtvResultado else None,
            v.oblea,
            v.vehiculo.dependencia.dependencia_id if v.vehiculo.dependencia else None,
            v.vehiculo.dependencia.dependencia_descripcion if v.vehiculo.dependencia else None,
            v.zona
        ])

    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition":
            "attachment; filename=vtv_reporte.xlsx"
        }
    )

def get_by_vehiculoId(db: Session, vehiculo_id: int):
    item = vtv_repository.get_by_vehiculoId(db, vehiculo_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vtv para el vehiculo={vehiculo_id} no encontrado"
        )
    return item

def get_by_id(db: Session, id: int):
    item = vtv_repository.get_by_id(db, id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vtv con id={id} no encontrado"
        )
    return item

def create(db: Session, vtv: VtvCreate):
    # 🔎 Buscar última VTV del vehículo
    ultima_vtv = vtv_repository.get_last_vtvId_by_vehiculo(
        db, vtv.vehiculo_id
    )

    # 🚨 Validar regla de negocio
    if ultima_vtv:
        if not ultima_vtv.tipo_vtvResultado_id or not ultima_vtv.fecha_realizada:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No se puede generar una nueva solicitud. La VTV anterior no tiene cargado el resultado o las fechas."
            )

    # ✅ Crear nueva solicitud
    return vtv_repository.create(db, vtv)

def update(db: Session, id: int, vtv: VtvUpdate):
    db_vtv = vtv_repository.update(db, id, vtv)
    if not db_vtv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vtv con id={id} no encontrado"
        )
    return db_vtv

def delete(db: Session, id: int):
    deleted = vtv_repository.delete(db, id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vtv con id={id} no encontrado"
        )
    return {"message": f"Vtv con id={id} eliminado correctamente"}

# Consultas
def get_by_vencidas(db: Session):
    return vtv_repository.get_vtvVencidas(db)

def get_by_vencer(db: Session):
    return vtv_repository.get_vtvVencer(db)