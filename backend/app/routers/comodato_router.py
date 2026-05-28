from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.comodato_schema import Comodato, ComodatoUpdate
from ..services import comodato_service

router = APIRouter(prefix="/comodato", tags=["Comodato"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=Comodato)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return comodato_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================

@router.get("/", response_model=list[Comodato])
def list_comodato(db: Session = Depends(get_db)):
    return comodato_service.get_all(db)

@router.get("/{id}", response_model=Comodato)
def get_comodato(id: int, db: Session = Depends(get_db)):
    return comodato_service.get_by_id(db, id)

@router.put("/{id}", response_model=Comodato, dependencies=[Depends(require_role("admin"))])
def update_comodato(id: int, item: ComodatoUpdate, db: Session = Depends(get_db)):
    return comodato_service.update(db, id, item)