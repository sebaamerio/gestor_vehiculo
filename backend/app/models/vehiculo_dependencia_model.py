from sqlalchemy import Column, Integer, BigInteger, String, Date, ForeignKey, DateTime, Boolean, func
from sqlalchemy.orm import relationship
from ..core.database import Base # Asume que Base está aquí

class VehiculoDependencia(Base):
    __tablename__ = "vehiculo_dependencia"

    id = Column(Integer, primary_key=True, index=True)    
    fecha_desde = Column(Date, nullable=False)
    fecha_hasta = Column(Date, nullable=True)    
    dependencia_descripcion =Column(String(100), nullable=True)
    activo = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    update_user = Column(String(60), nullable=True)

    # Relaciones
    vehiculo_id = Column(BigInteger, ForeignKey("vehiculos.id"), nullable=False)
    dependencia_id = Column(BigInteger, ForeignKey("dependencias.id"), nullable=True)
    tipo_tramite_id = Column(Integer, ForeignKey("tipo_tramite_dependencia.id"), nullable=False)


    # Relación ORM
    vehiculo = relationship("Vehiculo", back_populates="vehiculo_dependencias") 
    dependencia = relationship("Dependencia", back_populates="vehiculos")
    tipo_tramite_dependencia = relationship("TipoTramiteDependencia")