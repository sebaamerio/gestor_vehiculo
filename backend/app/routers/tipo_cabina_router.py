from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_cabina_schema import TipoCabina, TipoCabinaCreate
from ..services import tipo_cabina_service

router = APIRouter(prefix="/tipo_cabina", tags=["TipoCabina"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[TipoCabina])
def list_tipo_cabina(db: Session = Depends(get_db)):
    return tipo_cabina_service.get_all(db)

@router.get("/{id}", response_model=TipoCabina)
def get_tipo_cabina(id: int, db: Session = Depends(get_db)):
    return tipo_cabina_service.get_by_id(db, id)

@router.post("/", response_model=TipoCabina, dependencies=[Depends(require_role("admin"))])
def create_tipo_cabina(data: TipoCabinaCreate, db: Session = Depends(get_db)):
    return tipo_cabina_service.create(db, data)

@router.put("/{id}", response_model=TipoCabina, dependencies=[Depends(require_role("admin"))])
def update_tipo_cabina(id: int, data: TipoCabinaCreate, db: Session = Depends(get_db)):
    return tipo_cabina_service.update(db, id, data)

@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_cabina(id: int, db: Session = Depends(get_db)):
    return tipo_cabina_service.delete(db, id)