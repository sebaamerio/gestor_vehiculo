'use client'

import { useState } from 'react'
import { notFound } from 'next/navigation'
import { AppShell } from '@/components/layout/AppShell'
import { VehicleDetailPanel } from '@/components/vehicles/VehicleDetailPanel'
import { VehicleModal } from '@/components/vehicles/VehicleModal'
import {
  getVehicleById,
  getDriverByVehicleId,
  getMaintenanceByVehicleId,
  getFuelLogsByVehicleId,
  getDocumentsByVehicleId,
} from '@/lib/data'
import type { Vehicle, VehicleFormData } from '@/lib/types'

interface VehiclePageProps {
  params: { id: string }
}

export default function VehiclePage({ params }: VehiclePageProps) {
  const initialVehicle = getVehicleById(params.id)
  if (!initialVehicle) notFound()

  const [vehicle, setVehicle] = useState<Vehicle>(initialVehicle)
  const [modalOpen, setModalOpen] = useState(false)

  const driver = getDriverByVehicleId(vehicle.id)
  const maintenance = getMaintenanceByVehicleId(vehicle.id)
  const fuelLogs = getFuelLogsByVehicleId(vehicle.id)
  const documents = getDocumentsByVehicleId(vehicle.id)

  function handleSave(data: VehicleFormData) {
    setVehicle((prev) => ({ ...prev, ...data, updatedAt: new Date().toISOString() }))
    setModalOpen(false)
  }

  return (
    <AppShell>
      <VehicleDetailPanel
        vehicle={vehicle}
        driver={driver}
        maintenance={maintenance}
        fuelLogs={fuelLogs}
        documents={documents}
        onEdit={() => setModalOpen(true)}
      />

      <VehicleModal
        open={modalOpen}
        onClose={() => setModalOpen(false)}
        vehicle={vehicle}
        onSave={handleSave}
      />
    </AppShell>
  )
}
