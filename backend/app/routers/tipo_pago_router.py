from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_pago_schema import TipoPago, TipoPagoCreate
from ..services import tipo_pago_service

router = APIRouter(prefix="/tipo_pago", tags=["TipoPago"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoPago])
def list_tipo_pago(db: Session = Depends(get_db)):
    return tipo_pago_service.get_all(db)


@router.get("/{id}", response_model=TipoPago)
def get_tipo_pago(id: int, db: Session = Depends(get_db)):
    return tipo_pago_service.get_by_id(db, id)


@router.post("/", response_model=TipoPago, dependencies=[Depends(require_role("admin"))])
def create_tipo_pago(data: TipoPagoCreate, db: Session = Depends(get_db)):
    return tipo_pago_service.create(db, data)


@router.put("/{id}", response_model=TipoPago, dependencies=[Depends(require_role("admin"))])
def update_tipo_pago(id: int, data: TipoPagoCreate, db: Session = Depends(get_db)):
    return tipo_pago_service.update(db, id, data)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_pago(id: int, db: Session = Depends(get_db)):
    return tipo_pago_service.delete(db, id)
