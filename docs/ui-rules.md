# UI Rules

## Generales

- Jerarquía visual agresiva — el ojo tiene que saber adónde ir
- Whitespace generoso — nunca cramped
- Menos elementos, mejor composición
- Cada pantalla tiene que sentirse premium
- Sin paredes de texto
- Preferir cards sobre tablas
- Interfaces calmadas y mínimas

## Interacciones

- Hover state obligatorio en todo elemento clickeable
- Transiciones suaves (`duration-150` o `duration-200`)
- Focus states para accesibilidad
- Estados de carga en acciones asíncronas

## Responsive

- Mobile-first
- Layout adapta con `md:` breakpoint principalmente
- Sidebar colapsa en mobile

## Feedback visual

- Badges de color para estados (verde/naranja/rojo)
- Empty states con ícono + mensaje, nunca una lista vacía sin contexto
- Confirmación visual tras guardar (spinner en botón)

## Específico del dominio

- Patentes siempre con estilo `plate` (fuente monospace, mayúsculas)
- Fechas en español con formato `dd-MM-yyyy` o `d 'de' MMMM 'de' yyyy`
- Importes con `formatCurrency()` — nunca números crudos
- Kilometraje con `formatMileage()` — con separador de miles y unidad
