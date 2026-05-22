'use client'

import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts'
import { motion } from 'framer-motion'
import { cn } from '@/lib/utils'

interface FleetStatusCardProps {
  stats: {
    activeVehicles: number
    inMaintenance: number
    outOfService: number
    inactive: number
    totalVehicles: number
  }
}

const STATUS_DATA_CONFIG = [
  { key: 'activeVehicles', label: 'Active', color: '#10B981', bg: 'bg-fleet-active-bg', text: 'text-fleet-active' },
  { key: 'inMaintenance', label: 'Maintenance', color: '#F59E0B', bg: 'bg-fleet-maintenance-bg', text: 'text-fleet-maintenance' },
  { key: 'inactive', label: 'Inactive', color: '#6B7280', bg: 'bg-fleet-inactive-bg', text: 'text-fleet-inactive' },
  { key: 'outOfService', label: 'Out of Service', color: '#EF4444', bg: 'bg-fleet-danger-bg', text: 'text-fleet-danger' },
]

const CustomTooltip = ({ active, payload }: { active?: boolean; payload?: { name: string; value: number }[] }) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-surface-overlay border border-subtle rounded-xl px-3 py-2 shadow-elevated">
        <p className="text-[12px] font-medium text-text-primary">{payload[0].name}</p>
        <p className="text-[11px] text-text-muted">{payload[0].value} vehicles</p>
      </div>
    )
  }
  return null
}

export function FleetStatusCard({ stats }: FleetStatusCardProps) {
  const data = STATUS_DATA_CONFIG.map((config) => ({
    name: config.label,
    value: stats[config.key as keyof typeof stats] as number,
    color: config.color,
  })).filter((d) => d.value > 0)

  const activePercent = Math.round((stats.activeVehicles / stats.totalVehicles) * 100)

  return (
    <div className="bg-surface rounded-2xl border border-subtle shadow-card p-6">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h3 className="text-[15px] font-semibold text-text-primary">Fleet Status</h3>
          <p className="text-[12px] text-text-muted mt-0.5">{stats.totalVehicles} total vehicles</p>
        </div>
        <div className="px-2.5 py-1 rounded-lg bg-fleet-active-bg border border-fleet-active-border">
          <span className="text-[12px] font-semibold text-fleet-active">{activePercent}% active</span>
        </div>
      </div>

      <div className="flex items-center gap-6">
        {/* Donut Chart */}
        <div className="relative w-32 h-32 flex-shrink-0">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={data}
                cx="50%"
                cy="50%"
                innerRadius={40}
                outerRadius={60}
                paddingAngle={2}
                dataKey="value"
                strokeWidth={0}
              >
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} opacity={0.85} />
                ))}
              </Pie>
              <Tooltip content={<CustomTooltip />} />
            </PieChart>
          </ResponsiveContainer>
          {/* Center text */}
          <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
            <span className="text-xl font-bold text-text-primary">{stats.activeVehicles}</span>
            <span className="text-[10px] text-text-muted font-medium">online</span>
          </div>
        </div>

        {/* Legend */}
        <div className="flex-1 space-y-2.5">
          {STATUS_DATA_CONFIG.map((config) => {
            const value = stats[config.key as keyof typeof stats] as number
            const pct = stats.totalVehicles > 0 ? Math.round((value / stats.totalVehicles) * 100) : 0
            return (
              <motion.div
                key={config.key}
                initial={{ opacity: 0, x: 8 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.25 }}
                className="flex items-center justify-between gap-3"
              >
                <div className="flex items-center gap-2 min-w-0">
                  <div className="w-2 h-2 rounded-full flex-shrink-0" style={{ backgroundColor: config.color }} />
                  <span className="text-[12px] text-text-muted truncate">{config.label}</span>
                </div>
                <div className="flex items-center gap-2 flex-shrink-0">
                  <span className="text-[12px] font-semibold text-text-primary">{value}</span>
                  <span className="text-[11px] text-text-disabled w-7 text-right">{pct}%</span>
                </div>
              </motion.div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
