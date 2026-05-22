'use client'

import { useState } from 'react'
import { AppShell } from '@/components/layout/AppShell'
import { MaintenanceList } from '@/components/maintenance/MaintenanceList'
import { PageHeader } from '@/components/shared/PageHeader'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Wrench, Calendar, DollarSign, AlertTriangle } from 'lucide-react'
import { MOCK_MAINTENANCE, MOCK_VEHICLES, getDashboardStats } from '@/lib/data'
import { formatCurrency } from '@/lib/utils'
import { motion } from 'framer-motion'

export default function MaintenancePage() {
  const stats = getDashboardStats()
  const scheduled = MOCK_MAINTENANCE.filter((m) => m.status === 'scheduled')
  const completed = MOCK_MAINTENANCE.filter((m) => m.status === 'completed')
  const overdue = MOCK_MAINTENANCE.filter((m) => m.status === 'overdue')
  const totalCost = MOCK_MAINTENANCE.filter((m) => m.status === 'completed').reduce((s, m) => s + m.cost, 0)

  return (
    <AppShell>
      <div className="px-6 md:px-8 py-8 max-w-[1200px] mx-auto">
        <PageHeader
          title="Maintenance"
          description="Track service history and upcoming maintenance"
          icon={Wrench}
        />

        {/* Summary cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {[
            { icon: AlertTriangle, label: 'Overdue', value: overdue.length, color: 'text-fleet-danger', bg: 'bg-fleet-danger-bg' },
            { icon: Calendar, label: 'Scheduled', value: scheduled.length, color: 'text-fleet-maintenance', bg: 'bg-fleet-maintenance-bg' },
            { icon: Wrench, label: 'Completed', value: completed.length, color: 'text-fleet-active', bg: 'bg-fleet-active-bg' },
            { icon: DollarSign, label: 'Total Spent', value: formatCurrency(totalCost), color: 'text-accent-light', bg: 'bg-accent/10' },
          ].map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.05 }}
              className="bg-surface rounded-xl border border-subtle p-4"
            >
              <div className={`w-8 h-8 rounded-lg ${stat.bg} flex items-center justify-center mb-3`}>
                <stat.icon className={`w-4 h-4 ${stat.color}`} />
              </div>
              <div className="text-[11px] text-text-muted mb-0.5">{stat.label}</div>
              <div className="text-xl font-bold text-text-primary">{stat.value}</div>
            </motion.div>
          ))}
        </div>

        {/* Tabs */}
        <Tabs defaultValue="upcoming">
          <TabsList className="mb-6">
            <TabsTrigger value="upcoming">
              Upcoming
              {scheduled.length > 0 && (
                <span className="ml-1.5 text-[10px] bg-subtle px-1.5 py-0.5 rounded-full text-text-muted">
                  {scheduled.length}
                </span>
              )}
            </TabsTrigger>
            <TabsTrigger value="history">History</TabsTrigger>
          </TabsList>

          <TabsContent value="upcoming">
            {overdue.length > 0 && (
              <div className="mb-6">
                <MaintenanceList
                  records={overdue}
                  vehicles={MOCK_VEHICLES}
                  title="Overdue"
                />
              </div>
            )}
            <MaintenanceList
              records={scheduled}
              vehicles={MOCK_VEHICLES}
              title={overdue.length > 0 ? 'Scheduled' : undefined}
            />
          </TabsContent>

          <TabsContent value="history">
            <MaintenanceList
              records={[...completed].sort((a, b) => b.date.localeCompare(a.date))}
              vehicles={MOCK_VEHICLES}
            />
          </TabsContent>
        </Tabs>
      </div>
    </AppShell>
  )
}
