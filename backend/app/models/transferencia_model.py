from sqlalchemy import Column, Integer, String, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from ..core.database import Base

class Transferencia(Base):
    __tablename__ = "transferencias"

    id = Column(Integer, primary_key=True, index=True)
    novedad_id = Column(Integer, ForeignKey("novedades.id"), nullable=False, unique=True) 
    fecha = Column(Date, nullable=False)
    expediente = Column(String(50), nullable=True)
    informe = Column(String(50), nullable=True)
    acto_id = Column(Integer, ForeignKey("tipo_acto.id"), nullable=True) 
    norma = Column(String(50), nullable=True)
    dependencia_anterior_id = Column(BigInteger, nullable=True)
    dependencia_anterior_descripcion =Column(String(100), nullable=True)
    dependencia_id = Column(BigInteger, nullable=True)
    dependencia_descripcion =Column(String(100), nullable=True)

    # Relación ORM
    novedad = relationship("Novedad", back_populates="transferencia")
    tipo_acto = relationship("TipoActo")