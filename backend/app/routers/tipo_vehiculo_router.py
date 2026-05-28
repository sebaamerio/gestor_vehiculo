from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_vehiculo_schema import TipoVehiculo, TipoVehiculoCreate
from ..services import tipo_vehiculo_service

router = APIRouter(prefix="/tipo_vehiculo", tags=["TipoVehiculos"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoVehiculo])
def list_tipo_vehiculos(db: Session = Depends(get_db)):
    return tipo_vehiculo_service.get_all(db)


@router.get("/{id}", response_model=TipoVehiculo)
def get_tipo_vehiculo(id: int, db: Session = Depends(get_db)):
    return tipo_vehiculo_service.get_by_id(db, id)


@router.post("/", response_model=TipoVehiculo, dependencies=[Depends(require_role("admin"))])
def create_tipo_vehiculo(tipo_vehiculo: TipoVehiculoCreate, db: Session = Depends(get_db)):
    return tipo_vehiculo_service.create(db, tipo_vehiculo)


@router.put("/{id}", response_model=TipoVehiculo, dependencies=[Depends(require_role("admin"))])
def update_tipo_vehiculo(id: int, tipo_vehiculo: TipoVehiculoCreate, db: Session = Depends(get_db)):
    return tipo_vehiculo_service.update(db, id, tipo_vehiculo)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_vehiculo(id: int, db: Session = Depends(get_db)):
    return tipo_vehiculo_service.delete(db, id)
