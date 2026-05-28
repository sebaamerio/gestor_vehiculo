from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.localidad_schema import LocalidadCreate, Localidad
from ..services import localidad_service

router = APIRouter(prefix="/localidades", tags=["Localidades"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[Localidad])
def listar_localidades(db: Session = Depends(get_db)):
    return localidad_service.get_all(db)

@router.get("/{id}", response_model=Localidad)
def obtener_localidad(id: int, db: Session = Depends(get_db)):
    localidad = localidad_service.get_by_id(db, id)
    if not localidad:
        raise HTTPException(status_code=404, detail="Localidad no encontrada")
    return localidad

@router.post("/", response_model=Localidad, dependencies=[Depends(require_role("admin"))])
def crear_localidad(localidad: LocalidadCreate, db: Session = Depends(get_db)):
    return localidad_service.create(db, localidad)

@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def eliminar_localidad(id: int, db: Session = Depends(get_db)):
    localidad = localidad_service.delete(db, id)
    if not localidad:
        raise HTTPException(status_code=404, detail="Localidad no encontrada")
    return {"mensaje": "Localidad eliminada correctamente"}
