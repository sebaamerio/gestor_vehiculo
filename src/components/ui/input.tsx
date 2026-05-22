import * as React from 'react'
import { cn } from '@/lib/utils'

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  error?: boolean
}

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, error, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          'flex h-9 w-full rounded-lg border bg-surface-elevated px-3 py-1.5 text-[13px] text-text-primary transition-all',
          'placeholder:text-text-muted',
          'focus:outline-none focus:ring-1',
          'disabled:cursor-not-allowed disabled:opacity-50',
          error
            ? 'border-fleet-danger/50 focus:border-fleet-danger focus:ring-fleet-danger/25'
            : 'border-subtle hover:border-subtle-hover focus:border-accent/40 focus:ring-accent/20',
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = 'Input'

export { Input }
