from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.dependencia_schema import Dependencia, DependenciaCreate, DependenciaUpdate
from ..services import dependencia_service

router = APIRouter(prefix="/dependencia", tags=["Dependencia"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[Dependencia])
def list_dependencia(db: Session = Depends(get_db)):
    return dependencia_service.get_all(db)


@router.get("/{id}", response_model=Dependencia)
def get_dependencia(id: int, db: Session = Depends(get_db)):
    return dependencia_service.get_by_id(db, id)


@router.post("/", response_model=Dependencia, dependencies=[Depends(require_role("admin"))])
def create_dependencia(dependencia: DependenciaCreate, db: Session = Depends(get_db)):
    return dependencia_service.create(db, dependencia)


@router.put("/{id}", response_model=Dependencia, dependencies=[Depends(require_role("admin"))])
def update_dependencia(id: int, dependencia: DependenciaUpdate, db: Session = Depends(get_db)):
    return dependencia_service.update(db, id, dependencia)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_dependencia(id: int, db: Session = Depends(get_db)):
    return dependencia_service.delete(db, id)