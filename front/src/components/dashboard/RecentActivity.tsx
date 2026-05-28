'use client'

import { motion } from 'framer-motion'
import { Wrench, Fuel, FileText, Car, UserCheck, Clock } from 'lucide-react'
import { cn, formatDate } from '@/lib/utils'

interface Activity {
  id: string
  type: 'maintenance' | 'fuel' | 'document' | 'vehicle' | 'driver'
  title: string
  description: string
  time: string
  vehicleLabel?: string
}

const RECENT_ACTIVITIES: Activity[] = [
  {
    id: 'act1',
    type: 'maintenance',
    title: 'Cambio de Frenos',
    description: 'Ford Transit — servicio completado',
    time: '2025-04-15T11:00:00Z',
    vehicleLabel: 'DEF-9012',
  },
  {
    id: 'act2',
    type: 'fuel',
    title: 'Carga de Combustible',
    description: 'BMW 5 Series — 48L en Mobil',
    time: '2025-04-15T09:20:00Z',
    vehicleLabel: 'ABC-1234',
  },
  {
    id: 'act3',
    type: 'document',
    title: 'Seguro Renovado',
    description: 'Honda CR-V — Allianz, vigente hasta Feb 2026',
    time: '2025-04-14T14:00:00Z',
    vehicleLabel: 'PQR-5678',
  },
  {
    id: 'act4',
    type: 'vehicle',
    title: 'Vehiculo Agregado',
    description: 'Tesla Model 3 agregado a la flota',
    time: '2025-04-12T10:00:00Z',
    vehicleLabel: 'GHI-3456',
  },
  {
    id: 'act5',
    type: 'driver',
    title: 'Conductor Asignado',
    description: 'Ava Thompson → Toyota Camry',
    time: '2025-04-11T16:30:00Z',
  },
  {
    id: 'act6',
    type: 'maintenance',
    title: 'Cambio de Aceite',
    description: 'Toyota Camry — servicio programado',
    time: '2025-04-05T09:00:00Z',
    vehicleLabel: 'XYZ-5678',
  },
]

const ACTIVITY_CONFIG = {
  maintenance: { icon: Wrench, bg: 'bg-fleet-maintenance-bg', color: 'text-fleet-maintenance' },
  fuel: { icon: Fuel, bg: 'bg-blue-500/10', color: 'text-blue-400' },
  document: { icon: FileText, bg: 'bg-accent/10', color: 'text-accent-light' },
  vehicle: { icon: Car, bg: 'bg-fleet-active-bg', color: 'text-fleet-active' },
  driver: { icon: UserCheck, bg: 'bg-purple-500/10', color: 'text-purple-400' },
}

function timeAgo(dateStr: string): string {
  const date = new Date(dateStr)
  const now = new Date()
  const diff = Math.floor((now.getTime() - date.getTime()) / 1000)

  if (diff < 60) return 'Ahora mismo'
  if (diff < 3600) return `${Math.floor(diff / 60)}min atras`
  if (diff < 86400) return `${Math.floor(diff / 3600)}h atras`
  if (diff < 604800) return `${Math.floor(diff / 86400)}d atras`
  return formatDate(dateStr, 'MMM d')
}

export function RecentActivity() {
  return (
    <div className="bg-surface rounded-2xl border border-subtle shadow-card p-6">
      <div className="flex items-center justify-between mb-5">
        <div>
          <h3 className="text-[15px] font-semibold text-text-primary">Actividad Reciente</h3>
          <p className="text-[12px] text-text-muted mt-0.5">Ultimas actualizaciones de la flota</p>
        </div>
        <Clock className="w-4 h-4 text-text-muted" />
      </div>

      <div className="space-y-1">
        {RECENT_ACTIVITIES.map((activity, i) => {
          const config = ACTIVITY_CONFIG[activity.type]
          const Icon = config.icon

          return (
            <motion.div
              key={activity.id}
              initial={{ opacity: 0, y: 6 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.04 }}
              className="group flex items-start gap-3 p-2.5 rounded-xl hover:bg-surface-elevated transition-colors cursor-default"
            >
              <div className={cn('w-7 h-7 rounded-lg flex items-center justify-center flex-shrink-0 mt-0.5', config.bg)}>
                <Icon className={cn('w-3.5 h-3.5', config.color)} />
              </div>
              <div className="flex-1 min-w-0">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[13px] font-medium text-text-primary truncate">{activity.title}</span>
                  <span className="text-[11px] text-text-muted flex-shrink-0">{timeAgo(activity.time)}</span>
                </div>
                <p className="text-[12px] text-text-muted mt-0.5">{activity.description}</p>
              </div>
              {activity.vehicleLabel && (
                <span className="plate text-[10px] text-text-disabled bg-subtle px-1.5 py-0.5 rounded flex-shrink-0">
                  {activity.vehicleLabel}
                </span>
              )}
            </motion.div>
          )
        })}
      </div>
    </div>
  )
}
