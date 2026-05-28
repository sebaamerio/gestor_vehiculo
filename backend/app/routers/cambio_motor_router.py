from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.cambio_motor_schema import CambioMotor, CambioMotorUpdate
from ..services import cambio_motor_service

router = APIRouter(prefix="/cambio_motor", tags=["CambioMotor"], dependencies=[Depends(get_current_user)])

# ========================
#  Sección de consultas
# ========================
@router.get("/by_novedad/{novedad_id}", response_model=CambioMotor)
def get_by_novedad( novedad_id: int, db: Session = Depends(get_db)):
    return cambio_motor_service.get_by_NovedadId(db, novedad_id)

# ========================
# Sección CRUD 
# ========================

@router.get("/", response_model=list[CambioMotor])
def list(db: Session = Depends(get_db)):
    return cambio_motor_service.get_all(db)


@router.get("/{id}", response_model=CambioMotor)
def get(id: int, db: Session = Depends(get_db)):
    return cambio_motor_service.get_by_id(db, id)

@router.put("/{id}", response_model=CambioMotor, dependencies=[Depends(require_role("admin"))])
def update(id: int, data: CambioMotorUpdate, db: Session = Depends(get_db)):
    return cambio_motor_service.update(db, id, data)
