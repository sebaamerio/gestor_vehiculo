'use client'

import { useState } from 'react'
import { AppShell } from '@/components/layout/AppShell'
import { ReparacionList } from '@/components/reparacion/ReparacionList'
import { ReparacionModal } from '@/components/reparacion/ReparacionModal'
import { PageHeader } from '@/components/shared/PageHeader'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Wrench, CheckCircle2, DollarSign } from 'lucide-react'
import { MOCK_REPARACIONES, MOCK_VEHICLES, applyAutoStatus } from '@/lib/data'
import { formatCurrency } from '@/lib/utils'
import { motion } from 'framer-motion'
import type { ReparacionRecord, ReparacionFormData } from '@/lib/types'

export default function ReparacionPage() {
  const [reparaciones, setReparaciones] = useState<ReparacionRecord[]>(() => MOCK_REPARACIONES.map(applyAutoStatus))
  const [editingRecord, setEditingRecord] = useState<ReparacionRecord | undefined>(undefined)
  const [modalOpen, setModalOpen] = useState(false)

  const scheduled = reparaciones.filter((r) => r.status === 'scheduled')
  const completed = reparaciones.filter((r) => r.status === 'completed')
  const overdue = reparaciones.filter((r) => r.status === 'overdue')
  const totalCost = completed.reduce((s, r) => s + r.cost, 0)

  function handleEdit(id: string) {
    setEditingRecord(reparaciones.find((r) => r.id === id))
    setModalOpen(true)
  }

  function handleSave(data: ReparacionFormData) {
    if (!editingRecord) return
    setReparaciones((prev) =>
      prev.map((r) => (r.id === editingRecord.id ? applyAutoStatus({ ...r, ...data }) : r))
    )
  }

  const editingVehicle = editingRecord
    ? MOCK_VEHICLES.find((v) => v.id === editingRecord.vehicleId)
    : undefined

  return (
    <AppShell>
      <div className="px-6 md:px-8 py-8 max-w-[1200px] mx-auto">
        <PageHeader
          title="Reparaciones"
          description="Historial de servicios y reparaciones programadas"
          icon={Wrench}
        />

        {/* Summary cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {[
            { icon: Wrench, label: 'En Reparacion', value: scheduled.length, color: 'text-fleet-maintenance', bg: 'bg-fleet-maintenance-bg' },
            { icon: CheckCircle2, label: 'Reparadas', value: completed.length + overdue.length, color: 'text-fleet-active', bg: 'bg-fleet-active-bg' },
            { icon: DollarSign, label: 'Total Gastado', value: formatCurrency(totalCost), color: 'text-accent-light', bg: 'bg-accent/10' },
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
              En Reparacion
              {scheduled.length > 0 && (
                <span className="ml-1.5 text-[10px] bg-subtle px-1.5 py-0.5 rounded-full text-text-muted">
                  {scheduled.length}
                </span>
              )}
            </TabsTrigger>
            <TabsTrigger value="history" className="data-[state=active]:text-fleet-active">Reparadas</TabsTrigger>
          </TabsList>

          <TabsContent value="upcoming">
            <ReparacionList
              records={scheduled}
              vehiculos={MOCK_VEHICLES}
              onEdit={handleEdit}
            />
          </TabsContent>

          <TabsContent value="history">
            <ReparacionList
              records={[...completed, ...overdue].sort((a, b) => b.date.localeCompare(a.date))}
              vehiculos={MOCK_VEHICLES}
              onEdit={handleEdit}
            />
          </TabsContent>
        </Tabs>
      </div>

      <ReparacionModal
        open={modalOpen}
        onClose={() => setModalOpen(false)}
        vehicleMileage={editingVehicle?.mileage ?? 0}
        record={editingRecord}
        onSave={handleSave}
      />
    </AppShell>
  )
}
