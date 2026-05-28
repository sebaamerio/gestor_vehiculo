from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.accidente_schema import Accidente, AccidenteUpdate
from ..services import accidente_service

router = APIRouter(prefix="/accidente", tags=["Accidente"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=Accidente)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return accidente_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================

@router.get("/", response_model=list[Accidente])
def list(db: Session = Depends(get_db)):
    return accidente_service.get_all(db)

@router.get("/{id}", response_model=Accidente)
def get(id: int, db: Session = Depends(get_db)):
    return accidente_service.get_by_id(db, id)

@router.put("/{id}", response_model=Accidente, dependencies=[Depends(require_role("admin"))])
def update(id: int, item: AccidenteUpdate, db: Session = Depends(get_db)):
    return accidente_service.update(db, id, item)
