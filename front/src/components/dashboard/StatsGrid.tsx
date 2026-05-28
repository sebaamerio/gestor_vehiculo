'use client'

import { motion } from 'framer-motion'
import { Car, CheckCircle2, Wrench, AlertTriangle, Users, TrendingUp, TrendingDown } from 'lucide-react'
import { cn, formatCurrency, formatMileage } from '@/lib/utils'

interface StatCard {
  label: string
  value: string | number
  subValue?: string
  icon: React.ElementType
  iconBg: string
  iconColor: string
  trend?: number
  trendLabel?: string
  highlight?: boolean
}

interface StatsGridProps {
  stats: ReturnType<typeof import('@/lib/data').getDashboardStats>
}

export function StatsGrid({ stats }: StatsGridProps) {
  const cards: StatCard[] = [
    {
      label: 'Flota Total',
      value: stats.totalVehicles,
      subValue: `${stats.activeVehicles} activos`,
      icon: Car,
      iconBg: 'bg-accent/10',
      iconColor: 'text-accent-light',
      trend: 2,
      trendLabel: 'vs mes anterior',
    },
    {
      label: 'Operativos',
      value: stats.activeVehicles,
      subValue: `${Math.round((stats.activeVehicles / stats.totalVehicles) * 100)}% de la flota`,
      icon: CheckCircle2,
      iconBg: 'bg-fleet-active-bg',
      iconColor: 'text-fleet-active',
      highlight: true,
    },
    {
      label: 'En Reparacion',
      value: stats.enReparacion + stats.outOfService,
      subValue: `${stats.enReparacion} servicio · ${stats.outOfService} fuera de linea`,
      icon: Wrench,
      iconBg: 'bg-fleet-maintenance-bg',
      iconColor: 'text-fleet-maintenance',
    },
    {
      label: 'Combustible Mensual',
      value: formatCurrency(stats.monthlyFuelCost),
      subValue: 'Abril 2025',
      icon: TrendingUp,
      iconBg: 'bg-blue-500/10',
      iconColor: 'text-blue-400',
      trend: -4,
      trendLabel: 'vs Marzo',
    },
  ]

  return (
    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
      {cards.map((card, i) => (
        <StatCard key={card.label} card={card} index={i} />
      ))}
    </div>
  )
}

function StatCard({ card, index }: { card: StatCard; index: number }) {
  const Icon = card.icon
  const hasTrend = card.trend !== undefined
  const isPositive = (card.trend ?? 0) >= 0

  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3, delay: index * 0.06, ease: [0.4, 0, 0.2, 1] }}
      className={cn(
        'group relative rounded-2xl border p-5 overflow-hidden cursor-default',
        'transition-all duration-200 hover:border-subtle-hover hover:-translate-y-0.5',
        card.highlight
          ? 'bg-fleet-active-bg/30 border-fleet-active-border/50 hover:border-fleet-active-border'
          : 'bg-surface border-subtle hover:bg-surface-elevated shadow-card hover:shadow-card-hover'
      )}
    >
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-card opacity-50" />

      <div className="relative">
        {/* Icon + Trend */}
        <div className="flex items-start justify-between mb-4">
          <div className={cn('w-9 h-9 rounded-xl flex items-center justify-center', card.iconBg)}>
            <Icon className={cn('w-4.5 h-4.5', card.iconColor)} />
          </div>

          {hasTrend && (
            <span
              className={cn(
                'flex items-center gap-0.5 text-[11px] font-medium px-1.5 py-0.5 rounded-md',
                isPositive
                  ? 'text-fleet-active bg-fleet-active-bg'
                  : 'text-fleet-danger bg-fleet-danger-bg'
              )}
            >
              {isPositive ? <TrendingUp className="w-2.5 h-2.5" /> : <TrendingDown className="w-2.5 h-2.5" />}
              {Math.abs(card.trend!)}%
            </span>
          )}
        </div>

        {/* Value */}
        <div className="space-y-0.5">
          <div className={cn('font-bold tracking-tight', typeof card.value === 'string' ? 'text-2xl' : 'text-3xl')}>
            {card.value}
          </div>
          <div className="text-[12px] font-medium text-text-muted">{card.label}</div>
        </div>

        {/* Sub value */}
        {card.subValue && (
          <div className="mt-3 pt-3 border-t border-subtle">
            <span className="text-[12px] text-text-muted">{card.subValue}</span>
            {hasTrend && card.trendLabel && (
              <span className="text-[11px] text-text-disabled ml-1.5">{card.trendLabel}</span>
            )}
          </div>
        )}
      </div>
    </motion.div>
  )
}
