from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_traccion_schema import TipoTraccion, TipoTraccionCreate
from ..services import tipo_traccion_service

router = APIRouter(prefix="/tipo_traccion", tags=["TipoTraccion"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[TipoTraccion])
def list_tipo_traccion(db: Session = Depends(get_db)):
    return tipo_traccion_service.get_all(db)

@router.get("/{id}", response_model=TipoTraccion)
def get_tipo_traccion(id: int, db: Session = Depends(get_db)):
    return tipo_traccion_service.get_by_id(db, id)

@router.post("/", response_model=TipoTraccion, dependencies=[Depends(require_role("admin"))])
def create_tipo_traccion(data: TipoTraccionCreate, db: Session = Depends(get_db)):
    return tipo_traccion_service.create(db, data)

@router.put("/{id}", response_model=TipoTraccion, dependencies=[Depends(require_role("admin"))])
def update_tipo_traccion(id: int, data: TipoTraccionCreate, db: Session = Depends(get_db)):
    return tipo_traccion_service.update(db, id, data)

@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_traccion(id: int, db: Session = Depends(get_db)):
    return tipo_traccion_service.delete(db, id)