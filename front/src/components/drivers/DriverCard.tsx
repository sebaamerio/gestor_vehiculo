'use client'

import { motion } from 'framer-motion'
import { Phone, Mail, Star, Car, Shield } from 'lucide-react'
import { Avatar, AvatarFallback } from '@/components/ui/avatar'
import { cn, formatDate, daysUntilExpiry, getExpiryStatus } from '@/lib/utils'
import type { Driver, Vehicle } from '@/lib/types'

interface DriverCardProps {
  driver: Driver
  vehicle?: Vehicle
  index?: number
}

const STATUS_CONFIG = {
  active: { bg: 'bg-fleet-active-bg', text: 'text-fleet-active', dot: 'bg-fleet-active', label: 'Activo' },
  inactive: { bg: 'bg-fleet-inactive-bg', text: 'text-fleet-inactive', dot: 'bg-fleet-inactive', label: 'Inactivo' },
  on_leave: { bg: 'bg-fleet-maintenance-bg', text: 'text-fleet-maintenance', dot: 'bg-fleet-maintenance', label: 'De Licencia' },
}

export function DriverCard({ driver, vehicle, index = 0 }: DriverCardProps) {
  const statusConfig = STATUS_CONFIG[driver.status]
  const licenseStatus = getExpiryStatus(driver.licenseExpiration)

  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.28, delay: index * 0.05 }}
      className="group bg-surface rounded-2xl border border-subtle p-5 hover:border-subtle-hover hover:-translate-y-0.5 transition-all shadow-card hover:shadow-card-hover cursor-default"
    >
      {/* Header */}
      <div className="flex items-start justify-between mb-4">
        <div className="flex items-center gap-3">
          <Avatar className="w-11 h-11">
            <AvatarFallback className="text-sm">{driver.initials}</AvatarFallback>
          </Avatar>
          <div>
            <div className="text-[15px] font-semibold text-text-primary">{driver.name}</div>
            <div className="flex items-center gap-1.5 mt-0.5">
              <span className={cn('flex items-center gap-1 text-[11px] font-medium', statusConfig.text)}>
                <span className={cn('w-1.5 h-1.5 rounded-full', statusConfig.dot, driver.status === 'active' ? 'status-pulse' : '')} />
                {statusConfig.label}
              </span>
            </div>
          </div>
        </div>

        {driver.rating && (
          <div className="flex items-center gap-1 bg-yellow-500/10 px-2 py-1 rounded-lg">
            <Star className="w-3 h-3 text-yellow-400 fill-yellow-400" />
            <span className="text-[12px] font-semibold text-yellow-400">{driver.rating}</span>
          </div>
        )}
      </div>

      {/* Contact */}
      <div className="space-y-1.5 mb-4">
        <div className="flex items-center gap-2 text-[12px] text-text-muted">
          <Mail className="w-3 h-3 flex-shrink-0" />
          <span className="truncate">{driver.email}</span>
        </div>
        <div className="flex items-center gap-2 text-[12px] text-text-muted">
          <Phone className="w-3 h-3 flex-shrink-0" />
          <span>{driver.phone}</span>
        </div>
      </div>

      {/* Divider */}
      <div className="border-t border-subtle pt-4">
        <div className="grid grid-cols-2 gap-3">
          {/* Vehicle */}
          <div>
            <div className="text-[10px] text-text-disabled uppercase tracking-wider mb-1">Vehiculo</div>
            {vehicle ? (
              <div className="flex items-center gap-1.5 text-[12px] text-text-secondary">
                <Car className="w-3 h-3 text-text-muted" />
                <span className="truncate">{vehicle.brand} {vehicle.model}</span>
              </div>
            ) : (
              <span className="text-[12px] text-text-muted">Sin asignar</span>
            )}
          </div>

          {/* License */}
          <div>
            <div className="text-[10px] text-text-disabled uppercase tracking-wider mb-1">Licencia</div>
            <div className="flex items-center gap-1.5">
              <Shield className="w-3 h-3 text-text-muted flex-shrink-0" />
              <span
                className={cn(
                  'text-[11px] font-medium',
                  licenseStatus === 'expired' || licenseStatus === 'critical' ? 'text-fleet-danger' :
                  licenseStatus === 'warning' ? 'text-fleet-maintenance' : 'text-fleet-active'
                )}
              >
                {licenseStatus === 'expired' ? 'Vencida' :
                 licenseStatus === 'ok' ? formatDate(driver.licenseExpiration, 'MMM yyyy') :
                 `${daysUntilExpiry(driver.licenseExpiration)}d restantes`}
              </span>
            </div>
          </div>
        </div>

        {driver.totalTrips !== undefined && (
          <div className="mt-3 text-[11px] text-text-muted">
            {driver.totalTrips} viajes · Desde {formatDate(driver.joinDate, 'MMM yyyy')}
          </div>
        )}
      </div>
    </motion.div>
  )
}
