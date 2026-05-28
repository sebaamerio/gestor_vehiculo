from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Configuración de la aplicación
from app.core.config import settings
from app.core.database import Base

# Importar todos los modelos (debe existir app/models/__init__.py)
import app.models


# Alembic Config object
config = context.config

# Sobrescribir la URL de conexión con la de settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Metadata de los modelos
target_metadata = Base.metadata


# ---------------------------------------------------------
# FILTRO DE OBJETOS PARA EVITAR CAMBIOS FALSOS
# ---------------------------------------------------------
def include_object(object, name, type_, reflected, compare_to):

    # Ignorar índices automáticos
    if type_ == "index":
        return False

    # Ignorar foreign keys generadas/reflejadas por la DB
    if type_ == "foreign_key_constraint" and reflected:
        return False

    # Ignorar unique constraints reflejadas
    if type_ == "unique_constraint" and reflected:
        return False

    return True


# ---------------------------------------------------------
# MIGRACIONES OFFLINE
# ---------------------------------------------------------
def run_migrations_offline() -> None:

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


# ---------------------------------------------------------
# MIGRACIONES ONLINE
# ---------------------------------------------------------
def run_migrations_online() -> None:

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


# ---------------------------------------------------------
# EJECUCIÓN
# ---------------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()