import { cn } from '@/lib/utils'
import type { VehicleStatus, FuelType } from '@/lib/types'
import { getStatusLabel, getFuelTypeLabel } from '@/lib/utils'
import { Zap, Fuel, Droplets, Leaf } from 'lucide-react'

interface StatusBadgeProps {
  status: VehicleStatus
  size?: 'sm' | 'md'
  dot?: boolean
}

const STATUS_CONFIG: Record<
  VehicleStatus,
  { label: string; bg: string; text: string; border: string; dot: string }
> = {
  active: {
    label: 'Activo',
    bg: 'bg-fleet-active-bg',
    text: 'text-fleet-active',
    border: 'border-fleet-active-border',
    dot: 'bg-fleet-active',
  },
  maintenance: {
    label: 'En Reparacion',
    bg: 'bg-fleet-maintenance-bg',
    text: 'text-fleet-maintenance',
    border: 'border-fleet-maintenance-border',
    dot: 'bg-fleet-maintenance',
  },
  inactive: {
    label: 'Inactivo',
    bg: 'bg-fleet-inactive-bg',
    text: 'text-fleet-inactive',
    border: 'border-fleet-inactive-border',
    dot: 'bg-fleet-inactive',
  },
  out_of_service: {
    label: 'Fuera de Servicio',
    bg: 'bg-fleet-danger-bg',
    text: 'text-fleet-danger',
    border: 'border-fleet-danger-border',
    dot: 'bg-fleet-danger',
  },
}

export function StatusBadge({ status, size = 'md', dot = true }: StatusBadgeProps) {
  const config = STATUS_CONFIG[status]

  return (
    <span
      className={cn(
        'inline-flex items-center gap-1.5 rounded-full border font-medium',
        config.bg,
        config.text,
        config.border,
        size === 'sm' ? 'px-2 py-0.5 text-[11px]' : 'px-2.5 py-1 text-[12px]'
      )}
    >
      {dot && (
        <span
          className={cn(
            'rounded-full flex-shrink-0',
            config.dot,
            status === 'active' ? 'status-pulse' : '',
            size === 'sm' ? 'w-1.5 h-1.5' : 'w-2 h-2'
          )}
        />
      )}
      {config.label}
    </span>
  )
}

interface FuelBadgeProps {
  fuelType: FuelType
  size?: 'sm' | 'md'
}

const FUEL_ICONS: Record<FuelType, React.ElementType> = {
  gasoline: Fuel,
  diesel: Droplets,
  electric: Zap,
  hybrid: Leaf,
  cng: Droplets,
}

export function FuelBadge({ fuelType, size = 'md' }: FuelBadgeProps) {
  const Icon = FUEL_ICONS[fuelType]

  return (
    <span
      className={cn(
        'inline-flex items-center gap-1.5 rounded-full border font-medium bg-subtle text-text-muted border-subtle',
        size === 'sm' ? 'px-2 py-0.5 text-[11px]' : 'px-2.5 py-1 text-[12px]'
      )}
    >
      <Icon className={size === 'sm' ? 'w-2.5 h-2.5' : 'w-3 h-3'} />
      {getFuelTypeLabel(fuelType)}
    </span>
  )
}
