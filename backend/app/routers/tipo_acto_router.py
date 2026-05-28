from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_acto_schema import TipoActo, TipoActoCreate
from ..services import tipo_acto_service

router = APIRouter(prefix="/tipo_acto", tags=["TipoActo"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoActo])
def list_tipo_actoss(db: Session = Depends(get_db)):
    return tipo_acto_service.get_all(db)


@router.get("/{id}", response_model=TipoActo)
def get_tipo_acto(id: int, db: Session = Depends(get_db)):
    return tipo_acto_service.get_by_id(db, id)


@router.post("/", response_model=TipoActo, dependencies=[Depends(require_role("admin"))])
def create_tipo_acto(data: TipoActoCreate, db: Session = Depends(get_db)):
    return tipo_acto_service.create(db, data)


@router.put("/{id}", response_model=TipoActo, dependencies=[Depends(require_role("admin"))])
def update_tipo_acto(id: int, data: TipoActoCreate, db: Session = Depends(get_db)):
    return tipo_acto_service.update(db, id, data)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_acto(id: int, db: Session = Depends(get_db)):
    return tipo_acto_service.delete(db, id)
