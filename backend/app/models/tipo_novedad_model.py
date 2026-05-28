from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..core.database import Base

class TipoNovedad(Base):
    __tablename__ = "tipo_novedad"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), unique=True, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    # Relación ORM
    novedades = relationship("Novedad", back_populates="tipo_novedad")