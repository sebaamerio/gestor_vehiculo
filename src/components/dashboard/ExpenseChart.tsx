'use client'

import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from 'recharts'
import { MONTHLY_EXPENSE_DATA } from '@/lib/data'
import { formatCurrency } from '@/lib/utils'

const CustomTooltip = ({
  active,
  payload,
  label,
}: {
  active?: boolean
  payload?: { name: string; value: number; color: string }[]
  label?: string
}) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-surface-overlay border border-subtle rounded-xl px-4 py-3 shadow-elevated">
        <p className="text-[12px] font-semibold text-text-primary mb-2">{label}</p>
        {payload.map((entry) => (
          <div key={entry.name} className="flex items-center justify-between gap-6">
            <div className="flex items-center gap-1.5">
              <div className="w-2 h-2 rounded-full" style={{ backgroundColor: entry.color }} />
              <span className="text-[11px] text-text-muted capitalize">{entry.name}</span>
            </div>
            <span className="text-[12px] font-semibold text-text-primary">
              {formatCurrency(entry.value)}
            </span>
          </div>
        ))}
      </div>
    )
  }
  return null
}

export function ExpenseChart() {
  const total = MONTHLY_EXPENSE_DATA.reduce(
    (acc, d) => ({ fuel: acc.fuel + d.fuel, maintenance: acc.maintenance + d.maintenance }),
    { fuel: 0, maintenance: 0 }
  )

  return (
    <div className="bg-surface rounded-2xl border border-subtle shadow-card p-6">
      <div className="flex items-start justify-between mb-6">
        <div>
          <h3 className="text-[15px] font-semibold text-text-primary">Tendencia de Gastos</h3>
          <p className="text-[12px] text-text-muted mt-0.5">Ultimos 6 meses</p>
        </div>
        <div className="flex gap-4">
          <div className="text-right">
            <div className="text-[11px] text-text-muted">Combustible</div>
            <div className="text-[14px] font-semibold text-blue-400">{formatCurrency(total.fuel)}</div>
          </div>
          <div className="text-right">
            <div className="text-[11px] text-text-muted">Reparaciones</div>
            <div className="text-[14px] font-semibold text-fleet-maintenance">{formatCurrency(total.maintenance)}</div>
          </div>
        </div>
      </div>

      <div className="h-52">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={MONTHLY_EXPENSE_DATA} margin={{ top: 4, right: 4, left: -20, bottom: 0 }}>
            <defs>
              <linearGradient id="fuelGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#3B82F6" stopOpacity={0.2} />
                <stop offset="95%" stopColor="#3B82F6" stopOpacity={0} />
              </linearGradient>
              <linearGradient id="maintenanceGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#F59E0B" stopOpacity={0.2} />
                <stop offset="95%" stopColor="#F59E0B" stopOpacity={0} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" vertical={false} />
            <XAxis
              dataKey="month"
              tick={{ fill: 'rgba(255,255,255,0.35)', fontSize: 11 }}
              axisLine={false}
              tickLine={false}
            />
            <YAxis
              tick={{ fill: 'rgba(255,255,255,0.35)', fontSize: 11 }}
              axisLine={false}
              tickLine={false}
              tickFormatter={(v) => `$${v / 1000}k`}
            />
            <Tooltip content={<CustomTooltip />} cursor={{ stroke: 'rgba(255,255,255,0.06)', strokeWidth: 1 }} />
            <Area
              type="monotone"
              dataKey="fuel"
              name="Combustible"
              stroke="#3B82F6"
              strokeWidth={2}
              fill="url(#fuelGradient)"
              dot={false}
              activeDot={{ r: 4, fill: '#3B82F6', strokeWidth: 0 }}
            />
            <Area
              type="monotone"
              dataKey="maintenance"
              name="Reparaciones"
              stroke="#F59E0B"
              strokeWidth={2}
              fill="url(#maintenanceGradient)"
              dot={false}
              activeDot={{ r: 4, fill: '#F59E0B', strokeWidth: 0 }}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
