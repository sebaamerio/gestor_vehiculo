'use client'

import { motion } from 'framer-motion'
import { AlertTriangle, Clock, Shield, Wrench, ChevronRight } from 'lucide-react'
import Link from 'next/link'
import { cn, formatDate } from '@/lib/utils'
import type { Alert } from '@/lib/types'
import { MOCK_VEHICLES } from '@/lib/data'

interface MaintenanceAlertsProps {
  alerts: Alert[]
}

const ALERT_CONFIG = {
  critical: {
    icon: AlertTriangle,
    bg: 'bg-fleet-danger-bg',
    border: 'border-fleet-danger-border',
    iconColor: 'text-fleet-danger',
    dot: 'bg-fleet-danger',
  },
  warning: {
    icon: Clock,
    bg: 'bg-fleet-maintenance-bg',
    border: 'border-fleet-maintenance-border',
    iconColor: 'text-fleet-maintenance',
    dot: 'bg-fleet-maintenance',
  },
  info: {
    icon: Wrench,
    bg: 'bg-accent/10',
    border: 'border-accent/20',
    iconColor: 'text-accent-light',
    dot: 'bg-accent',
  },
}

export function MaintenanceAlerts({ alerts }: MaintenanceAlertsProps) {
  return (
    <div className="bg-surface rounded-2xl border border-subtle shadow-card p-6 flex flex-col h-full">
      <div className="flex items-center justify-between mb-5">
        <div>
          <h3 className="text-[15px] font-semibold text-text-primary">Alertas</h3>
          <p className="text-[12px] text-text-muted mt-0.5">{alerts.length} alertas activas</p>
        </div>
        <Link
          href="/maintenance"
          className="flex items-center gap-1 text-[12px] text-accent-light hover:text-accent transition-colors"
        >
          Ver todas <ChevronRight className="w-3 h-3" />
        </Link>
      </div>

      <div className="space-y-2 flex-1">
        {alerts.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-8 text-center">
            <Shield className="w-8 h-8 text-fleet-active mb-2 opacity-60" />
            <p className="text-[13px] text-text-muted">Todo en orden — sin alertas activas</p>
          </div>
        ) : (
          alerts.map((alert, i) => {
            const config = ALERT_CONFIG[alert.severity]
            const AlertIcon = config.icon
            const vehicle = MOCK_VEHICLES.find((v) => v.id === alert.vehicleId)

            return (
              <motion.div
                key={alert.id}
                initial={{ opacity: 0, x: -8 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: i * 0.05 }}
              >
                <Link
                  href={`/vehicles/${alert.vehicleId}`}
                  className={cn(
                    'flex items-start gap-3 p-3 rounded-xl border transition-all',
                    'hover:brightness-110 cursor-pointer',
                    config.bg,
                    config.border
                  )}
                >
                  <div className={cn('w-7 h-7 rounded-lg flex items-center justify-center flex-shrink-0 mt-0.5', config.bg)}>
                    <AlertIcon className={cn('w-3.5 h-3.5', config.iconColor)} />
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between gap-2">
                      <span className="text-[12px] font-semibold text-text-primary truncate">
                        {vehicle ? `${vehicle.brand} ${vehicle.model}` : 'Vehicle'}
                      </span>
                      {alert.daysUntil !== undefined && (
                        <span className={cn('text-[11px] font-medium flex-shrink-0', config.iconColor)}>
                          {alert.daysUntil < 0
                            ? `${Math.abs(alert.daysUntil)}d vencido`
                            : alert.daysUntil === 0
                            ? 'Hoy'
                            : `${alert.daysUntil}d restantes`}
                        </span>
                      )}
                    </div>
                    <p className="text-[12px] text-text-muted mt-0.5 leading-snug">{alert.message}</p>
                  </div>
                </Link>
              </motion.div>
            )
          })
        )}
      </div>
    </div>
  )
}
