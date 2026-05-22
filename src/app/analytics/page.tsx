'use client'

import { AppShell } from '@/components/layout/AppShell'
import { PageHeader } from '@/components/shared/PageHeader'
import { ExpenseChart } from '@/components/dashboard/ExpenseChart'
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip,
  ResponsiveContainer, PieChart, Pie, Cell
} from 'recharts'
import { BarChart3, TrendingUp, Fuel, Car, DollarSign } from 'lucide-react'
import { MOCK_VEHICLES, MOCK_MAINTENANCE, MOCK_FUEL_LOGS } from '@/lib/data'
import { formatCurrency, formatMileage } from '@/lib/utils'
import { motion } from 'framer-motion'
import { cn } from '@/lib/utils'

const FUEL_DISTRIBUTION = [
  { name: 'Gasoline', value: MOCK_VEHICLES.filter(v => v.fuelType === 'gasoline').length, color: '#F97316' },
  { name: 'Diesel', value: MOCK_VEHICLES.filter(v => v.fuelType === 'diesel').length, color: '#60A5FA' },
  { name: 'Electric', value: MOCK_VEHICLES.filter(v => v.fuelType === 'electric').length, color: '#22D3EE' },
  { name: 'Hybrid', value: MOCK_VEHICLES.filter(v => v.fuelType === 'hybrid').length, color: '#34D399' },
].filter(d => d.value > 0)

const MILEAGE_BY_BRAND = Object.entries(
  MOCK_VEHICLES.reduce((acc, v) => {
    acc[v.brand] = (acc[v.brand] || 0) + v.mileage
    return acc
  }, {} as Record<string, number>)
).map(([brand, mileage]) => ({ brand, mileage }))
 .sort((a, b) => b.mileage - a.mileage)
 .slice(0, 6)

const MAINTENANCE_BY_TYPE = Object.entries(
  MOCK_MAINTENANCE.reduce((acc, m) => {
    acc[m.type] = (acc[m.type] || 0) + m.cost
    return acc
  }, {} as Record<string, number>)
).map(([type, cost]) => ({ type: type.replace('_', ' '), cost }))
 .sort((a, b) => b.cost - a.cost)

function CustomTooltip({ active, payload, label }: { active?: boolean; payload?: { value: number }[]; label?: string }) {
  if (active && payload && payload.length) {
    return (
      <div className="bg-surface-overlay border border-subtle rounded-xl px-3 py-2 shadow-elevated">
        <p className="text-[11px] text-text-muted">{label}</p>
        <p className="text-[13px] font-semibold text-text-primary">{formatCurrency(payload[0].value)}</p>
      </div>
    )
  }
  return null
}

function MileageTooltip({ active, payload, label }: { active?: boolean; payload?: { value: number }[]; label?: string }) {
  if (active && payload && payload.length) {
    return (
      <div className="bg-surface-overlay border border-subtle rounded-xl px-3 py-2 shadow-elevated">
        <p className="text-[11px] text-text-muted">{label}</p>
        <p className="text-[13px] font-semibold text-text-primary">{formatMileage(payload[0].value)}</p>
      </div>
    )
  }
  return null
}

export default function AnalyticsPage() {
  const totalFuelCost = MOCK_FUEL_LOGS.reduce((s, f) => s + f.cost, 0)
  const totalMaintenanceCost = MOCK_MAINTENANCE.reduce((s, m) => s + m.cost, 0)
  const avgMileage = MOCK_VEHICLES.reduce((s, v) => s + v.mileage, 0) / MOCK_VEHICLES.length

  return (
    <AppShell>
      <div className="px-6 md:px-8 py-8 max-w-[1400px] mx-auto">
        <PageHeader
          title="Analytics"
          description="Fleet performance and cost insights"
          icon={BarChart3}
        />

        {/* KPI row */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {[
            { icon: Fuel, label: 'Total Fuel Cost', value: formatCurrency(totalFuelCost), color: 'text-blue-400', bg: 'bg-blue-500/10' },
            { icon: DollarSign, label: 'Maintenance Cost', value: formatCurrency(totalMaintenanceCost), color: 'text-fleet-maintenance', bg: 'bg-fleet-maintenance-bg' },
            { icon: Car, label: 'Avg Mileage', value: formatMileage(Math.round(avgMileage)), color: 'text-accent-light', bg: 'bg-accent/10' },
            { icon: TrendingUp, label: 'Total Fleet Cost', value: formatCurrency(totalFuelCost + totalMaintenanceCost), color: 'text-fleet-active', bg: 'bg-fleet-active-bg' },
          ].map((kpi, i) => (
            <motion.div
              key={kpi.label}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.05 }}
              className="bg-surface rounded-xl border border-subtle p-4"
            >
              <div className={cn('w-8 h-8 rounded-lg flex items-center justify-center mb-3', kpi.bg)}>
                <kpi.icon className={cn('w-4 h-4', kpi.color)} />
              </div>
              <div className="text-[11px] text-text-muted mb-0.5">{kpi.label}</div>
              <div className="text-lg font-bold text-text-primary">{kpi.value}</div>
            </motion.div>
          ))}
        </div>

        {/* Charts grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
          {/* Expense trends */}
          <ExpenseChart />

          {/* Fuel type distribution */}
          <div className="bg-surface rounded-2xl border border-subtle p-6">
            <h3 className="text-[15px] font-semibold text-text-primary mb-1">Fuel Type Distribution</h3>
            <p className="text-[12px] text-text-muted mb-5">By vehicle count</p>
            <div className="flex items-center gap-6">
              <div className="w-44 h-44 flex-shrink-0">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie data={FUEL_DISTRIBUTION} cx="50%" cy="50%" innerRadius={45} outerRadius={65} paddingAngle={2} dataKey="value" strokeWidth={0}>
                      {FUEL_DISTRIBUTION.map((entry, index) => (
                        <Cell key={index} fill={entry.color} opacity={0.85} />
                      ))}
                    </Pie>
                  </PieChart>
                </ResponsiveContainer>
              </div>
              <div className="space-y-3 flex-1">
                {FUEL_DISTRIBUTION.map((item) => (
                  <div key={item.name} className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <div className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: item.color }} />
                      <span className="text-[13px] text-text-secondary">{item.name}</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-[13px] font-semibold text-text-primary">{item.value}</span>
                      <span className="text-[11px] text-text-disabled">
                        {Math.round((item.value / MOCK_VEHICLES.length) * 100)}%
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Mileage by brand */}
          <div className="bg-surface rounded-2xl border border-subtle p-6">
            <h3 className="text-[15px] font-semibold text-text-primary mb-1">Fleet Mileage by Brand</h3>
            <p className="text-[12px] text-text-muted mb-5">Cumulative kilometers</p>
            <div className="h-52">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={MILEAGE_BY_BRAND} margin={{ top: 4, right: 4, left: -20, bottom: 0 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" vertical={false} />
                  <XAxis dataKey="brand" tick={{ fill: 'rgba(255,255,255,0.35)', fontSize: 11 }} axisLine={false} tickLine={false} />
                  <YAxis tick={{ fill: 'rgba(255,255,255,0.35)', fontSize: 10 }} axisLine={false} tickLine={false} tickFormatter={(v) => `${v / 1000}k`} />
                  <Tooltip content={<MileageTooltip />} cursor={{ fill: 'rgba(255,255,255,0.04)' }} />
                  <Bar dataKey="mileage" fill="#7C3AED" opacity={0.8} radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Maintenance by type */}
          <div className="bg-surface rounded-2xl border border-subtle p-6">
            <h3 className="text-[15px] font-semibold text-text-primary mb-1">Maintenance Costs by Type</h3>
            <p className="text-[12px] text-text-muted mb-5">Total spending per service type</p>
            <div className="h-52">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={MAINTENANCE_BY_TYPE} layout="vertical" margin={{ top: 4, right: 4, left: 40, bottom: 0 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" horizontal={false} />
                  <XAxis type="number" tick={{ fill: 'rgba(255,255,255,0.35)', fontSize: 10 }} axisLine={false} tickLine={false} tickFormatter={(v) => `$${v}`} />
                  <YAxis type="category" dataKey="type" tick={{ fill: 'rgba(255,255,255,0.35)', fontSize: 10 }} axisLine={false} tickLine={false} width={80} />
                  <Tooltip content={<CustomTooltip />} cursor={{ fill: 'rgba(255,255,255,0.04)' }} />
                  <Bar dataKey="cost" fill="#F59E0B" opacity={0.8} radius={[0, 4, 4, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>
      </div>
    </AppShell>
  )
}
