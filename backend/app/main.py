from fastapi import FastAPI
from app.core.config import settings
from .core.error_handler import setup_exception_handlers
from fastapi.middleware.cors import CORSMiddleware
from .routers import (
    auth_router,
    tipo_vehiculo_router,
    vehiculo_router,
    localidad_router,
    provincia_router,
    tipo_acto_router,
    tipo_carroceria_router,
    tipo_condicion_router,
    tipo_motor_router,
    tipo_novedad_router,
    tipo_situacion_router,
    tipo_vtvResultado_router,
    tipo_marca_router,
    tipo_model_router,
    tipo_documento_router,
    tipo_aptitud_router,
    tipo_cabina_router,
    tipo_traccion_router,
    tipo_pago_router,
    dependencia_router,
    vtv_router,
    baja_router,
    cambio_motor_router,
    accidente_router,
    donacion_router,
    robo_router,
    transferencia_router,
    novedad_router,
    chofer_router,
    taller_router,
    reparacion_router,
    vehiculo_dependencia_router,
    catalogos_router,
    cambio_chasis_router,
    comodato_router,
    infraccion_router
)

# 🚨 PASO CRUCIAL 1: Importar los modelos que tienen referencias circulares
# Esto fuerza a Python a cargar los módulos de esquema
from app.schemas.reparacion_schema import Reparacion
from app.schemas.vtv_schema import Vtv
from app.schemas.vehiculo_schema import Vehiculo
from app.schemas.tipo_vtvResultado_schema import TipoVtvResultado
from app.schemas.novedad_schema import Novedad
from app.schemas.vehiculo_dependencia_schema import VehiculoDependencia

# 🚨 PASO CRUCIAL 2: Llamar a model_rebuild() inmediatamente para resolver las referencias en cadena
Vtv.model_rebuild()
Reparacion.model_rebuild()
VehiculoDependencia.model_rebuild()
Vehiculo.model_rebuild()
TipoVtvResultado.model_rebuild()
Novedad.model_rebuild()

app = FastAPI(title="OKauto API", debug=settings.DEBUG)

# 🛡️ Configurar Middleware para Proxy (Cloudflare/Nginx)
# Esto permite que FastAPI confíe en los headers 'X-Forwarded-Proto' y genere URLs https correctamente.
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts=["*"])

# ⚙️ Configurar CORS antes de registrar los routers
origins = settings.cors_origins_list

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar el manejador global de errores
setup_exception_handlers(app)

@app.get("/info")
def info():
    return {"environment": settings.ENV}

# Registrar los routers
app.include_router(auth_router.router)
app.include_router(tipo_vehiculo_router.router)
app.include_router(tipo_acto_router.router)
app.include_router(tipo_carroceria_router.router)
app.include_router(tipo_condicion_router.router)
app.include_router(tipo_motor_router.router)
app.include_router(tipo_novedad_router.router)
app.include_router(tipo_situacion_router.router)
app.include_router(tipo_vtvResultado_router.router)
app.include_router(tipo_marca_router.router)
app.include_router(tipo_model_router.router)
app.include_router(tipo_documento_router.router)
app.include_router(tipo_aptitud_router.router)
app.include_router(tipo_cabina_router.router)
app.include_router(tipo_traccion_router.router)
app.include_router(tipo_pago_router.router)
app.include_router(dependencia_router.router)

# Es mejor registrar los routers VTV/Vehículo antes de que FastAPI intente construir el esquema.
app.include_router(vtv_router.router)
app.include_router(reparacion_router.router)
app.include_router(baja_router.router)
app.include_router(cambio_motor_router.router)
app.include_router(accidente_router.router)
app.include_router(donacion_router.router)
app.include_router(robo_router.router)
app.include_router(transferencia_router.router)
app.include_router(cambio_chasis_router.router)
app.include_router(comodato_router.router)
app.include_router(infraccion_router.router)

app.include_router(novedad_router.router)
app.include_router(vehiculo_dependencia_router.router)
app.include_router(vehiculo_router.router)

app.include_router(localidad_router.router)
app.include_router(provincia_router.router)

app.include_router(chofer_router.router)
app.include_router(taller_router.router)
app.include_router(catalogos_router.router)