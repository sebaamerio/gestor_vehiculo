from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class TipoCondicion(Base):
    __tablename__ = "tipo_condicion"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), unique=True, nullable=False)
    icon = Column(String(50), unique=True, nullable=True)

    # Relación inversa
    vehiculos = relationship("Vehiculo", back_populates="tipo_condicion")