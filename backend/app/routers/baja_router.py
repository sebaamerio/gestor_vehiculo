from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.baja_schema import Baja, BajaUpdate
from ..services import baja_service

router = APIRouter(prefix="/baja", tags=["Baja"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=Baja)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return baja_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================
@router.get("/", response_model=list[Baja])
def list_bajas(db: Session = Depends(get_db)):
    return baja_service.get_all(db)


@router.get("/{id}", response_model=Baja)
def get_baja(id: int, db: Session = Depends(get_db)):
    return baja_service.get_by_id(db, id)

@router.put("/{id}", response_model=Baja, dependencies=[Depends(require_role("admin"))])
def update_baja(id: int, baja: BajaUpdate, db: Session = Depends(get_db)):
    return baja_service.update(db, id, baja)


