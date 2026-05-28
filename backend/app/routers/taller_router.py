from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.taller_schema import Taller, TallerCreate, TallerUpdate
from ..services import taller_service

router = APIRouter(prefix="/taller", tags=["Taller"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[Taller])
def list(db: Session = Depends(get_db)):
    return taller_service.get_all(db)


@router.get("/{id}", response_model=Taller)
def get(id: int, db: Session = Depends(get_db)):
    return taller_service.get_by_id(db, id)


@router.post("/", response_model=Taller, dependencies=[Depends(require_role("admin"))])
def create(data: TallerCreate, db: Session = Depends(get_db)):
    return taller_service.create(db, data)


@router.put("/{id}", response_model=Taller, dependencies=[Depends(require_role("admin"))])
def update(id: int, data: TallerUpdate, db: Session = Depends(get_db)):
    return taller_service.update(db, id, data)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete(id: int, db: Session = Depends(get_db)):
    return taller_service.delete(db, id)
