# Design System

## Estética

Premium modern SaaS — oscuro, limpio, con foco en jerarquía y espacio.

Referentes: Linear, Vercel, Stripe, Raycast, Lovable.

## Colores

| Token | Valor | Uso |
|-------|-------|-----|
| `--color-base` | `#0A0A0A` | Fondo general |
| `--color-surface` | `#111111` | Cards y paneles |
| `--color-sidebar` | `#0D0D0D` | Sidebar |
| Borders | `rgba(255,255,255,0.08)` | Bordes sutiles |
| Accent | `#7C3AED` | Acción principal |

### Colores semánticos de flota

| Token | Color | Significado |
|-------|-------|-------------|
| `fleet-active` | Verde | Vehículo activo / Reparado |
| `fleet-maintenance` | Naranja/Amber | En reparación / Por vencer |
| `fleet-danger` | Rojo | Vencido / Fuera de servicio |

## Tipografía

- Jerarquía fuerte: headings grandes, labels pequeños
- Tamaños frecuentes: `text-[11px]`, `text-[12px]`, `text-[13px]`, `text-[14px]`, `text-[15px]`
- Peso: `font-medium` para labels, `font-semibold` para datos, `font-bold` para títulos

## Espaciado

- Padding de cards: `p-4` o `p-5`
- Gap entre elementos: `gap-2`, `gap-3`
- Secciones separadas con `mb-6` o `mb-8`
- Whitespace generoso, nunca cramped

## Componentes

- Bordes redondeados: `rounded-xl` (cards), `rounded-2xl` (paneles grandes), `rounded-lg` (botones/badges)
- Sombras: `shadow-card`, `shadow-card-hover` en hover
- Bordes: `border border-subtle` (clase utilitaria)
- Badges de estado: pill con `bg-*-bg`, `text-*`, `border-*-border`

## Íconos

- Librería: Lucide Icons
- Tamaños: `w-3.5 h-3.5` (inline), `w-4 h-4` (botones), `w-8 h-8` (empty states)

## Reglas

- Sin Bootstrap, sin Material UI, sin estilos default de Tailwind sin customizar
- Hover state obligatorio en todo elemento interactivo
- Animaciones con Framer Motion — discretas, máximo 300ms
- Preferir cards sobre tablas
- Priorizar legibilidad sobre densidad
