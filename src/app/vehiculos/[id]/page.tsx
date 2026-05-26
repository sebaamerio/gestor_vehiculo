'use client'

import { useState } from 'react'
import { notFound } from 'next/navigation'
import { AppShell } from '@/components/layout/AppShell'
import { VehicleDetailPanel } from '@/components/vehiculos/VehicleDetailPanel'
import { VehicleModal } from '@/components/vehiculos/VehicleModal'
import { ReparacionModal } from '@/components/reparacion/ReparacionModal'
import {
  getVehicleById,
  getDriverByVehicleId,
  getReparacionByVehicleId,
  getFuelLogsByVehicleId,
  getDocumentsByVehicleId,
} from '@/lib/data'
import type { Vehicle, VehicleFormData, ReparacionRecord, ReparacionFormData } from '@/lib/types'

interface VehiclePageProps {
  params: { id: string }
}

export default function VehiclePage({ params }: VehiclePageProps) {
  const initialVehicle = getVehicleById(params.id)
  if (!initialVehicle) notFound()

  const [vehicle, setVehicle] = useState<Vehicle>(initialVehicle)
  const [modalOpen, setModalOpen] = useState(false)
  const [reparacionModalOpen, setReparacionModalOpen] = useState(false)
  const [editingRecord, setEditingRecord] = useState<ReparacionRecord | undefined>(undefined)
  const [reparacion, setReparacion] = useState<ReparacionRecord[]>(
    getReparacionByVehicleId(params.id)
  )

  const driver = getDriverByVehicleId(vehicle.id)
  const fuelLogs = getFuelLogsByVehicleId(vehicle.id)
  const documents = getDocumentsByVehicleId(vehicle.id)

  function handleSaveVehicle(data: VehicleFormData) {
    setVehicle((prev) => ({ ...prev, ...data, updatedAt: new Date().toISOString() }))
    setModalOpen(false)
  }

  function handleOpenAdd() {
    setEditingRecord(undefined)
    setReparacionModalOpen(true)
  }

  function handleOpenEdit(id: string) {
    setEditingRecord(reparacion.find((r) => r.id === id))
    setReparacionModalOpen(true)
  }

  function handleSaveReparacion(data: ReparacionFormData) {
    if (editingRecord) {
      setReparacion((prev) =>
        prev.map((r) => (r.id === editingRecord.id ? { ...r, ...data } : r))
      )
    } else {
      const newRecord: ReparacionRecord = {
        ...data,
        id: `r${Date.now()}`,
        vehicleId: vehicle.id,
      }
      setReparacion((prev) => [newRecord, ...prev])
    }
  }

  return (
    <AppShell>
      <VehicleDetailPanel
        vehicle={vehicle}
        driver={driver}
        reparacion={reparacion}
        fuelLogs={fuelLogs}
        documents={documents}
        onEdit={() => setModalOpen(true)}
        onAddMaintenance={handleOpenAdd}
        onEditReparacion={handleOpenEdit}
      />

      <VehicleModal
        open={modalOpen}
        onClose={() => setModalOpen(false)}
        vehicle={vehicle}
        onSave={handleSaveVehicle}
      />

      <ReparacionModal
        open={reparacionModalOpen}
        onClose={() => setReparacionModalOpen(false)}
        vehicleMileage={vehicle.mileage}
        record={editingRecord}
        onSave={handleSaveReparacion}
      />
    </AppShell>
  )
}
