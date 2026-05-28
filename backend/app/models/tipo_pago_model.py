from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..core.database import Base

class TipoPago(Base):
    __tablename__ = "tipo_pago"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(50), unique=True, nullable=False)