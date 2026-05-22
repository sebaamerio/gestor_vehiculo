import { motion } from 'framer-motion'
import { LucideIcon } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { cn } from '@/lib/utils'

interface EmptyStateProps {
  icon: LucideIcon
  title: string
  description: string
  action?: {
    label: string
    onClick: () => void
  }
  className?: string
}

export function EmptyState({ icon: Icon, title, description, action, className }: EmptyStateProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      className={cn('flex flex-col items-center justify-center py-20 px-6 text-center', className)}
    >
      <div className="relative mb-5">
        <div className="w-16 h-16 rounded-2xl bg-surface-elevated border border-subtle flex items-center justify-center">
          <Icon className="w-7 h-7 text-text-muted" />
        </div>
        <div className="absolute inset-0 rounded-2xl bg-gradient-radial from-accent/5 to-transparent -z-10 scale-150" />
      </div>

      <h3 className="text-[15px] font-semibold text-text-primary mb-1.5">{title}</h3>
      <p className="text-[13px] text-text-muted max-w-xs leading-relaxed mb-6">{description}</p>

      {action && (
        <Button onClick={action.onClick} size="sm">
          {action.label}
        </Button>
      )}
    </motion.div>
  )
}
