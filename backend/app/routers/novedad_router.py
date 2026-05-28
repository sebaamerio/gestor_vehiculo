from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..core.deps import get_current_user, require_role
from ..services import novedad_service
from ..schemas.novedad_schema import Novedad, NovedadUpdate, NovedadPayload, NovedadResponse

router = APIRouter(prefix="/novedades", tags=["Novedad"], dependencies=[Depends(get_current_user)])

@router.get("/stats/by_tipo")
def get_novedades_by_tipo(db: Session = Depends(get_db)):
    return novedad_service.get_by_tipo(db)

@router.get("/by_vehiculo/{vehiculo_id}", response_model=list[Novedad])
def get_novedad_by_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    return novedad_service.get_by_vehiculoId(db, vehiculo_id)

@router.get("/", response_model=list[Novedad])
def list_novedades(db: Session = Depends(get_db)):
    return novedad_service.get_all(db)

@router.get("/{id:int}", response_model=Novedad)
def get_novedad(id: int, db: Session = Depends(get_db)):
    return novedad_service.get_by_id(db, id)

@router.post("/", response_model=NovedadResponse, dependencies=[Depends(require_role("admin"))])
def create_novedad(payload: NovedadPayload, db: Session = Depends(get_db)):
    # El servicio ahora devuelve el NovedadResponse ensamblado
    return novedad_service.create(
        db,
        novedad=payload.novedad,
        detalle=payload.detalle
    )

@router.put("/{id}", response_model=Novedad, dependencies=[Depends(require_role("admin"))])
def update_novedad(id: int, novedad: NovedadUpdate, db: Session = Depends(get_db)):
    return novedad_service.update(db, id, novedad)


@router.delete("/{id}", dependencies=[Depends(require_role("admin"))])
def delete_novedad(id: int, db: Session = Depends(get_db)):
    return novedad_service.delete(db, id)