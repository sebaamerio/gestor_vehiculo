import * as React from 'react'
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const badgeVariants = cva(
  'inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-xs font-medium transition-colors',
  {
    variants: {
      variant: {
        default: 'bg-accent/15 text-accent-light border border-accent/20',
        active: 'bg-fleet-active-bg text-fleet-active border border-fleet-active-border',
        maintenance: 'bg-fleet-maintenance-bg text-fleet-maintenance border border-fleet-maintenance-border',
        inactive: 'bg-fleet-inactive-bg text-fleet-inactive border border-fleet-inactive-border',
        danger: 'bg-fleet-danger-bg text-fleet-danger border border-fleet-danger-border',
        secondary: 'bg-surface-elevated text-text-secondary border border-subtle',
        outline: 'border border-subtle text-text-muted',
      },
    },
    defaultVariants: {
      variant: 'default',
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return <div className={cn(badgeVariants({ variant }), className)} {...props} />
}

export { Badge, badgeVariants }
