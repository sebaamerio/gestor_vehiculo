from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.infraccion_schema import Infraccion, InfraccionUpdate
from ..services import infraccion_service

router = APIRouter(prefix="/infraccion", tags=["Infraccion"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=Infraccion)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return infraccion_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================

@router.get("/", response_model=list[Infraccion])
def list(db: Session = Depends(get_db)):
    return infraccion_service.get_all(db)

@router.get("/{id}", response_model=Infraccion)
def get(id: int, db: Session = Depends(get_db)):
    return infraccion_service.get_by_id(db, id)

@router.put("/{id}", response_model=Infraccion, dependencies=[Depends(require_role("admin"))])
def update(id: int, item: InfraccionUpdate, db: Session = Depends(get_db)):
    return infraccion_service.update(db, id, item)