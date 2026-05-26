'use client'

import { motion } from 'framer-motion'
import { Wrench, CheckCircle2, Clock, AlertCircle, Calendar, Pencil } from 'lucide-react'
import Link from 'next/link'
import { cn, formatDate, formatCurrency, getReparacionTypeLabel } from '@/lib/utils'
import type { ReparacionRecord, Vehicle } from '@/lib/types'

interface ReparacionListProps {
  records: ReparacionRecord[]
  vehiculos: Vehicle[]
  title?: string
  showVehicle?: boolean
  onEdit?: (id: string) => void
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

export function ReparacionList({
  records,
  vehiculos,
  title,
  showVehicle = true,
  onEdit,
}: ReparacionListProps) {
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
        const vehicle = vehiculos.find((v) => v.id === record.vehicleId)

        return (
          <motion.div
            key={record.id}
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: i * 0.04 }}
            className="bg-surface rounded-xl border border-subtle p-4 hover:border-subtle-hover transition-colors"
          >
            {/* Header: tipo + estado + editar */}
            <div className="flex items-center justify-between gap-3">
              <div className="flex items-center gap-3 min-w-0">
                <div className={cn('w-8 h-8 rounded-lg flex items-center justify-center flex-shrink-0', config.bg)}>
                  <StatusIcon className={cn('w-4 h-4', config.text)} />
                </div>
                <span className="text-[15px] font-semibold text-text-primary truncate">
                  {getReparacionTypeLabel(record.type)}
                </span>
              </div>
              <div className="flex items-center gap-2 flex-shrink-0">
                <span className={cn('text-[11px] font-semibold px-2.5 py-1 rounded-full', config.bg, config.text)}>
                  {config.label}
                </span>
                {onEdit && (
                  <button
                    onClick={() => onEdit(record.id)}
                    className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-[12px] font-medium bg-accent/10 text-accent-light hover:bg-accent/20 transition-colors"
                  >
                    <Pencil className="w-3 h-3" />
                    Editar
                  </button>
                )}
              </div>
            </div>

            {/* Patente + vehiculo */}
            {showVehicle && vehicle && (
              <div className="flex items-center gap-2 mt-1.5">
                <span className="plate text-[12px] font-bold">{vehicle.plateNumber}</span>
                <Link
                  href={`/vehiculos/${vehicle.id}`}
                  className="text-[12px] text-text-secondary hover:text-text-primary transition-colors"
                  onClick={(e) => e.stopPropagation()}
                >
                  {vehicle.brand} {vehicle.model} {vehicle.year}
                </Link>
              </div>
            )}

            {/* Fechas + costo */}
            <div className="flex items-center justify-between mt-2">
              <div className="flex items-center gap-1.5">
                <Calendar className="w-3 h-3 text-text-disabled flex-shrink-0" />
                <span className="text-[11px] text-text-muted">Ingreso:</span>
                <span className="text-[11px] text-text-secondary font-medium">{formatDate(record.date, 'dd-MM-yyyy')}</span>
                <span className="text-text-disabled text-[10px] mx-1">·</span>
                <span className="text-[11px] text-text-muted">Entrega:</span>
                <span className="text-[11px] text-text-secondary font-medium">
                  {record.deliveryDate ? formatDate(record.deliveryDate, 'dd-MM-yyyy') : '—'}
                </span>
              </div>
              <span className="text-[14px] font-semibold text-text-primary flex-shrink-0">
                {record.cost > 0 ? formatCurrency(record.cost) : '—'}
              </span>
            </div>

            {/* Descripcion opcional */}
            {record.description && (
              <p className="text-[12px] text-text-muted mt-2 leading-relaxed">{record.description}</p>
            )}
          </motion.div>
        )
      })}
    </div>
  )
}
