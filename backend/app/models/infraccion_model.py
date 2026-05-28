from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Infraccion(Base):
    __tablename__ = "infracciones"

    id = Column(Integer, primary_key=True, index=True)
    novedad_id = Column(Integer, ForeignKey("novedades.id"), nullable=False, unique=True) 
    fecha = Column(Date, nullable=False)
    chofer_id = Column(Integer, ForeignKey("choferes.id"), nullable=True)
    localidad_id = Column(Integer, ForeignKey("localidades.id"), nullable=True)
    acta = Column(String(80), nullable=True)
    citacion = Column(String(80), nullable=True)
    causa = Column(String(80), nullable=True)
    tipo_pago_id = Column(Integer, ForeignKey("tipo_pago.id"), nullable=True) 

    # Relación ORM
    novedad = relationship("Novedad", back_populates="infraccion")
    chofer = relationship("Chofer")
    localidad = relationship("Localidad")
    tipo_pago = relationship("TipoPago") 
