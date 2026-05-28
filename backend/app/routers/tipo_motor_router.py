from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_motor_schema import TipoMotor, TipoMotorCreate
from ..services import tipo_motor_service

router = APIRouter(prefix="/tipo_motor", tags=["TipoMotor"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoMotor])
def list_tipo_motor(db: Session = Depends(get_db)):
    return tipo_motor_service.get_all(db)


@router.get("/{id}", response_model=TipoMotor)
def get_tipo_motor(id: int, db: Session = Depends(get_db)):
    return tipo_motor_service.get_by_id(db, id)


@router.post("/", response_model=TipoMotor, dependencies=[Depends(require_role("admin"))])
def create_tipo_motor(tipo_vehiculo: TipoMotorCreate, db: Session = Depends(get_db)):
    return tipo_motor_service.create(db, tipo_vehiculo)


@router.put("/{id}", response_model=TipoMotor, dependencies=[Depends(require_role("admin"))])
def update_tipo_motor(id: int, tipo_vehiculo: TipoMotorCreate, db: Session = Depends(get_db)):
    return tipo_motor_service.update(db, id, tipo_vehiculo)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_motor(id: int, db: Session = Depends(get_db)):
    return tipo_motor_service.delete(db, id)
