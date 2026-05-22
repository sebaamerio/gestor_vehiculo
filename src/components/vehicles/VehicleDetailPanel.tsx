'use client'

import { motion } from 'framer-motion'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Separator } from '@/components/ui/separator'
import { Progress } from '@/components/ui/progress'
import { Avatar, AvatarFallback } from '@/components/ui/avatar'
import { StatusBadge, FuelBadge } from '@/components/shared/StatusBadge'
import {
  Car, Gauge, Calendar, User, Shield, Wrench,
  FileText, Fuel, ChevronLeft, Edit, MapPin, Hash,
  TrendingUp, DollarSign, Clock
} from 'lucide-react'
import { Button } from '@/components/ui/button'
import Link from 'next/link'
import {
  cn, formatDate, formatMileage, formatCurrency, getBrandColor,
  daysUntilExpiry, getExpiryStatus, getMaintenanceTypeLabel
} from '@/lib/utils'
import type { Vehicle, Driver, MaintenanceRecord, FuelLog, VehicleDocument } from '@/lib/types'

interface VehicleDetailPanelProps {
  vehicle: Vehicle
  driver?: Driver
  maintenance: MaintenanceRecord[]
  fuelLogs: FuelLog[]
  documents: VehicleDocument[]
  onEdit: () => void
}

function DetailRow({ label, value, mono }: { label: string; value: React.ReactNode; mono?: boolean }) {
  return (
    <div className="flex items-center justify-between py-2.5 border-b border-subtle last:border-0">
      <span className="text-[12px] text-text-muted">{label}</span>
      <span className={cn('text-[13px] font-medium text-text-primary', mono && 'font-mono text-[12px]')}>
        {value}
      </span>
    </div>
  )
}

function ExpiryBadge({ dateStr }: { dateStr: string }) {
  const status = getExpiryStatus(dateStr)
  const days = daysUntilExpiry(dateStr)

  const config = {
    expired: { bg: 'bg-fleet-danger-bg', text: 'text-fleet-danger', label: 'Vencido' },
    critical: { bg: 'bg-fleet-danger-bg', text: 'text-fleet-danger', label: `${days}d left` },
    warning: { bg: 'bg-fleet-maintenance-bg', text: 'text-fleet-maintenance', label: `${days}d left` },
    ok: { bg: 'bg-fleet-active-bg', text: 'text-fleet-active', label: formatDate(dateStr) },
  }[status]

  return (
    <span className={cn('text-[11px] font-medium px-2 py-0.5 rounded-full', config.bg, config.text)}>
      {config.label}
    </span>
  )
}

export function VehicleDetailPanel({
  vehicle, driver, maintenance, fuelLogs, documents, onEdit,
}: VehicleDetailPanelProps) {
  const brandColor = vehicle.brandColor || getBrandColor(vehicle.brand)
  const totalMaintenanceCost = maintenance.reduce((sum, m) => sum + m.cost, 0)
  const totalFuelCost = fuelLogs.reduce((sum, f) => sum + f.cost, 0)

  return (
    <div className="min-h-screen bg-base">
      {/* Back navigation */}
      <div className="px-8 pt-6">
        <Link
          href="/vehicles"
          className="inline-flex items-center gap-1.5 text-[13px] text-text-muted hover:text-text-secondary transition-colors mb-6"
        >
          <ChevronLeft className="w-4 h-4" />
          Volver a la Flota
        </Link>
      </div>

      <div className="px-8 pb-10">
        {/* Hero header */}
        <motion.div
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: 1, y: 0 }}
          className="flex flex-col md:flex-row md:items-start justify-between gap-6 mb-8"
        >
          <div className="flex items-start gap-5">
            {/* Brand icon */}
            <div
              className="w-16 h-16 rounded-2xl flex items-center justify-center border flex-shrink-0"
              style={{
                backgroundColor: brandColor + '15',
                borderColor: brandColor + '30',
              }}
            >
              <Car className="w-8 h-8" style={{ color: brandColor }} />
            </div>

            <div>
              <div className="flex items-center gap-3 mb-1">
                <span
                  className="text-[11px] font-bold uppercase tracking-widest"
                  style={{ color: brandColor }}
                >
                  {vehicle.brand}
                </span>
                <span className="text-text-disabled text-[11px]">{vehicle.year}</span>
              </div>
              <h1 className="text-2xl font-bold text-text-primary tracking-tight mb-2">
                {vehicle.model}
              </h1>
              <div className="flex items-center gap-3 flex-wrap">
                <StatusBadge status={vehicle.status} />
                <FuelBadge fuelType={vehicle.fuelType} />
                <span className="plate text-[13px] text-text-muted">{vehicle.plateNumber}</span>
              </div>
            </div>
          </div>

          <Button onClick={onEdit} variant="outline" size="sm" className="flex-shrink-0">
            <Edit className="w-3.5 h-3.5 mr-1.5" />
            Editar Vehiculo
          </Button>
        </motion.div>

        {/* Quick stats bar */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {[
            { icon: Gauge, label: 'Kilometraje', value: formatMileage(vehicle.mileage) },
            { icon: DollarSign, label: 'Total Reparaciones', value: formatCurrency(totalMaintenanceCost) },
            { icon: Fuel, label: 'Combustible Gastado', value: formatCurrency(totalFuelCost) },
            { icon: Clock, label: 'En Flota Desde', value: vehicle.purchaseDate ? formatDate(vehicle.purchaseDate, 'MMM yyyy') : '—' },
          ].map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.05 }}
              className="bg-surface rounded-xl border border-subtle p-4"
            >
              <stat.icon className="w-4 h-4 text-text-muted mb-2" />
              <div className="text-[11px] text-text-muted mb-0.5">{stat.label}</div>
              <div className="text-[15px] font-semibold text-text-primary">{stat.value}</div>
            </motion.div>
          ))}
        </div>

        {/* Tabs */}
        <Tabs defaultValue="overview">
          <TabsList>
            <TabsTrigger value="overview">Resumen</TabsTrigger>
            <TabsTrigger value="maintenance">
              Reparaciones
              {maintenance.length > 0 && (
                <span className="ml-1.5 text-[10px] bg-subtle px-1.5 py-0.5 rounded-full text-text-muted">
                  {maintenance.length}
                </span>
              )}
            </TabsTrigger>
            <TabsTrigger value="documents">Documentos</TabsTrigger>
            <TabsTrigger value="fuel">Combustible</TabsTrigger>
          </TabsList>

          {/* Overview Tab */}
          <TabsContent value="overview">
            <div className="grid md:grid-cols-2 gap-6">
              {/* Vehicle specs */}
              <div className="bg-surface rounded-2xl border border-subtle p-5">
                <h3 className="text-[13px] font-semibold text-text-primary mb-1">Especificaciones</h3>
                <p className="text-[12px] text-text-muted mb-4">Detalles tecnicos</p>
                <div>
                  <DetailRow label="Marca" value={vehicle.brand} />
                  <DetailRow label="Modelo" value={vehicle.model} />
                  <DetailRow label="Año" value={vehicle.year} />
                  <DetailRow label="Patente" value={vehicle.plateNumber} mono />
                  <DetailRow label="Motor" value={vehicle.motor} />
                  <DetailRow label="Chasis" value={vehicle.chasis} mono />
                  <DetailRow label="Combustible" value={<FuelBadge fuelType={vehicle.fuelType} size="sm" />} />
                  <DetailRow label="Kilometraje" value={formatMileage(vehicle.mileage)} />
                </div>
              </div>

              {/* Documents & Driver */}
              <div className="space-y-4">
                {/* Driver */}
                <div className="bg-surface rounded-2xl border border-subtle p-5">
                  <h3 className="text-[13px] font-semibold text-text-primary mb-3">Conductor Asignado</h3>
                  {driver ? (
                    <div className="flex items-center gap-3">
                      <Avatar className="w-10 h-10">
                        <AvatarFallback>{driver.initials}</AvatarFallback>
                      </Avatar>
                      <div>
                        <div className="text-[14px] font-semibold text-text-primary">{driver.name}</div>
                        <div className="text-[12px] text-text-muted">{driver.email}</div>
                        <div className="text-[12px] text-text-muted">{driver.phone}</div>
                      </div>
                    </div>
                  ) : (
                    <p className="text-[13px] text-text-muted">Sin conductor asignado</p>
                  )}
                </div>

                {/* Document expiry */}
                <div className="bg-surface rounded-2xl border border-subtle p-5">
                  <h3 className="text-[13px] font-semibold text-text-primary mb-3">Estado de Documentos</h3>
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <Shield className="w-3.5 h-3.5 text-text-muted" />
                        <span className="text-[13px] text-text-secondary">Seguro</span>
                      </div>
                      <ExpiryBadge dateStr={vehicle.insuranceExpiration} />
                    </div>
                    <Separator />
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <FileText className="w-3.5 h-3.5 text-text-muted" />
                        <span className="text-[13px] text-text-secondary">VTV</span>
                      </div>
                      <ExpiryBadge dateStr={vehicle.technicalInspectionExpiration} />
                    </div>
                  </div>
                </div>

                {/* Notes */}
                {vehicle.notes && (
                  <div className="bg-surface rounded-2xl border border-subtle p-5">
                    <h3 className="text-[13px] font-semibold text-text-primary mb-2">Notas</h3>
                    <p className="text-[13px] text-text-secondary leading-relaxed">{vehicle.notes}</p>
                  </div>
                )}
              </div>
            </div>
          </TabsContent>

          {/* Maintenance Tab */}
          <TabsContent value="maintenance">
            {maintenance.length === 0 ? (
              <div className="bg-surface rounded-2xl border border-subtle p-12 text-center">
                <Wrench className="w-8 h-8 text-text-muted mx-auto mb-3" />
                <p className="text-[13px] text-text-muted">Sin registros de reparacion</p>
              </div>
            ) : (
              <div className="space-y-3">
                {maintenance.map((record, i) => (
                  <motion.div
                    key={record.id}
                    initial={{ opacity: 0, y: 6 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.04 }}
                    className="bg-surface rounded-xl border border-subtle p-4 flex items-start gap-4"
                  >
                    <div className={cn(
                      'w-8 h-8 rounded-lg flex items-center justify-center flex-shrink-0 mt-0.5',
                      record.status === 'completed' ? 'bg-fleet-active-bg' :
                      record.status === 'overdue' ? 'bg-fleet-danger-bg' : 'bg-fleet-maintenance-bg'
                    )}>
                      <Wrench className={cn(
                        'w-4 h-4',
                        record.status === 'completed' ? 'text-fleet-active' :
                        record.status === 'overdue' ? 'text-fleet-danger' : 'text-fleet-maintenance'
                      )} />
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between gap-2">
                        <span className="text-[14px] font-semibold text-text-primary">
                          {getMaintenanceTypeLabel(record.type)}
                        </span>
                        <span className="text-[14px] font-semibold text-text-primary flex-shrink-0">
                          {record.cost > 0 ? formatCurrency(record.cost) : 'Gratis'}
                        </span>
                      </div>
                      <p className="text-[12px] text-text-muted mt-0.5">{record.description}</p>
                      <div className="flex items-center gap-3 mt-2 text-[11px] text-text-disabled">
                        <span>{formatDate(record.date)}</span>
                        <span>·</span>
                        <span>{formatMileage(record.mileage)}</span>
                        {record.provider && (
                          <>
                            <span>·</span>
                            <span>{record.provider}</span>
                          </>
                        )}
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            )}
          </TabsContent>

          {/* Documents Tab */}
          <TabsContent value="documents">
            {documents.length === 0 ? (
              <div className="bg-surface rounded-2xl border border-subtle p-12 text-center">
                <FileText className="w-8 h-8 text-text-muted mx-auto mb-3" />
                <p className="text-[13px] text-text-muted">Sin documentos registrados</p>
              </div>
            ) : (
              <div className="space-y-3">
                {documents.map((doc, i) => (
                  <motion.div
                    key={doc.id}
                    initial={{ opacity: 0, y: 6 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.04 }}
                    className="bg-surface rounded-xl border border-subtle p-4 flex items-center gap-4"
                  >
                    <div className="w-8 h-8 rounded-lg bg-accent/10 flex items-center justify-center flex-shrink-0">
                      <FileText className="w-4 h-4 text-accent-light" />
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="text-[14px] font-semibold text-text-primary">{doc.name}</div>
                      <div className="text-[12px] text-text-muted mt-0.5">
                        {doc.provider} · Emitido {formatDate(doc.issueDate)}
                      </div>
                    </div>
                    <ExpiryBadge dateStr={doc.expirationDate} />
                  </motion.div>
                ))}
              </div>
            )}
          </TabsContent>

          {/* Fuel Tab */}
          <TabsContent value="fuel">
            {fuelLogs.length === 0 ? (
              <div className="bg-surface rounded-2xl border border-subtle p-12 text-center">
                <Fuel className="w-8 h-8 text-text-muted mx-auto mb-3" />
                <p className="text-[13px] text-text-muted">Sin registros de combustible</p>
              </div>
            ) : (
              <div className="space-y-3">
                {fuelLogs.map((log, i) => (
                  <motion.div
                    key={log.id}
                    initial={{ opacity: 0, y: 6 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: i * 0.04 }}
                    className="bg-surface rounded-xl border border-subtle p-4 flex items-center gap-4"
                  >
                    <div className="w-8 h-8 rounded-lg bg-blue-500/10 flex items-center justify-center flex-shrink-0">
                      <Fuel className="w-4 h-4 text-blue-400" />
                    </div>
                    <div className="flex-1">
                      <div className="flex items-center justify-between">
                        <span className="text-[14px] font-semibold text-text-primary">
                          {vehicle.fuelType === 'electric' ? `${log.cost.toFixed(2)} kWh charge` : `${log.liters}L filled`}
                        </span>
                        <span className="text-[14px] font-semibold text-text-primary">{formatCurrency(log.cost)}</span>
                      </div>
                      <div className="flex items-center gap-3 mt-1 text-[11px] text-text-disabled">
                        <span>{formatDate(log.date)}</span>
                        <span>·</span>
                        <span>{formatMileage(log.mileage)}</span>
                        {log.station && (
                          <>
                            <span>·</span>
                            <span>{log.station}</span>
                          </>
                        )}
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            )}
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}
