# Pages

Todas las páginas usan `AppShell` (sidebar + topbar) como layout base.
Ruta base: `src/app/` en el frontend.

## Dashboard (`/dashboard`)

- Resumen general de la flota
- Stats grid: vehículos activos, en reparación, fuera de servicio
- Gráfico de gastos (combustible vs reparaciones, últimos 6 meses)
- Estado de la flota (FleetStatusCard)
- Alertas de reparaciones próximas (ReparacionAlerts)
- Actividad reciente (RecentActivity)
- Fecha actual en español

## Vehículos (`/vehiculos`)

- Grid de cards de vehículos
- Filtros por estado y tipo de combustible
- Buscador por texto
- Línea de color en card según estado: verde (activo), naranja (en reparación), rojo (VTV/seguro vencido)
- Badge específico si VTV o seguro está vencido
- Modal para agregar/editar vehículo

## Detalle de vehículo (`/vehiculos/[id]`)

- Header con marca, modelo, patente, estado
- Quick stats: kilometraje, costo total reparaciones, combustible, antigüedad
- Tabs:
  - **Resumen**: especificaciones técnicas, conductor asignado, estado de documentos
  - **Reparaciones**: lista con mismo diseño que página de reparaciones, botón agregar
  - **Documentos**: listado con estado de vencimiento
  - **Combustible**: historial de cargas
- Modal editar vehículo
- Modal agregar/editar reparación

## Reparaciones (`/reparacion`)

- Stats: En Reparacion / Reparadas / Total Gastado
- Tabs: **En Reparacion** | **Reparadas**
- Cards con: tipo, patente + vehículo, fechas ingreso/entrega, estado, costo
- Estado automático: entrega pasada → Reparado (verde), entrega futura o sin fecha → En Reparacion (naranja)
- Edición inline con modal

## Conductores (`/drivers`)

- Cards por conductor con foto/iniciales, estado, licencia
- Información de contacto y vehículo asignado

## Documentos (`/documents`)

- Documentos agrupados por estado de vencimiento
- Filtros: todos / por vencer / vencidos

## Estadísticas (`/analytics`)

- Gráficos de consumo de combustible
- Distribución de tipos de reparación
- Costos por período
- KPIs generales de la flota

## Configuración (`/settings`)

- Preferencias del sistema
- Notificaciones
- Datos de la organización
