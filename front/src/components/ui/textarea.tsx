import * as React from 'react'
import { cn } from '@/lib/utils'

export interface TextareaProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {}

const Textarea = React.forwardRef<HTMLTextAreaElement, TextareaProps>(
  ({ className, ...props }, ref) => {
    return (
      <textarea
        className={cn(
          'flex min-h-[80px] w-full rounded-lg border border-subtle bg-surface-elevated px-3 py-2 text-[13px] text-text-primary',
          'placeholder:text-text-muted',
          'hover:border-subtle-hover focus:border-accent/40 focus:ring-1 focus:ring-accent/20 focus:outline-none',
          'disabled:cursor-not-allowed disabled:opacity-50',
          'resize-none transition-all',
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Textarea.displayName = 'Textarea'

export { Textarea }
