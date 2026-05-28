from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_modelo_schema import TipoModelo, TipoModeloCreate
from ..services import tipo_modelo_service

router = APIRouter(prefix="/tipo_modelo", tags=["TipoModelo"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoModelo])
def list_tipo_modelos(db: Session = Depends(get_db)):
    return tipo_modelo_service.get_all(db)


@router.get("/{id}", response_model=TipoModelo)
def get_tipo_modelo(id: int, db: Session = Depends(get_db)):
    return tipo_modelo_service.get_by_id(db, id)


@router.post("/", response_model=TipoModelo, dependencies=[Depends(require_role("admin"))])
def create_tipo_modelo(tipo_modelo: TipoModeloCreate, db: Session = Depends(get_db)):
    return tipo_modelo_service.create(db, tipo_modelo)


@router.put("/{id}", response_model=TipoModelo, dependencies=[Depends(require_role("admin"))])
def update_tipo_modelo(id: int, tipo_modelo: TipoModeloCreate, db: Session = Depends(get_db)):
    return tipo_modelo_service.update(db, id, tipo_modelo)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_modelo(id: int, db: Session = Depends(get_db)):
    return tipo_modelo_service.delete(db, id)
