from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_vtvResultado_schema import TipoVtvResultado, TipoVtvResultadoCreate
from ..services import tipo_vtvResultado_service

router = APIRouter(prefix="/tipo_vtvResultado", tags=["TipoVtvResultado"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoVtvResultado])
def list_tipo_vtvResultado(db: Session = Depends(get_db)):
    return tipo_vtvResultado_service.get_all(db)


@router.get("/{id}", response_model=TipoVtvResultado)
def get_tipo_vtvResultado(id: int, db: Session = Depends(get_db)):
    return tipo_vtvResultado_service.get_by_id(db, id)


@router.post("/", response_model=TipoVtvResultado, dependencies=[Depends(require_role("admin"))])
def create_tipo_vtvResultado(tipo_vehiculo: TipoVtvResultadoCreate, db: Session = Depends(get_db)):
    return tipo_vtvResultado_service.create(db, tipo_vehiculo)


@router.put("/{id}", response_model=TipoVtvResultado, dependencies=[Depends(require_role("admin"))])
def update_tipo_vtvResultado(id: int, tipo_vehiculo: TipoVtvResultadoCreate, db: Session = Depends(get_db)):
    return tipo_vtvResultado_service.update(db, id, tipo_vehiculo)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_vtvResultado(id: int, db: Session = Depends(get_db)):
    return tipo_vtvResultado_service.delete(db, id)
