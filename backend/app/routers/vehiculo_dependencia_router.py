from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.vehiculo_dependencia_schema import VehiculoDependencia, VehiculoDependenciaCreate, VehiculoDependenciaUpdate
from ..services import vehiculo_dependencia_service

router = APIRouter(prefix="/VehiculoDependencia", tags=["VehiculoDependencia"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[VehiculoDependencia])
def list(db: Session = Depends(get_db)):
    return vehiculo_dependencia_service.get_all(db)


@router.get("/{id}", response_model=VehiculoDependencia)
def get(id: int, db: Session = Depends(get_db)):
    return vehiculo_dependencia_service.get_by_id(db, id)


@router.post("/", response_model=VehiculoDependencia, dependencies=[Depends(require_role("admin"))])
def create(data: VehiculoDependenciaCreate, db: Session = Depends(get_db)):
    return vehiculo_dependencia_service.create(db, data)


@router.put("/{id}", response_model=VehiculoDependencia, dependencies=[Depends(require_role("admin"))])
def update(id: int, data: VehiculoDependenciaUpdate, db: Session = Depends(get_db)):
    return vehiculo_dependencia_service.update(db, id, data)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete(id: int, db: Session = Depends(get_db)):
    return vehiculo_dependencia_service.delete(db, id)