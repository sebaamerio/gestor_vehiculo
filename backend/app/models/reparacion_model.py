from sqlalchemy import Column, Integer, BigInteger, DECIMAL, String, ForeignKey, Date, DateTime, func
from sqlalchemy.orm import relationship
from ..core.database import Base

class Reparacion(Base):
    __tablename__ = "reparaciones"

    id = Column(BigInteger, primary_key=True, index=True)
    fecha = Column(Date, nullable=True)
    factura = Column(String(50), nullable=True)
    fecha_pres = Column(Date, nullable=True)
    detalle = Column(String(255), nullable=True)
    importe = Column(DECIMAL(12, 2), nullable=True)
    caract = Column(String(50), nullable=True)
    expediente= Column(String(50), nullable=True)
    anioexp= Column(Integer, nullable=True) 
    alcance= Column(String(50), nullable=True)
    nrocuerpo= Column(String(50), nullable=True)
    km= Column(Integer, nullable=True)
    update_user = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # relaciones
    vehiculo_id = Column(BigInteger, ForeignKey("vehiculos.id"), nullable=False)
    tipo_reparacion_estado_id = Column(Integer, ForeignKey("tipo_reparacion_estado.id"), nullable=True)
    taller_id = Column(Integer, ForeignKey("talleres.id"), nullable=True)

    # Relación ORM
    tipo_reparacion_estado = relationship("TipoReparacionEstado", back_populates="reparaciones")
    talleres = relationship("Taller", back_populates="reparaciones")
    vehiculo = relationship("Vehiculo", back_populates="reparaciones") 
