## Proyecto FlotaAuto

API REST desarrollada con **FastAPI**, conectada a una base de datos **PostgreSQL**, utilizando:
**SQLAlchemy** como ORM.
**Alembic** para migraciones.  
**Pydantic** para validaciones.

## ⚙️ Requisitos

- Python 3.12+
- PostgreSQL 14+ (o Docker)
- pipenv o virtualenv (recomendado)
- Alembic

## 📦 Instalación y ▶️ Ejecución del servidor

Copiar, completar y renombrar `.env.example` a `.env` dentro de `/backend`.

```bash
# 1. Clonar el repositorio
git clone https://github.com/sebaamerio/FlotaAuto.git
cd okauto-back/backend

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecución del servidor
uvicorn app.main:app --reload

# Swagger UI
http://127.0.0.1:8000/docs
```

## 🗄️ Base de datos

### Levantar PostgreSQL con Docker (recomendado)

No es necesario crear la base de datos manualmente. Docker la crea automáticamente
con el nombre, usuario y contraseña definidos en `compose-postgresql.yml`.

```bash
# Desde la raíz del proyecto (okauto-back/)
docker compose -f compose-postgresql.yml up -d
```

### Crear las tablas con Alembic

Una vez que PostgreSQL está corriendo, aplicar las migraciones desde `/backend`:

```bash
# Dentro del entorno virtual, desde okauto-back/backend/
alembic upgrade head
```

Esto crea todas las tablas en la base de datos. No requiere ningún paso previo adicional.

### Importar datos iniciales

Luego de crear las tablas, importar los datos desde el script ubicado en la raíz del proyecto:

```bash
# Desde la raíz del proyecto (okauto-back/)
psql -U app_user -d automotores -f BD_automotores_pg.sql
```

Con Docker, copiar el archivo al contenedor y ejecutarlo dentro:

```bash
docker cp BD_automotores_pg.sql okauto_db:/tmp/import.sql
docker exec okauto_db psql -U app_user -d automotores -f /tmp/import.sql
```

El script contiene todos los INSERT de la base de datos y resetea las secuencias
automáticamente al final. Solo ejecutarlo una vez sobre una base vacía.

### Verificar el estado de las migraciones

```bash
alembic current   # revisión aplicada actualmente
alembic history   # historial de migraciones
```

### Sin Docker (PostgreSQL local)

Si tenés PostgreSQL instalado localmente, crear la base de datos manualmente antes
de correr las migraciones:

```sql
CREATE DATABASE automotores;
CREATE USER app_user WITH PASSWORD 'secret123';
GRANT ALL PRIVILEGES ON DATABASE automotores TO app_user;
```

Luego ajustar las variables en `.env` y ejecutar `alembic upgrade head`.
