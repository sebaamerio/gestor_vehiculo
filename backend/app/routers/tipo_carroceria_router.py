from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_carroceria_schema import TipoCarroceria, TipoCarroceriaCreate
from ..services import tipo_carroceria_service

router = APIRouter(prefix="/tipo_carroceria", tags=["TipoCarroceria"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoCarroceria])
def list_tipo_carrocerias(db: Session = Depends(get_db)):
    return tipo_carroceria_service.get_all(db)


@router.get("/{id}", response_model=TipoCarroceria)
def get_tipo_carroceria(id: int, db: Session = Depends(get_db)):
    return tipo_carroceria_service.get_by_id(db, id)


@router.post("/", response_model=TipoCarroceria, dependencies=[Depends(require_role("admin"))])
def create_tipo_carroceria(tipo_carroceria: TipoCarroceriaCreate, db: Session = Depends(get_db)):
    return tipo_carroceria_service.create(db, tipo_carroceria)


@router.put("/{id}", response_model=TipoCarroceria, dependencies=[Depends(require_role("admin"))])
def update_tipo_carroceria(id: int, tipo_carroceria: TipoCarroceriaCreate, db: Session = Depends(get_db)):
    return tipo_carroceria_service.update(db, id, tipo_carroceria)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_carroceria(id: int, db: Session = Depends(get_db)):
    return tipo_carroceria_service.delete(db, id)
