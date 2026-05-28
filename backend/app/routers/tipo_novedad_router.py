from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_novedad_schema import TipoNovedad, TipoNovedadCreate
from ..services import tipo_novedad_service

router = APIRouter(prefix="/tipo_novedad", tags=["TipoNovedad"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoNovedad])
def list_tipo_novedad(db: Session = Depends(get_db)):
    return tipo_novedad_service.get_all(db)


@router.get("/{id}", response_model=TipoNovedad)
def get_tipo_novedad(id: int, db: Session = Depends(get_db)):
    return tipo_novedad_service.get_by_id(db, id)


@router.post("/", response_model=TipoNovedad, dependencies=[Depends(require_role("admin"))])
def create_tipo_novedad(tipo_vehiculo: TipoNovedadCreate, db: Session = Depends(get_db)):
    return tipo_novedad_service.create(db, tipo_vehiculo)


@router.put("/{id}", response_model=TipoNovedad, dependencies=[Depends(require_role("admin"))])
def update_tipo_novedad(id: int, tipo_vehiculo: TipoNovedadCreate, db: Session = Depends(get_db)):
    return tipo_novedad_service.update(db, id, tipo_vehiculo)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_novedad(id: int, db: Session = Depends(get_db)):
    return tipo_novedad_service.delete(db, id)
