from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Date, DateTime, func, SMALLINT
from sqlalchemy.orm import relationship
from ..core.database import Base

class Vtv(Base):
    __tablename__ = "vtv"

    id = Column(BigInteger, primary_key=True, index=True)
    fecha_solicitud = Column(Date, nullable=True)
    fecha_realizada = Column(Date, nullable=True)
    fecha_vto = Column(Date, nullable=True)
    zona = Column(SMALLINT, nullable=True)    
    oblea = Column(String(50), nullable=True)
    observaciones = Column(String(100), nullable=True)
    vtv_certificado_url = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    update_user = Column(String(100), nullable=True)

    # relaciones
    vehiculo_id = Column(BigInteger, ForeignKey("vehiculos.id"), nullable=False)
    tipo_vtvResultado_id = Column(Integer, ForeignKey("tipo_vtv_resultado.id"), nullable=True)

    # Relación ORM
    vehiculo = relationship("Vehiculo", back_populates="vtvs", lazy="joined")
    tipo_vtvResultado = relationship("TipoVtvResultado", back_populates="vtvs", lazy="joined")