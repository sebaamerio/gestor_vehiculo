from sqlalchemy import Column, Integer, String
from ..core.database import Base

class TipoDocumento(Base):
    __tablename__ = "tipo_documento"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), unique=True, nullable=False)