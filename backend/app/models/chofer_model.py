from sqlalchemy import Column, Integer, String, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from ..core.database import Base

class Chofer(Base):
    __tablename__ = "choferes"

    id = Column(Integer, primary_key=True)
    tipo_documento_id = Column(Integer, ForeignKey("tipo_documento.id"), nullable=True)
    documento = Column(String(20), nullable=True)
    nombre = Column(String(150), nullable=False)
    cargo = Column(Integer, nullable=True)
    licencia = Column(String(50), nullable=True)
    dependencia_id = Column(BigInteger, nullable=True)
    domicilio = Column(String(255), nullable=True)
    localidad_id = Column(Integer, ForeignKey("localidades.id"), nullable=True)
    telefono = Column(String(50), nullable=True)   
    tipo_situacion_chofer_id = Column(Integer, ForeignKey("tipo_situacion_chofer.id"), nullable=True)
    observacion = Column(String(255), nullable=True)
    clase = Column(Integer, nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    licencia_vto = Column(Date, nullable=True)

    # Relaciones
    tipo_documento = relationship("TipoDocumento")   
    localidad = relationship("Localidad")    
    tipo_situacion_chofer = relationship("TipoSituacionChofer")