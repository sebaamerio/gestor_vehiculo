from sqlalchemy import Column, Integer, BigInteger, SmallInteger, String, Boolean, Date, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from ..core.database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    # campos
    id = Column(BigInteger, primary_key=True, index=True)
    registro_nro = Column(Integer, nullable=True, unique=True)
    registro_marca = Column(Boolean, nullable=False, default=True)
    fecha_titulo = Column(Date, nullable=True)
    anio = Column(Integer, nullable=True)
    plazas = Column(Integer, nullable=True)
    carga = Column(Integer, nullable=True)
    ejes = Column(SmallInteger, nullable=True)
    motor_marca = Column(String(80), nullable=True)
    motor_nro = Column(String(80), nullable=False)
    dominio = Column(String(8), nullable=True, unique=True)
    dominio_anterior = Column(String(8), nullable=True)   
    chasis_marca = Column(String(80), nullable=True)
    chasis_nro = Column(String(40), nullable=False)
    fechaVtv = Column(Date, nullable=True)
    observaciones = Column(String(150), nullable=True)
    tipo_dominio  = Column(String(1), nullable=True)
    guarda = Column(String(30), nullable=True)
    titulo_certificado_url = Column(String(255), nullable=True)    
    cedula_certificado_url = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    update_user = Column(String(100), nullable=True)
    origen = Column(String(60), nullable=True)
    empresa = Column(String(60), nullable=True)
    ri_anterior = Column(Integer, nullable=True, unique=True)

    # relaciones
    marca_id = Column(Integer, ForeignKey("tipo_marca.id"), nullable=True)
    modelo_id = Column(Integer, ForeignKey("tipo_modelo.id"), nullable=True)
    tipo_vehiculo_id = Column(Integer, ForeignKey("tipo_vehiculo.id"), nullable=True)
    carroceria_id = Column(Integer, ForeignKey("tipo_carroceria.id"), nullable=True)
    tipo_motor_id = Column(Integer, ForeignKey("tipo_motor.id"), nullable=True)
    condicion_id  = Column(Integer, ForeignKey("tipo_condicion.id"), nullable=True)
    situacion_id = Column(Integer, ForeignKey("tipo_situacion.id"), nullable=True)
    tipo_aptitud_id = Column(Integer, ForeignKey("tipo_aptitud.id"), nullable=True)
    tipo_cabina_id = Column(Integer, ForeignKey("tipo_cabina.id"), nullable=True)
    tipo_traccion_id = Column(Integer, ForeignKey("tipo_traccion.id"), nullable=True)

    # Relación ORM
    tipo_marca = relationship("TipoMarca", back_populates="vehiculos", lazy="joined")
    tipo_modelo = relationship("TipoModelo", back_populates="vehiculos", lazy="joined")
    tipo_vehiculo = relationship("TipoVehiculo", back_populates="vehiculos", lazy="joined")
    tipo_carroceria = relationship("TipoCarroceria", back_populates="vehiculos", lazy="joined")
    tipo_motor = relationship("TipoMotor", back_populates="vehiculos", lazy="joined")
    tipo_condicion = relationship("TipoCondicion", back_populates="vehiculos", lazy="joined")
    tipo_situacion = relationship("TipoSituacion", back_populates="vehiculos", lazy="joined")
    tipo_aptitud = relationship("TipoAptitud", back_populates="vehiculos", lazy="joined")
    tipo_cabina = relationship("TipoCabina", back_populates="vehiculos", lazy="joined")
    tipo_traccion = relationship("TipoTraccion", back_populates="vehiculos", lazy="joined")

    vtvs = relationship("Vtv", back_populates="vehiculo", cascade="all, delete-orphan")
    novedades = relationship("Novedad", back_populates="vehiculo", cascade="all, delete-orphan")
    reparaciones = relationship("Reparacion", back_populates="vehiculo", cascade="all, delete-orphan")
    vehiculo_dependencias = relationship("VehiculoDependencia", back_populates="vehiculo", cascade="all, delete-orphan")

    @property
    def dependencia(self):
        return next(
            (d for d in self.vehiculo_dependencias if d.activo),
            None
        )