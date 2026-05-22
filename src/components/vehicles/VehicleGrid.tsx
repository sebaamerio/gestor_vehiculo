'use client'

import { useState, useMemo } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Search, Filter, SlidersHorizontal, Car, X } from 'lucide-react'
import { VehicleCard } from './VehicleCard'
import { EmptyState } from '@/components/shared/EmptyState'
import { Button } from '@/components/ui/button'
import { cn } from '@/lib/utils'
import type { Vehicle, Driver, VehicleStatus, FuelType } from '@/lib/types'

interface VehicleGridProps {
  vehicles: Vehicle[]
  drivers: Driver[]
  onEdit?: (id: string) => void
  onAdd?: () => void
}

const STATUS_FILTERS: { label: string; value: VehicleStatus | 'all' }[] = [
  { label: 'All', value: 'all' },
  { label: 'Active', value: 'active' },
  { label: 'Maintenance', value: 'maintenance' },
  { label: 'Inactive', value: 'inactive' },
  { label: 'Out of Service', value: 'out_of_service' },
]

const FUEL_FILTERS: { label: string; value: FuelType | 'all' }[] = [
  { label: 'All Fuels', value: 'all' },
  { label: 'Gasoline', value: 'gasoline' },
  { label: 'Diesel', value: 'diesel' },
  { label: 'Electric', value: 'electric' },
  { label: 'Hybrid', value: 'hybrid' },
]

export function VehicleGrid({ vehicles, drivers, onEdit, onAdd }: VehicleGridProps) {
  const [search, setSearch] = useState('')
  const [statusFilter, setStatusFilter] = useState<VehicleStatus | 'all'>('all')
  const [fuelFilter, setFuelFilter] = useState<FuelType | 'all'>('all')

  const filtered = useMemo(() => {
    return vehicles.filter((v) => {
      const matchesSearch =
        !search ||
        `${v.brand} ${v.model} ${v.plateNumber} ${v.vin}`.toLowerCase().includes(search.toLowerCase())
      const matchesStatus = statusFilter === 'all' || v.status === statusFilter
      const matchesFuel = fuelFilter === 'all' || v.fuelType === fuelFilter
      return matchesSearch && matchesStatus && matchesFuel
    })
  }, [vehicles, search, statusFilter, fuelFilter])

  const hasActiveFilters = statusFilter !== 'all' || fuelFilter !== 'all' || search

  return (
    <div>
      {/* Filter bar */}
      <div className="flex flex-col sm:flex-row gap-3 mb-6">
        {/* Search */}
        <div className="relative flex-1 max-w-sm">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-text-muted" />
          <input
            type="text"
            placeholder="Search by brand, plate, VIN…"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className={cn(
              'w-full h-9 pl-9 pr-4 rounded-lg border bg-surface-elevated text-[13px] text-text-primary',
              'placeholder:text-text-muted transition-all',
              'focus:outline-none focus:border-accent/40 focus:ring-1 focus:ring-accent/20',
              'border-subtle hover:border-subtle-hover'
            )}
          />
          {search && (
            <button
              onClick={() => setSearch('')}
              className="absolute right-2.5 top-1/2 -translate-y-1/2 text-text-muted hover:text-text-secondary transition-colors"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
        </div>

        {/* Status filter pills */}
        <div className="flex items-center gap-1.5 flex-wrap">
          {STATUS_FILTERS.map((f) => (
            <button
              key={f.value}
              onClick={() => setStatusFilter(f.value)}
              className={cn(
                'h-7 px-3 rounded-lg text-[12px] font-medium transition-all',
                statusFilter === f.value
                  ? 'bg-accent/15 text-accent-light border border-accent/25'
                  : 'bg-surface-elevated text-text-muted border border-subtle hover:border-subtle-hover hover:text-text-secondary'
              )}
            >
              {f.label}
            </button>
          ))}
        </div>
      </div>

      {/* Results count */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <span className="text-[13px] text-text-muted">
            {filtered.length} {filtered.length === 1 ? 'vehicle' : 'vehicles'}
            {hasActiveFilters && (
              <span className="text-text-disabled"> · filtered</span>
            )}
          </span>
          {hasActiveFilters && (
            <button
              onClick={() => {
                setSearch('')
                setStatusFilter('all')
                setFuelFilter('all')
              }}
              className="text-[12px] text-accent-light hover:text-accent transition-colors flex items-center gap-1"
            >
              <X className="w-3 h-3" /> Clear
            </button>
          )}
        </div>
      </div>

      {/* Vehicle grid */}
      <AnimatePresence mode="wait">
        {filtered.length === 0 ? (
          <EmptyState
            key="empty"
            icon={Car}
            title="No vehicles found"
            description={
              search
                ? `No vehicles match "${search}". Try a different search term.`
                : 'No vehicles match the selected filters.'
            }
            action={
              onAdd
                ? { label: 'Add Vehicle', onClick: onAdd }
                : undefined
            }
          />
        ) : (
          <motion.div
            key="grid"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4"
          >
            {filtered.map((vehicle, i) => {
              const driver = drivers.find((d) => d.id === vehicle.assignedDriverId)
              return (
                <VehicleCard
                  key={vehicle.id}
                  vehicle={vehicle}
                  driver={driver}
                  index={i}
                  onEdit={onEdit}
                />
              )
            })}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}
