from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.transferencia_schema import Transferencia, TransferenciaUpdate
from ..services import transferencia_service

router = APIRouter(prefix="/transferencia", tags=["Transferencia"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=Transferencia)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return transferencia_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================
@router.get("/", response_model=list[Transferencia])
def list(db: Session = Depends(get_db)):
    return transferencia_service.get_all(db)

@router.get("/{id}", response_model=Transferencia)
def get(id: int, db: Session = Depends(get_db)):
    return transferencia_service.get_by_id(db, id)

@router.put("/{id}", response_model=Transferencia, dependencies=[Depends(require_role("admin"))])
def update(id: int, item: TransferenciaUpdate, db: Session = Depends(get_db)):
    return transferencia_service.update(db, id, item)