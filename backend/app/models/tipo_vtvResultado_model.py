from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class TipoVtvResultado(Base):
    __tablename__ = "tipo_vtv_resultado"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(100), unique=True, nullable=False)

    # Relación ORM
    vtvs = relationship("Vtv", back_populates="tipo_vtvResultado")