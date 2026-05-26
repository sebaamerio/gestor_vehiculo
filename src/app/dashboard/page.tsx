'use client'

import { AppShell } from '@/components/layout/AppShell'
import { StatsGrid } from '@/components/dashboard/StatsGrid'
import { FleetStatusCard } from '@/components/dashboard/FleetStatusCard'
import { ReparacionAlerts } from '@/components/dashboard/ReparacionAlerts'
import { RecentActivity } from '@/components/dashboard/RecentActivity'
import { ExpenseChart } from '@/components/dashboard/ExpenseChart'
import { VehicleModal } from '@/components/vehiculos/VehicleModal'
import { getDashboardStats, MOCK_ALERTS, MOCK_VEHICLES } from '@/lib/data'
import { useState } from 'react'
import { motion } from 'framer-motion'
import { format } from 'date-fns'
import type { VehicleFormData } from '@/lib/types'

export default function DashboardPage() {
  const [modalOpen, setModalOpen] = useState(false)
  const stats = getDashboardStats()

  function handleSave(data: VehicleFormData) {
    console.log('New vehicle:', data)
  }

  const greeting = (() => {
    const h = new Date().getHours()
    if (h < 12) return 'Buenos dias'
    if (h < 18) return 'Buenas tardes'
    return 'Buenas noches'
  })()

  return (
    <AppShell onAddVehicle={() => setModalOpen(true)}>
      <div className="px-6 md:px-8 py-8 max-w-[1400px] mx-auto">
        {/* Page header */}
        <motion.div
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.25 }}
          className="mb-8"
        >
          <div className="flex items-end justify-between">
            <div>
              <p className="text-[13px] text-text-muted mb-1">{greeting}</p>
              <h1 className="text-2xl font-bold text-text-primary tracking-tight">Resumen de Flota</h1>
              <p className="text-[13px] text-text-muted mt-1">
                {format(new Date(), "EEEE, MMMM d, yyyy")}
              </p>
            </div>

            {/* Quick status pills */}
            <div className="hidden md:flex items-center gap-2">
              {stats.criticalAlerts > 0 && (
                <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-fleet-danger-bg border border-fleet-danger-border">
                  <span className="w-1.5 h-1.5 rounded-full bg-fleet-danger" />
                  <span className="text-[12px] font-medium text-fleet-danger">
                    {stats.criticalAlerts} {stats.criticalAlerts === 1 ? 'alerta critica' : 'alertas criticas'}
                  </span>
                </div>
              )}
              <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-fleet-active-bg border border-fleet-active-border">
                <span className="w-1.5 h-1.5 rounded-full bg-fleet-active status-pulse" />
                <span className="text-[12px] font-medium text-fleet-active">
                  {stats.activeVehicles} activos
                </span>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Stats grid */}
        <div className="mb-6">
          <StatsGrid stats={stats} />
        </div>

        {/* Middle row: Fleet status + Alerts */}
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-6 mb-6">
          <div className="lg:col-span-2">
            <FleetStatusCard stats={stats} />
          </div>
          <div className="lg:col-span-3">
            <ReparacionAlerts alerts={MOCK_ALERTS} />
          </div>
        </div>

        {/* Bottom row: Expense chart + Recent activity */}
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-6">
          <div className="lg:col-span-3">
            <ExpenseChart />
          </div>
          <div className="lg:col-span-2">
            <RecentActivity />
          </div>
        </div>
      </div>

      <VehicleModal
        open={modalOpen}
        onClose={() => setModalOpen(false)}
        onSave={handleSave}
      />
    </AppShell>
  )
}
