from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.provincia_schema import Provincia, ProvinciaCreate
from ..services import provincia_service

router = APIRouter(prefix="/provincias", tags=["Provincias"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[Provincia])
def listar_provincias(db: Session = Depends(get_db)):
    return provincia_service.get_all(db)

@router.get("/{id}", response_model=Provincia)
def obtener_provincia(id: int, db: Session = Depends(get_db)):
    provincia = provincia_service.get_by_id(db, id)
    if not provincia:
        raise HTTPException(status_code=404, detail="Provincia no encontrada")
    return provincia

@router.post("/", response_model=Provincia, dependencies=[Depends(require_role("admin"))])
def crear_provincia(provincia: ProvinciaCreate, db: Session = Depends(get_db)):
    return provincia_service.create(db, provincia)

@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def eliminar_provincia(id: int, db: Session = Depends(get_db)):
    provincia = provincia_service.delete(db, id)
    if not provincia:
        raise HTTPException(status_code=404, detail="Provincia no encontrada")
    return {"mensaje": "Provincia eliminada correctamente"}
