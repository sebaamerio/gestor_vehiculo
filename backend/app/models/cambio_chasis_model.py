from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class CambioChasis(Base):
    __tablename__ = "cambio_chasis"

    id = Column(Integer, primary_key=True, index=True)
    novedad_id = Column(Integer, ForeignKey("novedades.id"), nullable=False, unique=True) # Unique, solo 1 cambio por novedad
    chasis_anterior = Column(String(50), nullable=False)
    chasis_nuevo = Column(String(50), nullable=False)
    fecha = Column(Date, nullable=False)
    expediente = Column(String(50), nullable=True)
    informe = Column(String(50), nullable=True)
    acto_id = Column(Integer, ForeignKey("tipo_acto.id"), nullable=True) 
    norma = Column(String(50), nullable=True)

    # Relación ORM
    novedad = relationship("Novedad", back_populates="cambio_chasis")
    tipo_acto = relationship("TipoActo")