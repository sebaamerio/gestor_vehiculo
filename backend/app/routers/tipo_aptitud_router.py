from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_aptitud_schema import TipoAptitud, TipoAptitudCreate
from ..services import tipo_aptitud_service

router = APIRouter(prefix="/tipo_aptitud", tags=["TipoAptitud"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[TipoAptitud])
def list_tipo_aptitud(db: Session = Depends(get_db)):
    return tipo_aptitud_service.get_all(db)

@router.get("/{id}", response_model=TipoAptitud)
def get_tipo_aptitud(id: int, db: Session = Depends(get_db)):
    return tipo_aptitud_service.get_by_id(db, id)

@router.post("/", response_model=TipoAptitud, dependencies=[Depends(require_role("admin"))])
def create_tipo_aptitud(data: TipoAptitudCreate, db: Session = Depends(get_db)):
    return tipo_aptitud_service.create(db, data)

@router.put("/{id}", response_model=TipoAptitud, dependencies=[Depends(require_role("admin"))])
def update_tipo_aptitud(id: int, data: TipoAptitudCreate, db: Session = Depends(get_db)):
    return tipo_aptitud_service.update(db, id, data)

@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_aptitud(id: int, db: Session = Depends(get_db)):
    return tipo_aptitud_service.delete(db, id)