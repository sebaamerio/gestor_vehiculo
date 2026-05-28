# Animations

## Librería

Framer Motion — única librería de animación del proyecto.

## Patrones usados

### Entrada de listas
```tsx
<motion.div
  initial={{ opacity: 0, y: 6 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ delay: i * 0.04 }}
/>
```

### Entrada de secciones
```tsx
<motion.div
  initial={{ opacity: 0, y: -8 }}
  animate={{ opacity: 1, y: 0 }}
/>
```

### Sidebar (ancho colapsable)
```tsx
<motion.aside
  animate={{ width: collapsed ? 64 : 240 }}
  transition={{ duration: 0.2, ease: [0.4, 0, 0.2, 1] }}
/>
```

### Spinner de carga
```tsx
<motion.div
  animate={{ rotate: 360 }}
  transition={{ duration: 0.8, repeat: Infinity, ease: 'linear' }}
/>
```

### Active indicator en sidebar
```tsx
<motion.div layoutId="sidebar-active" transition={{ type: 'spring', bounce: 0.15 }} />
```

## Reglas

- Duración máxima: 300ms para transiciones de UI, 400ms para springs
- Delays en listas: `i * 0.04` (40ms por item)
- Ease preferido: `[0.4, 0, 0.2, 1]` (Material easing)
- `AnimatePresence` para elementos que entran/salen del DOM
- No animar cosas que el usuario no va a notar
- Nunca bloquear la interacción con animaciones largas
