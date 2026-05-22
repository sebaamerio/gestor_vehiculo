'use client'

import { AppShell } from '@/components/layout/AppShell'
import { DriverCard } from '@/components/drivers/DriverCard'
import { PageHeader } from '@/components/shared/PageHeader'
import { Users } from 'lucide-react'
import { MOCK_DRIVERS, MOCK_VEHICLES } from '@/lib/data'
import { motion } from 'framer-motion'

export default function DriversPage() {
  const activeDrivers = MOCK_DRIVERS.filter((d) => d.status === 'active')
  const otherDrivers = MOCK_DRIVERS.filter((d) => d.status !== 'active')

  return (
    <AppShell>
      <div className="px-6 md:px-8 py-8 max-w-[1200px] mx-auto">
        <PageHeader
          title="Drivers"
          description={`${MOCK_DRIVERS.length} total · ${activeDrivers.length} active`}
          icon={Users}
        />

        {/* Active drivers */}
        <div className="mb-8">
          <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-4">
            Active Drivers ({activeDrivers.length})
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {activeDrivers.map((driver, i) => {
              const vehicle = MOCK_VEHICLES.find((v) => v.id === driver.assignedVehicleId)
              return <DriverCard key={driver.id} driver={driver} vehicle={vehicle} index={i} />
            })}
          </div>
        </div>

        {/* Other drivers */}
        {otherDrivers.length > 0 && (
          <div>
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-4">
              Inactive / On Leave ({otherDrivers.length})
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {otherDrivers.map((driver, i) => {
                const vehicle = MOCK_VEHICLES.find((v) => v.id === driver.assignedVehicleId)
                return <DriverCard key={driver.id} driver={driver} vehicle={vehicle} index={i} />
              })}
            </div>
          </div>
        )}
      </div>
    </AppShell>
  )
}
