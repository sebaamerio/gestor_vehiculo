from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_condicion_schema import TipoCondicion, TipoCondicionCreate
from ..services import tipo_condicion_service

router = APIRouter(prefix="/tipo_condicion", tags=["TipoCondicion"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoCondicion])
def list_tipo_condiciones(db: Session = Depends(get_db)):
    return tipo_condicion_service.get_all(db)


@router.get("/{id}", response_model=TipoCondicion)
def get_tipo_condicion(id: int, db: Session = Depends(get_db)):
    return tipo_condicion_service.get_by_id(db, id)


@router.post("/", response_model=TipoCondicion, dependencies=[Depends(require_role("admin"))])
def create_tipo_condicion(tipo_vehiculo: TipoCondicionCreate, db: Session = Depends(get_db)):
    return tipo_condicion_service.create(db, tipo_vehiculo)


@router.put("/{id}", response_model=TipoCondicion, dependencies=[Depends(require_role("admin"))])
def update_tipo_condicion(id: int, tipo_vehiculo: TipoCondicionCreate, db: Session = Depends(get_db)):
    return tipo_condicion_service.update(db, id, tipo_vehiculo)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_condicion(id: int, db: Session = Depends(get_db)):
    return tipo_condicion_service.delete(db, id)