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
    label: 'Active',
    bg: 'bg-fleet-active-bg',
    text: 'text-fleet-active',
    border: 'border-fleet-active-border',
    dot: 'bg-fleet-active',
  },
  maintenance: {
    label: 'Maintenance',
    bg: 'bg-fleet-maintenance-bg',
    text: 'text-fleet-maintenance',
    border: 'border-fleet-maintenance-border',
    dot: 'bg-fleet-maintenance',
  },
  inactive: {
    label: 'Inactive',
    bg: 'bg-fleet-inactive-bg',
    text: 'text-fleet-inactive',
    border: 'border-fleet-inactive-border',
    dot: 'bg-fleet-inactive',
  },
  out_of_service: {
    label: 'Out of Service',
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

const FUEL_CONFIG: Record<
  FuelType,
  { icon: React.ElementType; bg: string; text: string; border: string }
> = {
  gasoline: {
    icon: Fuel,
    bg: 'bg-orange-500/10',
    text: 'text-orange-400',
    border: 'border-orange-500/20',
  },
  diesel: {
    icon: Droplets,
    bg: 'bg-blue-500/10',
    text: 'text-blue-400',
    border: 'border-blue-500/20',
  },
  electric: {
    icon: Zap,
    bg: 'bg-cyan-500/10',
    text: 'text-cyan-400',
    border: 'border-cyan-500/20',
  },
  hybrid: {
    icon: Leaf,
    bg: 'bg-green-500/10',
    text: 'text-green-400',
    border: 'border-green-500/20',
  },
  cng: {
    icon: Droplets,
    bg: 'bg-purple-500/10',
    text: 'text-purple-400',
    border: 'border-purple-500/20',
  },
}

export function FuelBadge({ fuelType, size = 'md' }: FuelBadgeProps) {
  const config = FUEL_CONFIG[fuelType]
  const Icon = config.icon

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
      <Icon className={size === 'sm' ? 'w-2.5 h-2.5' : 'w-3 h-3'} />
      {getFuelTypeLabel(fuelType)}
    </span>
  )
}
