# Stack

## Estructura del proyecto

```
gestor_vehiculo/
├── front/      # Next.js frontend
├── backend/    # FastAPI backend
└── docs/       # Documentación
```

## Frontend (`front/`)

- **Next.js 14** (App Router)
- **React 18** + TypeScript
- **Tailwind CSS** — estilos
- **shadcn/ui** — componentes base (Radix UI)
- **Framer Motion** — animaciones
- **Lucide Icons** — iconografía
- **Recharts** — gráficos
- **date-fns** — manejo de fechas con locale `es`
- **next-themes** — soporte dark/light mode

### Reglas frontend

- Usar siempre componentes shadcn antes de crear uno custom
- Solo Tailwind, sin CSS modules ni estilos inline arbitrarios
- Sin Material UI ni Bootstrap
- Tipos TypeScript estrictos, sin `any`
- Componentes en `src/components/`, páginas en `src/app/`

## Backend (`backend/`)

- **Python 3.12+**
- **FastAPI** — framework REST API
- **PostgreSQL 14+** — base de datos
- **SQLAlchemy 2.0** — ORM
- **Alembic** — migraciones de base de datos
- **Pydantic v2** — validación de schemas
- **bcrypt** + **python-jose** — autenticación JWT
- **Uvicorn** — servidor ASGI
- **psycopg2-binary** — driver PostgreSQL
- **Sentry SDK** — monitoreo de errores

### Estructura backend

```
backend/
├── app/
│   ├── core/          # config, database, security, deps
│   ├── models/        # modelos SQLAlchemy
│   ├── repositories/  # capa de acceso a datos
│   ├── routers/       # endpoints de la API
│   ├── schemas/       # schemas Pydantic
│   ├── services/      # lógica de negocio
│   └── main.py        # inicialización FastAPI
├── alembic/           # migraciones
├── requirements.txt
├── seed.py
└── .env
```

### Reglas backend

- Arquitectura en capas: router → service → repository → model
- Schemas Pydantic separados para request/response
- Migraciones siempre con Alembic, nunca modificar tablas manualmente
- Variables de entorno en `.env`, nunca hardcodeadas
- Swagger UI disponible en `http://localhost:8000/docs`

## Ejecución local

```bash
# Frontend
cd front && npm run dev        # http://localhost:3000

# Backend
cd backend
uvicorn app.main:app --reload  # http://localhost:8000
```
