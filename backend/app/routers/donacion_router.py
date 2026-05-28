from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.donacion_schema import Donacion, DonacionUpdate
from ..services import donacion_service

router = APIRouter(prefix="/donacion", tags=["Donacion"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=Donacion)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return donacion_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================

@router.get("/", response_model=list[Donacion])
def list_donaciones(db: Session = Depends(get_db)):
    return donacion_service.get_all(db)

@router.get("/{id}", response_model=Donacion)
def get_donacion(id: int, db: Session = Depends(get_db)):
    return donacion_service.get_by_id(db, id)

@router.put("/{id}", response_model=Donacion, dependencies=[Depends(require_role("admin"))])
def update_donacion(id: int, item: DonacionUpdate, db: Session = Depends(get_db)):
    return donacion_service.update(db, id, item)
