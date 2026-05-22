'use client'

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from '@/components/ui/dialog'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Separator } from '@/components/ui/separator'
import { Car } from 'lucide-react'
import { cn } from '@/lib/utils'
import type { Vehicle, VehicleFormData, Driver } from '@/lib/types'
import { MOCK_DRIVERS } from '@/lib/data'

interface VehicleModalProps {
  open: boolean
  onClose: () => void
  vehicle?: Vehicle
  onSave: (data: VehicleFormData) => void
}

const CURRENT_YEAR = new Date().getFullYear()
const YEARS = Array.from({ length: 30 }, (_, i) => CURRENT_YEAR - i)

const BRANDS = [
  'Audi', 'BMW', 'Chevrolet', 'Fiat', 'Ford', 'Honda', 'Hyundai',
  'Jeep', 'Kia', 'Land Rover', 'Mercedes-Benz', 'Nissan', 'Peugeot',
  'Porsche', 'Renault', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo', 'Other',
]

function FormField({
  label,
  children,
  required,
  error,
}: {
  label: string
  children: React.ReactNode
  required?: boolean
  error?: string
}) {
  return (
    <div className="space-y-1.5">
      <Label>
        {label}
        {required && <span className="text-fleet-danger ml-0.5">*</span>}
      </Label>
      {children}
      {error && <p className="text-[11px] text-fleet-danger">{error}</p>}
    </div>
  )
}

const EMPTY_FORM: VehicleFormData = {
  brand: '',
  model: '',
  year: CURRENT_YEAR,
  plateNumber: '',
  vin: '',
  mileage: 0,
  fuelType: 'gasoline',
  status: 'active',
  assignedDriverId: undefined,
  insuranceExpiration: '',
  technicalInspectionExpiration: '',
  color: '',
  purchaseDate: '',
  purchaseCost: undefined,
  notes: '',
}

export function VehicleModal({ open, onClose, vehicle, onSave }: VehicleModalProps) {
  const [form, setForm] = useState<VehicleFormData>(EMPTY_FORM)
  const [errors, setErrors] = useState<Partial<Record<keyof VehicleFormData, string>>>({})
  const [saving, setSaving] = useState(false)

  useEffect(() => {
    if (vehicle) {
      setForm({
        brand: vehicle.brand,
        model: vehicle.model,
        year: vehicle.year,
        plateNumber: vehicle.plateNumber,
        vin: vehicle.vin,
        mileage: vehicle.mileage,
        fuelType: vehicle.fuelType,
        status: vehicle.status,
        assignedDriverId: vehicle.assignedDriverId,
        insuranceExpiration: vehicle.insuranceExpiration,
        technicalInspectionExpiration: vehicle.technicalInspectionExpiration,
        color: vehicle.color || '',
        purchaseDate: vehicle.purchaseDate || '',
        purchaseCost: vehicle.purchaseCost,
        notes: vehicle.notes || '',
      })
    } else {
      setForm(EMPTY_FORM)
    }
    setErrors({})
  }, [vehicle, open])

  function update<K extends keyof VehicleFormData>(key: K, value: VehicleFormData[K]) {
    setForm((prev) => ({ ...prev, [key]: value }))
    setErrors((prev) => ({ ...prev, [key]: undefined }))
  }

  function validate(): boolean {
    const newErrors: Partial<Record<keyof VehicleFormData, string>> = {}
    if (!form.brand) newErrors.brand = 'Brand is required'
    if (!form.model) newErrors.model = 'Model is required'
    if (!form.plateNumber) newErrors.plateNumber = 'Plate number is required'
    if (!form.vin) newErrors.vin = 'VIN is required'
    if (!form.insuranceExpiration) newErrors.insuranceExpiration = 'Insurance expiration is required'
    if (!form.technicalInspectionExpiration) newErrors.technicalInspectionExpiration = 'Inspection date is required'
    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  async function handleSubmit() {
    if (!validate()) return
    setSaving(true)
    await new Promise((r) => setTimeout(r, 600))
    onSave(form)
    setSaving(false)
    onClose()
  }

  const isEdit = !!vehicle

  return (
    <Dialog open={open} onOpenChange={(o) => !o && onClose()}>
      <DialogContent className="max-w-2xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-accent/10 border border-accent/20 flex items-center justify-center flex-shrink-0">
              <Car className="w-4 h-4 text-accent-light" />
            </div>
            <div>
              <DialogTitle>{isEdit ? 'Edit Vehicle' : 'Add New Vehicle'}</DialogTitle>
              <DialogDescription className="mt-0.5">
                {isEdit ? 'Update vehicle information' : 'Enter details for the new fleet vehicle'}
              </DialogDescription>
            </div>
          </div>
        </DialogHeader>

        <div className="px-6 py-4 space-y-6">
          {/* Basic Info */}
          <div>
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-3">Vehicle Info</p>
            <div className="grid grid-cols-2 gap-3">
              <FormField label="Brand" required error={errors.brand}>
                <Select value={form.brand} onValueChange={(v) => update('brand', v)}>
                  <SelectTrigger className={cn(errors.brand && 'border-fleet-danger/50')}>
                    <SelectValue placeholder="Select brand" />
                  </SelectTrigger>
                  <SelectContent>
                    {BRANDS.map((b) => <SelectItem key={b} value={b}>{b}</SelectItem>)}
                  </SelectContent>
                </Select>
              </FormField>

              <FormField label="Model" required error={errors.model}>
                <Input
                  placeholder="e.g. Camry, Model 3"
                  value={form.model}
                  onChange={(e) => update('model', e.target.value)}
                  error={!!errors.model}
                />
              </FormField>

              <FormField label="Year">
                <Select value={String(form.year)} onValueChange={(v) => update('year', Number(v))}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    {YEARS.map((y) => <SelectItem key={y} value={String(y)}>{y}</SelectItem>)}
                  </SelectContent>
                </Select>
              </FormField>

              <FormField label="Fuel Type">
                <Select value={form.fuelType} onValueChange={(v) => update('fuelType', v as typeof form.fuelType)}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="gasoline">Gasoline</SelectItem>
                    <SelectItem value="diesel">Diesel</SelectItem>
                    <SelectItem value="electric">Electric</SelectItem>
                    <SelectItem value="hybrid">Hybrid</SelectItem>
                    <SelectItem value="cng">CNG</SelectItem>
                  </SelectContent>
                </Select>
              </FormField>
            </div>
          </div>

          <Separator />

          {/* Registration */}
          <div>
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-3">Registration</p>
            <div className="grid grid-cols-2 gap-3">
              <FormField label="Plate Number" required error={errors.plateNumber}>
                <Input
                  placeholder="ABC-1234"
                  value={form.plateNumber}
                  onChange={(e) => update('plateNumber', e.target.value.toUpperCase())}
                  className="font-mono"
                  error={!!errors.plateNumber}
                />
              </FormField>

              <FormField label="VIN" required error={errors.vin}>
                <Input
                  placeholder="17-char VIN"
                  value={form.vin}
                  onChange={(e) => update('vin', e.target.value.toUpperCase())}
                  className="font-mono text-[12px]"
                  error={!!errors.vin}
                />
              </FormField>

              <FormField label="Status">
                <Select value={form.status} onValueChange={(v) => update('status', v as typeof form.status)}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="active">Active</SelectItem>
                    <SelectItem value="maintenance">In Maintenance</SelectItem>
                    <SelectItem value="inactive">Inactive</SelectItem>
                    <SelectItem value="out_of_service">Out of Service</SelectItem>
                  </SelectContent>
                </Select>
              </FormField>

              <FormField label="Mileage (km)">
                <Input
                  type="number"
                  placeholder="0"
                  value={form.mileage || ''}
                  onChange={(e) => update('mileage', Number(e.target.value))}
                />
              </FormField>
            </div>
          </div>

          <Separator />

          {/* Expiry dates */}
          <div>
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-3">Documents</p>
            <div className="grid grid-cols-2 gap-3">
              <FormField label="Insurance Expiration" required error={errors.insuranceExpiration}>
                <Input
                  type="date"
                  value={form.insuranceExpiration}
                  onChange={(e) => update('insuranceExpiration', e.target.value)}
                  error={!!errors.insuranceExpiration}
                />
              </FormField>

              <FormField label="Inspection Expiration" required error={errors.technicalInspectionExpiration}>
                <Input
                  type="date"
                  value={form.technicalInspectionExpiration}
                  onChange={(e) => update('technicalInspectionExpiration', e.target.value)}
                  error={!!errors.technicalInspectionExpiration}
                />
              </FormField>
            </div>
          </div>

          <Separator />

          {/* Optional */}
          <div>
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-3">Optional Details</p>
            <div className="grid grid-cols-2 gap-3">
              <FormField label="Assigned Driver">
                <Select
                  value={form.assignedDriverId || 'none'}
                  onValueChange={(v) => update('assignedDriverId', v === 'none' ? undefined : v)}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="No driver assigned" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="none">No driver assigned</SelectItem>
                    {MOCK_DRIVERS.filter((d) => d.status === 'active').map((d) => (
                      <SelectItem key={d.id} value={d.id}>{d.name}</SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </FormField>

              <FormField label="Purchase Date">
                <Input
                  type="date"
                  value={form.purchaseDate}
                  onChange={(e) => update('purchaseDate', e.target.value)}
                />
              </FormField>

              <FormField label="Purchase Cost ($)">
                <Input
                  type="number"
                  placeholder="0"
                  value={form.purchaseCost || ''}
                  onChange={(e) => update('purchaseCost', Number(e.target.value) || undefined)}
                />
              </FormField>

              <FormField label="Color">
                <Input
                  placeholder="e.g. Midnight Black"
                  value={form.color}
                  onChange={(e) => update('color', e.target.value)}
                />
              </FormField>
            </div>

            <div className="mt-3">
              <FormField label="Notes">
                <Textarea
                  placeholder="Additional notes about this vehicle…"
                  value={form.notes}
                  onChange={(e) => update('notes', e.target.value)}
                  rows={3}
                />
              </FormField>
            </div>
          </div>
        </div>

        <DialogFooter>
          <Button variant="ghost" onClick={onClose} disabled={saving}>
            Cancel
          </Button>
          <Button onClick={handleSubmit} disabled={saving}>
            {saving ? (
              <span className="flex items-center gap-2">
                <motion.div
                  animate={{ rotate: 360 }}
                  transition={{ duration: 0.8, repeat: Infinity, ease: 'linear' }}
                  className="w-3.5 h-3.5 border-2 border-white/30 border-t-white rounded-full"
                />
                Saving…
              </span>
            ) : isEdit ? 'Save Changes' : 'Add Vehicle'}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
