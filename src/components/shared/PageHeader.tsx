import { motion } from 'framer-motion'
import { LucideIcon } from 'lucide-react'
import { cn } from '@/lib/utils'

interface PageHeaderProps {
  title: string
  description?: string
  icon?: LucideIcon
  actions?: React.ReactNode
  className?: string
}

export function PageHeader({ title, description, icon: Icon, actions, className }: PageHeaderProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: -6 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.2 }}
      className={cn('flex items-start justify-between gap-4 mb-8', className)}
    >
      <div className="flex items-center gap-3 min-w-0">
        {Icon && (
          <div className="w-9 h-9 rounded-xl bg-accent/10 border border-accent/20 flex items-center justify-center flex-shrink-0">
            <Icon className="w-4.5 h-4.5 text-accent-light" />
          </div>
        )}
        <div className="min-w-0">
          <h1 className="text-xl font-semibold text-text-primary tracking-tight">{title}</h1>
          {description && (
            <p className="text-[13px] text-text-muted mt-0.5">{description}</p>
          )}
        </div>
      </div>

      {actions && <div className="flex items-center gap-2 flex-shrink-0">{actions}</div>}
    </motion.div>
  )
}
