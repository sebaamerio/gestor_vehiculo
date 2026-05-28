from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class Taller(Base):
    __tablename__ = "talleres"

    id = Column(Integer, primary_key=True, index=True)
    taller_desc = Column(String(150), unique=True, nullable=False)
    domicilio = Column(String(100), nullable=True)
    cuit = Column(String(20), nullable=True)
    ing_brutos = Column(String(20), nullable=True)
    observaciones = Column(String(100), nullable=True)

    # Relación inversa
    reparaciones = relationship("Reparacion", back_populates="talleres")    