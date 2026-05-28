from sqlalchemy import Column, Integer, String
from ..core.database import Base

class TipoSituacionChofer(Base):
    __tablename__ = "tipo_situacion_chofer"  

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), unique=True, nullable=False)