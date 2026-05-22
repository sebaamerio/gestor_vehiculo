'use client'

import { AppShell } from '@/components/layout/AppShell'
import { PageHeader } from '@/components/shared/PageHeader'
import { FileText, Shield, AlertTriangle, CheckCircle2 } from 'lucide-react'
import { MOCK_DOCUMENTS, MOCK_VEHICLES } from '@/lib/data'
import { formatDate, daysUntilExpiry, getExpiryStatus, formatCurrency } from '@/lib/utils'
import { motion } from 'framer-motion'
import Link from 'next/link'
import { cn } from '@/lib/utils'

export default function DocumentsPage() {
  const withExpiry = MOCK_DOCUMENTS.map((doc) => ({
    ...doc,
    expiryStatus: getExpiryStatus(doc.expirationDate),
    daysLeft: daysUntilExpiry(doc.expirationDate),
  })).sort((a, b) => a.daysLeft - b.daysLeft)

  const critical = withExpiry.filter((d) => d.expiryStatus === 'expired' || d.expiryStatus === 'critical')
  const warning = withExpiry.filter((d) => d.expiryStatus === 'warning')
  const ok = withExpiry.filter((d) => d.expiryStatus === 'ok')

  function ExpiryChip({ status, days }: { status: string; days: number }) {
    const config = {
      expired: 'bg-fleet-danger-bg text-fleet-danger border-fleet-danger-border',
      critical: 'bg-fleet-danger-bg text-fleet-danger border-fleet-danger-border',
      warning: 'bg-fleet-maintenance-bg text-fleet-maintenance border-fleet-maintenance-border',
      ok: 'bg-fleet-active-bg text-fleet-active border-fleet-active-border',
    }[status] || 'bg-surface-elevated text-text-muted border-subtle'

    return (
      <span className={cn('text-[11px] font-medium px-2.5 py-1 rounded-full border', config)}>
        {status === 'expired' ? 'Expired' : status === 'ok' ? 'Valid' : `${days}d left`}
      </span>
    )
  }

  function DocSection({ title, items, icon: Icon, iconClass }: { title: string; items: typeof withExpiry; icon: typeof FileText; iconClass: string }) {
    if (items.length === 0) return null

    return (
      <div className="mb-8">
        <div className="flex items-center gap-2 mb-4">
          <Icon className={cn('w-3.5 h-3.5', iconClass)} />
          <p className="text-[11px] font-semibold text-text-muted uppercase tracking-wider">
            {title} ({items.length})
          </p>
        </div>
        <div className="space-y-2">
          {items.map((doc, i) => {
            const vehicle = MOCK_VEHICLES.find((v) => v.id === doc.vehicleId)
            return (
              <motion.div
                key={doc.id}
                initial={{ opacity: 0, y: 4 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.03 }}
                className="bg-surface rounded-xl border border-subtle p-4 flex items-center gap-4 hover:border-subtle-hover transition-colors"
              >
                <div className="w-9 h-9 rounded-xl bg-accent/10 border border-accent/20 flex items-center justify-center flex-shrink-0">
                  <FileText className="w-4 h-4 text-accent-light" />
                </div>

                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2">
                    <span className="text-[14px] font-semibold text-text-primary">{doc.name}</span>
                    <span className="text-[11px] capitalize text-text-muted bg-surface-elevated px-1.5 py-0.5 rounded">
                      {doc.type}
                    </span>
                  </div>
                  <div className="flex items-center gap-3 mt-1 text-[12px] text-text-muted">
                    {vehicle && (
                      <Link href={`/vehicles/${vehicle.id}`} className="text-accent-light hover:text-accent transition-colors">
                        {vehicle.brand} {vehicle.model}
                      </Link>
                    )}
                    {vehicle && <span className="text-text-disabled">·</span>}
                    {doc.provider && <span>{doc.provider}</span>}
                    <span className="text-text-disabled">·</span>
                    <span>Expires {formatDate(doc.expirationDate)}</span>
                    {doc.cost && (
                      <>
                        <span className="text-text-disabled">·</span>
                        <span>{formatCurrency(doc.cost)}</span>
                      </>
                    )}
                  </div>
                </div>

                <ExpiryChip status={doc.expiryStatus} days={doc.daysLeft} />
              </motion.div>
            )
          })}
        </div>
      </div>
    )
  }

  return (
    <AppShell>
      <div className="px-6 md:px-8 py-8 max-w-[1200px] mx-auto">
        <PageHeader
          title="Documents"
          description={`${MOCK_DOCUMENTS.length} documents · ${critical.length} need attention`}
          icon={FileText}
        />

        {/* Summary */}
        <div className="grid grid-cols-3 gap-4 mb-8">
          {[
            { label: 'Expired / Critical', value: critical.length, icon: AlertTriangle, color: 'text-fleet-danger', bg: 'bg-fleet-danger-bg' },
            { label: 'Expiring Soon', value: warning.length, icon: Shield, color: 'text-fleet-maintenance', bg: 'bg-fleet-maintenance-bg' },
            { label: 'Valid', value: ok.length, icon: CheckCircle2, color: 'text-fleet-active', bg: 'bg-fleet-active-bg' },
          ].map((stat, i) => (
            <motion.div
              key={stat.label}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.05 }}
              className="bg-surface rounded-xl border border-subtle p-4 flex items-center gap-3"
            >
              <div className={cn('w-9 h-9 rounded-xl flex items-center justify-center', stat.bg)}>
                <stat.icon className={cn('w-4 h-4', stat.color)} />
              </div>
              <div>
                <div className="text-[11px] text-text-muted">{stat.label}</div>
                <div className="text-xl font-bold text-text-primary">{stat.value}</div>
              </div>
            </motion.div>
          ))}
        </div>

        <DocSection title="Needs Attention" items={critical} icon={AlertTriangle} iconClass="text-fleet-danger" />
        <DocSection title="Expiring Soon" items={warning} icon={Shield} iconClass="text-fleet-maintenance" />
        <DocSection title="Valid Documents" items={ok} icon={CheckCircle2} iconClass="text-fleet-active" />
      </div>
    </AppShell>
  )
}
