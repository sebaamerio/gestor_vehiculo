'use client'

import { motion } from 'framer-motion'
import { Wrench, CheckCircle2, Clock, AlertCircle } from 'lucide-react'
import Link from 'next/link'
import { cn, formatDate, formatCurrency, formatMileage, getMaintenanceTypeLabel } from '@/lib/utils'
import type { MaintenanceRecord, Vehicle } from '@/lib/types'

interface MaintenanceListProps {
  records: MaintenanceRecord[]
  vehicles: Vehicle[]
  title?: string
  showVehicle?: boolean
}

const STATUS_CONFIG = {
  completed: {
    icon: CheckCircle2,
    bg: 'bg-fleet-active-bg',
    text: 'text-fleet-active',
    label: 'Completado',
  },
  scheduled: {
    icon: Clock,
    bg: 'bg-fleet-maintenance-bg',
    text: 'text-fleet-maintenance',
    label: 'Programado',
  },
  overdue: {
    icon: AlertCircle,
    bg: 'bg-fleet-danger-bg',
    text: 'text-fleet-danger',
    label: 'Vencido',
  },
}

export function MaintenanceList({
  records,
  vehicles,
  title,
  showVehicle = true,
}: MaintenanceListProps) {
  if (records.length === 0) {
    return (
      <div className="bg-surface rounded-2xl border border-subtle p-10 text-center">
        <Wrench className="w-8 h-8 text-text-muted mx-auto mb-3" />
        <p className="text-[14px] font-medium text-text-muted">Sin registros de reparacion</p>
      </div>
    )
  }

  return (
    <div className="space-y-3">
      {title && (
        <h3 className="text-[13px] font-semibold text-text-muted uppercase tracking-wider mb-3">{title}</h3>
      )}
      {records.map((record, i) => {
        const config = STATUS_CONFIG[record.status]
        const StatusIcon = config.icon
        const vehicle = vehicles.find((v) => v.id === record.vehicleId)

        return (
          <motion.div
            key={record.id}
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: i * 0.04 }}
            className="bg-surface rounded-xl border border-subtle p-4 flex items-start gap-4 hover:border-subtle-hover transition-colors"
          >
            <div className={cn('w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0', config.bg)}>
              <StatusIcon className={cn('w-4.5 h-4.5', config.text)} />
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-start justify-between gap-2">
                <div className="min-w-0">
                  <div className="text-[14px] font-semibold text-text-primary">
                    {getMaintenanceTypeLabel(record.type)}
                  </div>
                  <p className="text-[12px] text-text-muted mt-0.5">{record.description}</p>
                </div>
                <div className="flex-shrink-0 text-right">
                  <div className="text-[14px] font-semibold text-text-primary">
                    {record.cost > 0 ? formatCurrency(record.cost) : 'Gratis'}
                  </div>
                  <span className={cn('text-[11px] font-medium', config.text)}>{config.label}</span>
                </div>
              </div>

              <div className="flex items-center gap-3 mt-2 flex-wrap">
                <span className="text-[11px] text-text-disabled">{formatDate(record.date)}</span>
                <span className="text-text-disabled text-[10px]">·</span>
                <span className="text-[11px] text-text-disabled">{formatMileage(record.mileage)}</span>
                {record.provider && (
                  <>
                    <span className="text-text-disabled text-[10px]">·</span>
                    <span className="text-[11px] text-text-disabled">{record.provider}</span>
                  </>
                )}
                {showVehicle && vehicle && (
                  <>
                    <span className="text-text-disabled text-[10px]">·</span>
                    <Link
                      href={`/vehicles/${vehicle.id}`}
                      className="text-[11px] text-accent-light hover:text-accent transition-colors"
                      onClick={(e) => e.stopPropagation()}
                    >
                      {vehicle.brand} {vehicle.model}
                    </Link>
                  </>
                )}
              </div>

              {record.nextScheduledDate && (
                <div className="mt-2 text-[11px] text-text-muted">
                  Proximo: <span className="text-fleet-maintenance">{formatDate(record.nextScheduledDate)}</span>
                  {record.nextScheduledMileage && (
                    <span className="ml-1">o {formatMileage(record.nextScheduledMileage)}</span>
                  )}
                </div>
              )}
            </div>
          </motion.div>
        )
      })}
    </div>
  )
}
