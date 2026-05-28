from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from ..core.database import Base

class Dependencia(Base):
    __tablename__ = "dependencias"

    id = Column(BigInteger, primary_key=True, index=True)
    descripcion = Column(String(100), unique=False, nullable=False)   

    # Relación ORM
    vehiculos = relationship("VehiculoDependencia", back_populates="dependencia")