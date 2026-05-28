from sqlalchemy import Column, Integer, String, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from ..core.database import Base

class Comodato(Base):
    __tablename__ = "comodato"

    id = Column(Integer, primary_key=True, index=True)
    novedad_id = Column(Integer, ForeignKey("novedades.id"), nullable=False, unique=True) 
    fecha = Column(Date, nullable=False)
    dependencia_id =Column(Integer, nullable=True) 
    dependencia_descripcion =Column(String(100), nullable=True) 
    fecha_fin = Column(Date, nullable=True)
    destino = Column(String(150), nullable=True)
    expediente = Column(String(50), nullable=True)
    informe = Column(String(50), nullable=True)
    localidad_id = Column(Integer, ForeignKey("localidades.id"), nullable=True)
    acto_id = Column(Integer, ForeignKey("tipo_acto.id"), nullable=True) 
    norma = Column(String(50), nullable=True)

    # Relación ORM
    novedad = relationship("Novedad", back_populates="comodato")
    tipo_acto = relationship("TipoActo")
    localidad = relationship("Localidad")