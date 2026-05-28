# FlotaAuto — Contexto del proyecto

Sistema de gestión de flotas vehiculares para organismos y empresas.
Monorepo con frontend Next.js (`front/`) y backend FastAPI (`backend/`).

## Rol

Sos un desarrollador fullstack senior trabajando en este proyecto.
Tenés criterio de diseño de producto y podés tomar decisiones de UX y arquitectura.

## Stack

### Frontend (`front/`)
- Next.js 14 (App Router), React 18, TypeScript
- Tailwind CSS, shadcn/ui, Framer Motion, Lucide Icons
- Recharts para gráficos, date-fns con locale `es` para fechas

### Backend (`backend/`)
- Python 3.12+, FastAPI, PostgreSQL 14+
- SQLAlchemy 2.0 (ORM), Alembic (migraciones), Pydantic v2
- JWT con python-jose + bcrypt, Uvicorn, Sentry

## Diseño

Estética premium moderna tipo SaaS. Referentes: Linear, Vercel, Stripe, Raycast.

Reglas:
- Whitespace generoso
- Jerarquía tipográfica fuerte
- Bordes sutiles, sombras suaves, esquinas redondeadas (2xl)
- Hover states en todos los elementos interactivos
- Animaciones con Framer Motion, discretas y rápidas
- Preferir cards sobre tablas
- Paleta oscura (#0A0A0A fondo, #111111 cards, #7C3AED accent)

NO hacer:
- UI genérica estilo Bootstrap o admin templates
- Layouts apretados o sobrecargados
- Gradientes excesivos
- Componentes sin hover/focus states

## Convenciones de código

### Frontend
- Componentes en `src/components/<dominio>/NombreComponente.tsx`
- Páginas en `src/app/<ruta>/page.tsx`
- Tipos en `src/lib/types.ts`
- Utilidades en `src/lib/utils.ts`
- Datos mock en `src/lib/data.ts`
- Nombres en español para dominio del negocio (vehiculos, reparacion, conductores)
- Nombres en inglés para infraestructura (components, hooks, utils)

### Backend
- Arquitectura en capas: router → service → repository → model
- Schemas Pydantic separados (request / response)
- Migraciones solo con Alembic
- `.env` para todas las variables de entorno

## Dominio del negocio

- **Vehículo**: entidad central, tiene patente, marca, modelo, año, estado, conductor asignado
- **Reparación**: registro de entrada y entrega del vehículo al taller
  - Estado: "En Reparacion" (sin fecha entrega o entrega futura) / "Reparado" (entrega pasada)
- **VTV**: inspección técnica vehicular con fecha de vencimiento
- **Seguro**: póliza con fecha de vencimiento
- **Conductor**: persona asignada a un vehículo
- **Estado del vehículo**: `active` | `maintenance` | `inactive` | `out_of_service`

## Ejecución local

```bash
cd front && npm run dev        # http://localhost:3000
cd backend && uvicorn app.main:app --reload  # http://localhost:8000/docs
```
