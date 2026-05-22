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
  const hasWarning = insuranceStatus !== 'ok' || inspectionStatus !== 'ok'

  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.28, delay: index * 0.05, ease: [0.4, 0, 0.2, 1] }}
    >
      <Link href={`/vehicles/${vehicle.id}`} className="group block">
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
          <div
            className="h-1 w-full"
            style={{ background: brandColor, opacity: vehicle.status === 'active' ? 1 : 0.4 }}
          />

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
                    {vehicle.brand}
                  </span>
                </div>
                <h3 className="text-[16px] font-semibold text-text-primary leading-tight">
                  {vehicle.model}
                </h3>
                <div className="flex items-center gap-2 mt-1">
                  <span className="text-[12px] text-text-muted">{vehicle.year}</span>
                  <span className="text-text-disabled">·</span>
                  <span className="plate text-[12px] text-text-muted">{vehicle.plateNumber}</span>
                </div>
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
              <StatusBadge status={vehicle.status} size="sm" />
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

            {/* Warning indicator */}
            {hasWarning && (
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
