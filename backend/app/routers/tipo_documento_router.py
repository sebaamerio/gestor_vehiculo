from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..schemas.tipo_documento_schema import TipoDocumento, TipoDocumentoCreate
from ..services import tipo_documento_service

router = APIRouter(prefix="/tipo_documento", tags=["TipoDocumento"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=list[TipoDocumento])
def list_tipo_documentos(db: Session = Depends(get_db)):
    return tipo_documento_service.get_all(db)


@router.get("/{id}", response_model=TipoDocumento)
def get_tipo_documento(id: int, db: Session = Depends(get_db)):
    return tipo_documento_service.get_by_id(db, id)


@router.post("/", response_model=TipoDocumento, dependencies=[Depends(require_role("admin"))])
def create_tipo_documento(data: TipoDocumentoCreate, db: Session = Depends(get_db)):
    return tipo_documento_service.create(db, data)


@router.put("/{id}", response_model=TipoDocumento, dependencies=[Depends(require_role("admin"))])
def update_tipo_documento(id: int, data: TipoDocumentoCreate, db: Session = Depends(get_db)):
    return tipo_documento_service.update(db, id, data)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_tipo_documento(id: int, db: Session = Depends(get_db)):
    return tipo_documento_service.delete(db, id)
