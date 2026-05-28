from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class Provincia(Base):
    __tablename__ = "provincias"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(50), unique=True, nullable=False)

    # Relación con Localidad (uno a muchos)
    localidades = relationship("Localidad", back_populates="provincia", cascade="all, delete-orphan")