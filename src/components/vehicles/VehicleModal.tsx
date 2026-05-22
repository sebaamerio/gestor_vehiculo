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

const MODELS_BY_BRAND: Record<string, string[]> = {
  Audi:            ['A3', 'A4', 'A6', 'Q5', 'Q7'],
  BMW:             ['Serie 3', 'Serie 5', 'X3', 'X5', 'M3'],
  Chevrolet:       ['Onix', 'Cruze', 'Tracker', 'Spin', 'S10'],
  Fiat:            ['Cronos', 'Pulse', 'Toro', 'Strada', 'Mobi'],
  Ford:            ['Ranger', 'EcoSport', 'Focus', 'Kuga', 'Territory'],
  Honda:           ['Civic', 'CR-V', 'HR-V', 'Fit', 'WR-V'],
  Hyundai:         ['Tucson', 'Creta', 'HB20', 'Santa Fe', 'Elantra'],
  Jeep:            ['Renegade', 'Compass', 'Commander', 'Wrangler', 'Grand Cherokee'],
  Kia:             ['Sportage', 'Sorento', 'Cerato', 'Rio', 'Stinger'],
  'Land Rover':    ['Defender', 'Discovery', 'Range Rover', 'Evoque', 'Freelander'],
  'Mercedes-Benz': ['Clase A', 'Clase C', 'Clase E', 'GLC', 'GLE'],
  Nissan:          ['Frontier', 'Kicks', 'Versa', 'March', 'X-Trail'],
  Peugeot:         ['208', '308', '3008', '408', 'Partner'],
  Porsche:         ['911', 'Cayenne', 'Macan', 'Panamera', 'Taycan'],
  Renault:         ['Duster', 'Sandero', 'Logan', 'Captur', 'Kangoo'],
  Tesla:           ['Model 3', 'Model S', 'Model X', 'Model Y', 'Cybertruck'],
  Toyota:          ['Hilux', 'Corolla', 'SW4', 'Yaris', 'RAV4'],
  Volkswagen:      ['Amarok', 'Polo', 'Vento', 'Gol', 'Tiguan'],
  Volvo:           ['XC60', 'XC90', 'S60', 'V40', 'C40'],
  Other:           [],
}

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
  motor: '',
  chasis: '',
  mileage: 0,
  fuelType: 'gasoline',
  status: 'active',
  assignedDriverId: undefined,
  insuranceExpiration: '',
  technicalInspectionExpiration: '',
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
        motor: vehicle.motor,
        chasis: vehicle.chasis,
        mileage: vehicle.mileage,
        fuelType: vehicle.fuelType,
        status: vehicle.status,
        assignedDriverId: vehicle.assignedDriverId,
        insuranceExpiration: vehicle.insuranceExpiration,
        technicalInspectionExpiration: vehicle.technicalInspectionExpiration,
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
    setForm((prev) => ({
      ...prev,
      [key]: value,
      ...(key === 'brand' ? { model: '' } : {}),
    }))
    setErrors((prev) => ({ ...prev, [key]: undefined }))
  }

  function validate(): boolean {
    const newErrors: Partial<Record<keyof VehicleFormData, string>> = {}
    if (!form.brand) newErrors.brand = 'La marca es obligatoria'
    if (!form.model) newErrors.model = 'El modelo es obligatorio'
    if (!form.plateNumber) newErrors.plateNumber = 'La patente es obligatoria'
    if (!form.motor) newErrors.motor = 'El motor es obligatorio'
    if (!form.chasis) newErrors.chasis = 'El chasis es obligatorio'
    if (!form.insuranceExpiration) newErrors.insuranceExpiration = 'El vencimiento del seguro es obligatorio'
    if (!form.technicalInspectionExpiration) newErrors.technicalInspectionExpiration = 'El vencimiento de la VTV es obligatorio'
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
              <DialogTitle>{isEdit ? 'Editar Vehiculo' : 'Agregar Nuevo Vehiculo'}</DialogTitle>
              <DialogDescription className="mt-0.5">
                {isEdit ? 'Actualizar informacion del vehiculo' : 'Ingrese los datos del nuevo vehiculo'}
              </DialogDescription>
            </div>
          </div>
        </DialogHeader>

        <div className="px-6 py-4 space-y-6">
          {/* Basic Info */}
          <div>
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-3">Info del Vehiculo</p>
            <div className="grid grid-cols-2 gap-3">
              <FormField label="Marca" required error={errors.brand}>
                <Select value={form.brand} onValueChange={(v) => update('brand', v)}>
                  <SelectTrigger className={cn(errors.brand && 'border-fleet-danger/50')}>
                    <SelectValue placeholder="Seleccionar marca" />
                  </SelectTrigger>
                  <SelectContent>
                    {BRANDS.map((b) => <SelectItem key={b} value={b}>{b}</SelectItem>)}
                  </SelectContent>
                </Select>
              </FormField>

              <FormField label="Modelo" required error={errors.model}>
                {form.brand && form.brand !== 'Other' ? (
                  <Select
                    value={form.model}
                    onValueChange={(v) => update('model', v)}
                    disabled={!form.brand}
                  >
                    <SelectTrigger className={cn(errors.model && 'border-fleet-danger/50')}>
                      <SelectValue placeholder="Seleccionar modelo" />
                    </SelectTrigger>
                    <SelectContent>
                      {(MODELS_BY_BRAND[form.brand] ?? []).map((m) => (
                        <SelectItem key={m} value={m}>{m}</SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                ) : (
                  <Input
                    placeholder={form.brand ? 'Ingrese el modelo' : 'Seleccione una marca primero'}
                    value={form.model}
                    onChange={(e) => update('model', e.target.value)}
                    error={!!errors.model}
                    disabled={!form.brand}
                  />
                )}
              </FormField>

              <FormField label="Año">
                <Select value={String(form.year)} onValueChange={(v) => update('year', Number(v))}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    {YEARS.map((y) => <SelectItem key={y} value={String(y)}>{y}</SelectItem>)}
                  </SelectContent>
                </Select>
              </FormField>

              <FormField label="Combustible">
                <Select value={form.fuelType} onValueChange={(v) => update('fuelType', v as typeof form.fuelType)}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="gasoline">Nafta</SelectItem>
                    <SelectItem value="diesel">Diesel</SelectItem>
                    <SelectItem value="electric">Electrico</SelectItem>
                    <SelectItem value="hybrid">Hibrido</SelectItem>
                    <SelectItem value="cng">GNC</SelectItem>
                  </SelectContent>
                </Select>
              </FormField>
            </div>
          </div>

          <Separator />

          {/* Registration */}
          <div>
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-3">Registro</p>
            <div className="grid grid-cols-2 gap-3">
              <FormField label="Patente" required error={errors.plateNumber}>
                <Input
                  placeholder="ABC-1234"
                  value={form.plateNumber}
                  onChange={(e) => update('plateNumber', e.target.value.toUpperCase())}
                  className="font-mono"
                  error={!!errors.plateNumber}
                />
              </FormField>

              <FormField label="Motor" required error={errors.motor}>
                <Input
                  placeholder="Ej: 2.0 TSI 190cv"
                  value={form.motor}
                  onChange={(e) => update('motor', e.target.value.slice(0, 40))}
                  error={!!errors.motor}
                />
              </FormField>

              <FormField label="Chasis" required error={errors.chasis}>
                <Input
                  placeholder="Ej: WVWZZZ6RZNY12345"
                  value={form.chasis}
                  onChange={(e) => update('chasis', e.target.value.toUpperCase().slice(0, 40))}
                  className="font-mono text-[12px]"
                  error={!!errors.chasis}
                />
              </FormField>

              <FormField label="Estado">
                <Select value={form.status} onValueChange={(v) => update('status', v as typeof form.status)}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="active">Activo</SelectItem>
                    <SelectItem value="maintenance">En Reparacion</SelectItem>
                    <SelectItem value="inactive">Inactivo</SelectItem>
                    <SelectItem value="out_of_service">Fuera de Servicio</SelectItem>
                  </SelectContent>
                </Select>
              </FormField>

              <FormField label="Kilometraje (km)">
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
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-3">Documentos</p>
            <div className="grid grid-cols-2 gap-3">
              <FormField label="Vencimiento Seguro" required error={errors.insuranceExpiration}>
                <Input
                  type="date"
                  value={form.insuranceExpiration}
                  onChange={(e) => update('insuranceExpiration', e.target.value)}
                  error={!!errors.insuranceExpiration}
                />
              </FormField>

              <FormField label="Vencimiento VTV" required error={errors.technicalInspectionExpiration}>
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
            <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider mb-3">Datos Opcionales</p>
            <div className="grid grid-cols-2 gap-3">
              <FormField label="Conductor Asignado">
                <Select
                  value={form.assignedDriverId || 'none'}
                  onValueChange={(v) => update('assignedDriverId', v === 'none' ? undefined : v)}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Sin conductor asignado" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="none">Sin conductor asignado</SelectItem>
                    {MOCK_DRIVERS.filter((d) => d.status === 'active').map((d) => (
                      <SelectItem key={d.id} value={d.id}>{d.name}</SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </FormField>

              <FormField label="Fecha de Compra">
                <Input
                  type="date"
                  value={form.purchaseDate}
                  onChange={(e) => update('purchaseDate', e.target.value)}
                />
              </FormField>

              <FormField label="Costo de Compra ($)">
                <Input
                  type="number"
                  placeholder="0"
                  value={form.purchaseCost || ''}
                  onChange={(e) => update('purchaseCost', Number(e.target.value) || undefined)}
                />
              </FormField>
            </div>

            <div className="mt-3">
              <FormField label="Notas">
                <Textarea
                  placeholder="Notas adicionales sobre este vehiculo…"
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
            Cancelar
          </Button>
          <Button onClick={handleSubmit} disabled={saving}>
            {saving ? (
              <span className="flex items-center gap-2">
                <motion.div
                  animate={{ rotate: 360 }}
                  transition={{ duration: 0.8, repeat: Infinity, ease: 'linear' }}
                  className="w-3.5 h-3.5 border-2 border-white/30 border-t-white rounded-full"
                />
                Guardando…
              </span>
            ) : isEdit ? 'Guardar Cambios' : 'Agregar Vehiculo'}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
