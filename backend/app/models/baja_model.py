from sqlalchemy import Column, Integer, BigInteger, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Baja(Base):
    __tablename__ = "bajas"

    id = Column(Integer, primary_key=True, index=True)
    novedad_id = Column(Integer, ForeignKey("novedades.id"), nullable=False, unique=True) # Unique, solo 1 baja por novedad
    fecha = Column(Date, nullable=False)
    expediente = Column(String(50), nullable=True)
    informe = Column(String(50), nullable=True)
    acto_id = Column(Integer, ForeignKey("tipo_acto.id"), nullable=True) 
    norma = Column(String(50), nullable=True)

    # Relación ORM
    novedad = relationship("Novedad", back_populates="baja")
    tipo_acto = relationship("TipoActo") 