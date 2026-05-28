import os
import logging
import traceback
from logging.handlers import TimedRotatingFileHandler
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# =========================
# CONFIGURACIÓN DEL LOGGER
# =========================
# 📁 Ruta al archivo de log 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "..", "logs", "app_errors.log")

# ⚙️ Configurar logger
logger = logging.getLogger("app.error_handler")
logger.setLevel(logging.ERROR)

# 🔁 Rotación diaria, conserva los últimos 7 días
handler = TimedRotatingFileHandler(
    LOG_FILE, when="midnight", interval=1, backupCount=7, encoding="utf-8"
)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


# =========================
# MIDDLEWARE GLOBAL (FALLBACK)
# =========================
class GlobalErrorMiddleware(BaseHTTPMiddleware):
    """
    Captura cualquier error no controlado y devuelve una respuesta genérica.
    Mantiene la app funcionando y evita que se caiga el servidor.
    """

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as exc:
            error_trace = traceback.format_exc()
            logger.error(f"💥 Error inesperado en {request.url}:\n{error_trace}")

            return JSONResponse(
                status_code=500,
                content={
                    "status": "error",
                    "type": "unexpected_error",
                    "message": "Ocurrió un error interno. Por favor, intente más tarde o contacte al soporte.",
                },
            )


# =========================
# HANDLERS ESPECÍFICOS
# =========================

def http_exception_handler(request: Request, exc: HTTPException):
    """
    Maneja errores HTTP esperados (404, 401, etc.)
    """
    logger.warning(f"⚠️ HTTPException {exc.status_code}: {exc.detail} - {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "type": "http_exception",
            "message": exc.detail or "Error en la solicitud.",
        },
    )


def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    """
    Maneja errores generales de SQLAlchemy (errores de conexión, consultas, etc.)
    """
    logger.error(f"💾 Error SQLAlchemy: {exc} - {request.url}")
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "type": "database_error",
            "message": "Error al acceder a la base de datos. Intente nuevamente más tarde.",
        },
    )


def integrity_error_handler(request: Request, exc: IntegrityError):
    """
    Maneja violaciones de restricciones de integridad (duplicados, claves foráneas, etc.)
    """
    logger.error(f"🔐 Violación de integridad BD: {exc} - {request.url}")
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "type": "database_integrity",
            "message": "La operación no se pudo completar: datos duplicados o dependencias no válidas.",
        },
    )


def validation_error_handler(request: Request, exc: ValueError):
    """
    Maneja errores de validación manual (por ejemplo, en servicios o lógica de negocio)
    """
    logger.warning(f"⚙️ Error de validación: {exc} - {request.url}")
    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "type": "validation_error",
            "message": str(exc) or "Los datos proporcionados no son válidos.",
        },
    )


# =========================
# REGISTRO CENTRAL
# =========================
def setup_exception_handlers(app: FastAPI):
    """
    Registra todos los manejadores y middleware global.
    """
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
    app.add_exception_handler(IntegrityError, integrity_error_handler)
    app.add_exception_handler(ValueError, validation_error_handler)
    app.add_middleware(GlobalErrorMiddleware)
