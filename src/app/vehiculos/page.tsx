'use client'

import { useState } from 'react'
import { AppShell } from '@/components/layout/AppShell'
import { VehicleGrid } from '@/components/vehiculos/VehicleGrid'
import { VehicleModal } from '@/components/vehiculos/VehicleModal'
import { PageHeader } from '@/components/shared/PageHeader'
import { Button } from '@/components/ui/button'
import { Plus, Car } from 'lucide-react'
import { MOCK_VEHICLES, MOCK_DRIVERS } from '@/lib/data'
import type { Vehicle, VehicleFormData } from '@/lib/types'

export default function VehiculosPage() {
  const [modalOpen, setModalOpen] = useState(false)
  const [editingVehicle, setEditingVehicle] = useState<Vehicle | undefined>()
  const [vehiculos, setVehiculos] = useState(MOCK_VEHICLES)

  function handleEdit(id: string) {
    const v = vehiculos.find((v) => v.id === id)
    if (v) {
      setEditingVehicle(v)
      setModalOpen(true)
    }
  }

  function handleAdd() {
    setEditingVehicle(undefined)
    setModalOpen(true)
  }

  function handleSave(data: VehicleFormData) {
    if (editingVehicle) {
      setVehiculos((prev) =>
        prev.map((v) =>
          v.id === editingVehicle.id ? { ...v, ...data, updatedAt: new Date().toISOString() } : v
        )
      )
    } else {
      const newVehicle: Vehicle = {
        ...data,
        id: `v${Date.now()}`,
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      }
      setVehiculos((prev) => [newVehicle, ...prev])
    }
    setModalOpen(false)
    setEditingVehicle(undefined)
  }

  return (
    <AppShell onAddVehicle={handleAdd}>
      <div className="px-6 md:px-8 py-8 max-w-[1400px] mx-auto">
        <PageHeader
          title="Vehiculos"
          description={`${vehiculos.length} vehiculos · ${vehiculos.filter((v) => v.status === 'active').length} activos`}
          icon={Car}
          actions={
            <Button onClick={handleAdd} size="sm">
              <Plus className="w-3.5 h-3.5 mr-1.5" />
              Agregar Vehiculo
            </Button>
          }
        />

        <VehicleGrid
          vehiculos={vehiculos}
          drivers={MOCK_DRIVERS}
          onEdit={handleEdit}
          onAdd={handleAdd}
        />
      </div>

      <VehicleModal
        open={modalOpen}
        onClose={() => {
          setModalOpen(false)
          setEditingVehicle(undefined)
        }}
        vehicle={editingVehicle}
        onSave={handleSave}
      />
    </AppShell>
  )
}
