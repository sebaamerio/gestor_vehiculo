from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_marca_schema import TipoMarca, TipoMarcaCreate
from ..services import tipo_marca_service

router = APIRouter(prefix="/tipo_marca", tags=["TipoMarca"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoMarca])
def list_tipo_marcas(db: Session = Depends(get_db)):
    return tipo_marca_service.get_all(db)


@router.get("/{id}", response_model=TipoMarca)
def get_tipo_marca(id: int, db: Session = Depends(get_db)):
    return tipo_marca_service.get_by_id(db, id)


@router.post("/", response_model=TipoMarca, dependencies=[Depends(require_role("admin"))])
def create_tipo_marca(tipo_marca: TipoMarcaCreate, db: Session = Depends(get_db)):
    return tipo_marca_service.create(db, tipo_marca)


@router.put("/{id}", response_model=TipoMarca, dependencies=[Depends(require_role("admin"))])
def update_tipo_marca(id: int, tipo_marca: TipoMarcaCreate, db: Session = Depends(get_db)):
    return tipo_marca_service.update(db, id, tipo_marca)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_marca(id: int, db: Session = Depends(get_db)):
    return tipo_marca_service.delete(db, id)
