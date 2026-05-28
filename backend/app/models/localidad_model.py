from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class Localidad(Base):
    __tablename__ = "localidades"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(150), unique=False, nullable=False)
    partido_id = Column(String(5), unique=False, nullable=False)
    cod_postal = Column(Integer, default=0, nullable=False)
    provincia_id = Column(String(5), unique=False, nullable=False)

    # 🔹 Clave foránea a Provincia
    provincia_id = Column(Integer, ForeignKey("provincias.id"), nullable=False)

    # Relación inversa con Provincia
    provincia = relationship("Provincia", back_populates="localidades")