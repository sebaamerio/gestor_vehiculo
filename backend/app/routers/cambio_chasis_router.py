from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.cambio_chasis_schema import CambioChasis, CambioChasisUpdate
from ..services import cambio_chasis_service

router = APIRouter(prefix="/cambio_chasis", tags=["CambioChasis"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=CambioChasis)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return cambio_chasis_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================

@router.get("/", response_model=list[CambioChasis])
def list(db: Session = Depends(get_db)):
    return cambio_chasis_service.get_all(db)


@router.get("/{id}", response_model=CambioChasis)
def get(id: int, db: Session = Depends(get_db)):
    return cambio_chasis_service.get_by_id(db, id)

@router.put("/{id}", response_model=CambioChasis, dependencies=[Depends(require_role("admin"))])
def update(id: int, data: CambioChasisUpdate, db: Session = Depends(get_db)):
    return cambio_chasis_service.update(db, id, data)
