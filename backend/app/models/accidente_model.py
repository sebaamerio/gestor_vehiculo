from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Accidente(Base):
    __tablename__ = "accidentes"

    id = Column(Integer, primary_key=True, index=True)
    novedad_id = Column(Integer, ForeignKey("novedades.id"), nullable=False, unique=True) 
    fecha = Column(Date, nullable=False)
    expediente = Column(String(50), nullable=True)
    informe = Column(String(50), nullable=True)
    acto_id = Column(Integer, ForeignKey("tipo_acto.id"), nullable=True) 
    norma = Column(String(50), nullable=True)
    chofer_id = Column(Integer, ForeignKey("choferes.id"), nullable=True)
    localidad_id = Column(Integer, ForeignKey("localidades.id"), nullable=True)
    fecha_inicio_sumario = Column(Date, nullable=True)
    fecha_fin_sumario = Column(Date, nullable=True)
    lugar = Column(String(100), nullable=True)

    # Relación ORM
    novedad = relationship("Novedad", back_populates="accidente")
    tipo_acto = relationship("TipoActo") 
    chofer = relationship("Chofer")
    localidad = relationship("Localidad")