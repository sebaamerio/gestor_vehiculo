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
import { Wrench } from 'lucide-react'
import { cn } from '@/lib/utils'
import type { ReparacionFormData, ReparacionRecord, ReparacionType } from '@/lib/types'

interface ReparacionModalProps {
  open: boolean
  onClose: () => void
  vehicleMileage: number
  record?: ReparacionRecord
  onSave: (data: ReparacionFormData) => void
}

const TODAY = new Date().toISOString().split('T')[0]

function deriveStatus(deliveryDate: string, markedComplete: boolean): 'completed' | 'scheduled' | 'overdue' {
  if (markedComplete) return 'completed'
  if (deliveryDate && deliveryDate < TODAY) return 'overdue'
  return 'scheduled'
}

const EMPTY_FORM: ReparacionFormData = {
  type: 'oil_change',
  description: '',
  date: TODAY,
  cost: 0,
  mileage: 0,
  provider: '',
  status: 'scheduled',
}

const TYPE_OPTIONS: { value: ReparacionType; label: string }[] = [
  { value: 'oil_change', label: 'Cambio de Aceite' },
  { value: 'tire_rotation', label: 'Rotacion de Neumaticos' },
  { value: 'brake_inspection', label: 'Revision de Frenos' },
  { value: 'air_filter', label: 'Filtro de Aire' },
  { value: 'transmission', label: 'Transmision' },
  { value: 'battery', label: 'Bateria' },
  { value: 'coolant', label: 'Refrigerante' },
  { value: 'alignment', label: 'Alineacion' },
  { value: 'general_inspection', label: 'Inspeccion General' },
  { value: 'other', label: 'Otro' },
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

export function ReparacionModal({ open, onClose, vehicleMileage, record, onSave }: ReparacionModalProps) {
  const isEditing = !!record
  const [form, setForm] = useState<ReparacionFormData>({ ...EMPTY_FORM, mileage: vehicleMileage })
  const [deliveryDate, setDeliveryDate] = useState('')
  const [markedComplete, setMarkedComplete] = useState(false)
  const [errors, setErrors] = useState<Partial<Record<keyof ReparacionFormData, string>>>({})
  const [saving, setSaving] = useState(false)

  const derivedStatus = deriveStatus(deliveryDate, markedComplete)

  useEffect(() => {
    if (open) {
      if (record) {
        setForm({
          type: record.type,
          description: record.description,
          date: record.date,
          cost: record.cost,
          mileage: record.mileage,
          provider: record.provider ?? '',
          status: record.status,
        })
        setDeliveryDate(record.deliveryDate ?? '')
        setMarkedComplete(record.status === 'completed')
      } else {
        setForm({ ...EMPTY_FORM, mileage: vehicleMileage })
        setDeliveryDate('')
        setMarkedComplete(false)
      }
      setErrors({})
    }
  }, [open, vehicleMileage, record])

  function update<K extends keyof ReparacionFormData>(key: K, value: ReparacionFormData[K]) {
    setForm((prev) => ({ ...prev, [key]: value }))
    setErrors((prev) => ({ ...prev, [key]: undefined }))
  }

  function validate(): boolean {
    const newErrors: Partial<Record<keyof ReparacionFormData, string>> = {}
    if (!form.date) newErrors.date = 'La fecha es obligatoria'
    if (form.mileage <= 0) newErrors.mileage = 'El kilometraje debe ser mayor a 0'
    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  async function handleSubmit() {
    if (!validate()) return
    setSaving(true)
    await new Promise((r) => setTimeout(r, 500))
    onSave({
      ...form,
      status: derivedStatus,
      deliveryDate: deliveryDate || undefined,
      provider: form.provider?.trim() || undefined,
    })
    setSaving(false)
    onClose()
  }

  return (
    <Dialog open={open} onOpenChange={(o) => !o && onClose()}>
      <DialogContent className="max-w-xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-fleet-maintenance-bg border border-fleet-maintenance-border flex items-center justify-center flex-shrink-0">
              <Wrench className="w-4 h-4 text-fleet-maintenance" />
            </div>
            <div>
              <DialogTitle>{isEditing ? 'Editar Reparacion' : 'Agregar Reparacion'}</DialogTitle>
              <DialogDescription className="mt-0.5">
                {isEditing ? 'Modificar los datos del registro' : 'Registrar un nuevo servicio o reparacion'}
              </DialogDescription>
            </div>
          </div>
        </DialogHeader>

        <div className="px-6 py-4 space-y-5">
          {/* Fila 1: Tipo | Fecha */}
          <div className="grid grid-cols-2 gap-3">
            <FormField label="Tipo" required>
              <Select value={form.type} onValueChange={(v) => update('type', v as ReparacionType)}>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  {TYPE_OPTIONS.map((opt) => (
                    <SelectItem key={opt.value} value={opt.value}>{opt.label}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </FormField>

            <FormField label="Fecha" required error={errors.date}>
              <Input
                type="date"
                value={form.date}
                onChange={(e) => update('date', e.target.value)}
                error={!!errors.date}
              />
            </FormField>
          </div>

          {/* Fila 2: Fecha Entrega | Estado */}
          <div className="grid grid-cols-2 gap-3">
            <FormField label="Fecha de Entrega">
              <Input
                type="date"
                value={deliveryDate}
                onChange={(e) => setDeliveryDate(e.target.value)}
              />
            </FormField>

            <div className="flex flex-col justify-end gap-2 pb-1">
              <span className={cn(
                'text-[11px] font-semibold px-2.5 py-1 rounded-full self-start',
                derivedStatus === 'completed' ? 'bg-fleet-active-bg text-fleet-active' :
                derivedStatus === 'overdue'   ? 'bg-fleet-danger-bg text-fleet-danger' :
                                                'bg-fleet-maintenance-bg text-fleet-maintenance'
              )}>
                {derivedStatus === 'completed' ? 'Completado' : derivedStatus === 'overdue' ? 'Vencido' : 'Programado'}
              </span>
              <label className="flex items-center gap-2 cursor-pointer select-none">
                <input
                  type="checkbox"
                  checked={markedComplete}
                  onChange={(e) => {
                    setMarkedComplete(e.target.checked)
                    if (e.target.checked && !deliveryDate) setDeliveryDate(TODAY)
                  }}
                  className="w-3.5 h-3.5 accent-accent rounded"
                />
                <span className="text-[12px] text-text-secondary">Marcar completado</span>
              </label>
            </div>
          </div>

          {/* Fila 3: Descripcion (opcional) */}
          <FormField label="Descripcion">
            <Textarea
              placeholder="Ej: Cambio de aceite sintético 5W-30 + filtro"
              value={form.description}
              onChange={(e) => update('description', e.target.value)}
              rows={2}
            />
          </FormField>

          {/* Fila 4: resto de campos */}
          <div className="grid grid-cols-2 gap-3">
            <FormField label="Kilometraje (km)" required error={errors.mileage}>
              <Input
                type="number"
                placeholder="0"
                value={form.mileage || ''}
                onChange={(e) => update('mileage', Number(e.target.value))}
                error={!!errors.mileage}
              />
            </FormField>

            <FormField label="Costo ($)">
              <Input
                type="number"
                placeholder="0"
                value={form.cost || ''}
                onChange={(e) => update('cost', Number(e.target.value))}
              />
            </FormField>

            <FormField label="Proveedor">
              <Input
                placeholder="Ej: Taller El Rápido"
                value={form.provider}
                onChange={(e) => update('provider', e.target.value)}
              />
            </FormField>
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
            ) : isEditing ? 'Guardar Cambios' : 'Agregar Reparacion'}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
