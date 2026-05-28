from sqlalchemy import Column, Integer, String, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from ..core.database import Base

class Donacion(Base):
    __tablename__ = "donaciones"

    id = Column(Integer, primary_key=True, index=True)
    novedad_id = Column(Integer, ForeignKey("novedades.id"), nullable=False, unique=True) 
    fecha = Column(Date, nullable=False)
    expediente = Column(String(50), nullable=True)
    informe = Column(String(50), nullable=True)
    acto_id = Column(Integer, ForeignKey("tipo_acto.id"), nullable=True) 
    norma = Column(String(50), nullable=True)     
    destino = Column(String(150), nullable=True)
    localidad_id = Column(Integer, ForeignKey("localidades.id"), nullable=True)
    fecha_resolucion = Column(Date, nullable=True)    
    fecha_entrega = Column(Date, nullable=True)
    fecha_formulario = Column(Date, nullable=True)    
    fecha_finalizado = Column(Date, nullable=True)
    dependencia_anterior_id =Column(Integer, nullable=True) 
    dependencia_anterior_descripcion =Column(String(100), nullable=True) 

    # Relación ORM
    novedad = relationship("Novedad", back_populates="donacion")
    tipo_acto = relationship("TipoActo")
    localidad = relationship("Localidad")