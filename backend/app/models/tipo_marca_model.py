from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class TipoMarca(Base):
    __tablename__ = "tipo_marca"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), unique=True, nullable=False)

    # Relación (uno a muchos)
    modelos = relationship("TipoModelo", back_populates="marca", cascade="all, delete-orphan")

    # Relación inversa
    vehiculos = relationship("Vehiculo", back_populates="tipo_marca")