from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class TipoModelo(Base):
    __tablename__ = "tipo_modelo"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(150), unique=False, nullable=False)

    # 🔹 Clave foránea a Provincia
    marca_id = Column(Integer, ForeignKey("tipo_marca.id"), nullable=False)

    # Relación inversa
    marca = relationship("TipoMarca", back_populates="modelos")
    vehiculos = relationship("Vehiculo", back_populates="tipo_modelo")