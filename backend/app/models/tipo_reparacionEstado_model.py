from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class TipoReparacionEstado(Base):
    __tablename__ = "tipo_reparacion_estado"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), unique=True, nullable=False)

    # Relación ORM
    reparaciones = relationship("Reparacion", back_populates="tipo_reparacion_estado")