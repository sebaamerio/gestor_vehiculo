'use client'

import { motion } from 'framer-motion'
import Link from 'next/link'
import { Car, Gauge, Calendar, User, MoreHorizontal } from 'lucide-react'
import { cn, formatMileage, getBrandColor, getExpiryStatus } from '@/lib/utils'
import { StatusBadge, FuelBadge } from '@/components/shared/StatusBadge'
import type { Vehicle, Driver } from '@/lib/types'

interface VehicleCardProps {
  vehicle: Vehicle
  driver?: Driver
  index?: number
  onEdit?: (id: string) => void
}

export function VehicleCard({ vehicle, driver, index = 0, onEdit }: VehicleCardProps) {
  const brandColor = vehicle.brandColor || getBrandColor(vehicle.brand)
  const insuranceStatus = getExpiryStatus(vehicle.insuranceExpiration)
  const inspectionStatus = getExpiryStatus(vehicle.technicalInspectionExpiration)
  const insuranceExpired = insuranceStatus === 'expired' || insuranceStatus === 'critical'
  const inspectionExpired = inspectionStatus === 'expired' || inspectionStatus === 'critical'
  const hasExpired = insuranceExpired || inspectionExpired
  const expiredLabel = insuranceExpired && inspectionExpired
    ? 'VTV y Seguro vencidos'
    : inspectionExpired
    ? 'VTV vencida'
    : 'Seguro vencido'
  const hasWarning = insuranceStatus !== 'ok' || inspectionStatus !== 'ok'

  const accentBar = hasExpired
    ? 'bg-fleet-danger'
    : vehicle.status === 'maintenance'
    ? 'bg-fleet-maintenance'
    : vehicle.status === 'active'
    ? 'bg-fleet-active'
    : 'bg-subtle'

  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.28, delay: index * 0.05, ease: [0.4, 0, 0.2, 1] }}
    >
      <Link href={`/vehiculos/${vehicle.id}`} className="group block">
        <div
          className={cn(
            'relative rounded-2xl border bg-surface overflow-hidden cursor-pointer',
            'transition-all duration-200',
            'hover:-translate-y-1 hover:shadow-card-hover hover:border-subtle-hover',
            'shadow-card',
            vehicle.status === 'out_of_service' && 'opacity-70'
          )}
        >
          {/* Color accent bar */}
          <div className={cn('h-1 w-full', accentBar)} />

          {/* Card body */}
          <div className="p-5">
            {/* Header: Brand/Model + Actions */}
            <div className="flex items-start justify-between gap-2 mb-4">
              <div className="min-w-0">
                <div className="flex items-center gap-2 mb-0.5">
                  <div
                    className="w-6 h-6 rounded-md flex items-center justify-center flex-shrink-0"
                    style={{ backgroundColor: brandColor + '20', borderColor: brandColor + '30', border: '1px solid' }}
                  >
                    <Car className="w-3 h-3" style={{ color: brandColor }} />
                  </div>
                  <span className="text-[12px] font-semibold text-text-muted uppercase tracking-wider">
                    {vehicle.brand} · {vehicle.model}
                  </span>
                </div>
                <h3 className="text-[16px] font-semibold text-text-primary leading-tight plate">
                  {vehicle.plateNumber}
                </h3>
                <span className="text-[12px] text-text-muted mt-1">{vehicle.year}</span>
              </div>

              <button
                onClick={(e) => {
                  e.preventDefault()
                  e.stopPropagation()
                  onEdit?.(vehicle.id)
                }}
                className="w-7 h-7 rounded-lg flex items-center justify-center text-text-disabled hover:text-text-secondary hover:bg-subtle transition-colors opacity-0 group-hover:opacity-100"
              >
                <MoreHorizontal className="w-4 h-4" />
              </button>
            </div>

            {/* Status badges */}
            <div className="flex items-center gap-2 flex-wrap mb-4">
              {vehicle.status === 'active' && hasExpired ? (
                <span className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full text-[11px] font-medium bg-fleet-danger-bg text-fleet-danger border border-fleet-danger-border">
                  <span className="w-1.5 h-1.5 rounded-full bg-fleet-danger flex-shrink-0" />
                  {expiredLabel}
                </span>
              ) : (
                <StatusBadge status={vehicle.status} size="sm" />
              )}
              <FuelBadge fuelType={vehicle.fuelType} size="sm" />
            </div>

            {/* Stats grid */}
            <div className="grid grid-cols-2 gap-3 pt-4 border-t border-subtle">
              <div className="flex items-center gap-2">
                <Gauge className="w-3.5 h-3.5 text-text-disabled flex-shrink-0" />
                <div className="min-w-0">
                  <div className="text-[11px] text-text-muted">Kilometraje</div>
                  <div className="text-[13px] font-semibold text-text-primary">
                    {formatMileage(vehicle.mileage)}
                  </div>
                </div>
              </div>

              <div className="flex items-center gap-2">
                <User className="w-3.5 h-3.5 text-text-disabled flex-shrink-0" />
                <div className="min-w-0">
                  <div className="text-[11px] text-text-muted">Conductor</div>
                  <div className="text-[13px] font-semibold text-text-primary truncate">
                    {driver ? driver.name.split(' ')[0] : '—'}
                  </div>
                </div>
              </div>
            </div>

            {/* Warning indicator para vencimiento próximo (no crítico) */}
            {hasWarning && !hasExpired && (
              <div className="mt-3 flex items-center gap-1.5 text-[11px] text-fleet-maintenance">
                <div className="w-1.5 h-1.5 rounded-full bg-fleet-maintenance" />
                {insuranceStatus !== 'ok' ? 'Seguro' : 'VTV'} por vencer
              </div>
            )}
          </div>
        </div>
      </Link>
    </motion.div>
  )
}
