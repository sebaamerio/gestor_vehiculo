from sqlalchemy import Column, Integer, BigInteger, String, Date, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from ..core.database import Base # Asume que Base está aquí

class Novedad(Base):
    __tablename__ = "novedades"

    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(BigInteger, ForeignKey("vehiculos.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    tipo_novedad_id = Column(Integer, ForeignKey("tipo_novedad.id"), nullable=False)
    observaciones = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    update_user = Column(String(100), nullable=True)

    # Relación ORM (asume que Vehiculo tiene back_populates="novedades")
    vehiculo = relationship("Vehiculo", back_populates="novedades", lazy="joined")
    tipo_novedad = relationship("TipoNovedad", back_populates="novedades", lazy="joined")

    # Relaciones de las novedades específicas (usando cascade para limpieza)
    baja = relationship("Baja", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
    cambio_motor = relationship("CambioMotor", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
    accidente = relationship("Accidente", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
    donacion = relationship("Donacion", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
    robo = relationship("Robo", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
    transferencia = relationship("Transferencia", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
    cambio_chasis = relationship("CambioChasis", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
    comodato = relationship("Comodato", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
    infraccion = relationship("Infraccion", back_populates="novedad", uselist=False, cascade="all, delete-orphan")
