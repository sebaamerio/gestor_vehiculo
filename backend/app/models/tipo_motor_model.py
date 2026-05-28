from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class TipoMotor(Base):
    __tablename__ = "tipo_motor"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), unique=True, nullable=False)

    # Relación inversa
    vehiculos = relationship("Vehiculo", back_populates="tipo_motor")