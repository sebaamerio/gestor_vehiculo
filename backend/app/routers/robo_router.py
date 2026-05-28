from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.robo_schema import Robo, RoboUpdate
from ..services import robo_service

router = APIRouter(prefix="/robo", tags=["Robo"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=Robo)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return robo_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================
@router.get("/", response_model=list[Robo])
def list(db: Session = Depends(get_db)):
    return robo_service.get_all(db)

@router.get("/{id}", response_model=Robo)
def get(id: int, db: Session = Depends(get_db)):
    return robo_service.get_by_id(db, id)

@router.put("/{id}", response_model=Robo, dependencies=[Depends(require_role("admin"))])
def update(id: int, item: RoboUpdate, db: Session = Depends(get_db)):
    return robo_service.update(db, id, item)
