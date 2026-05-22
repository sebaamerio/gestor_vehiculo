import * as React from 'react'
import { Slot } from '@radix-ui/react-slot'
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  'inline-flex items-center justify-center whitespace-nowrap rounded-lg text-sm font-medium transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/60 focus-visible:ring-offset-1 focus-visible:ring-offset-base disabled:pointer-events-none disabled:opacity-40 active:scale-[0.98]',
  {
    variants: {
      variant: {
        default:
          'bg-accent text-white hover:bg-accent-light shadow-glow-sm hover:shadow-glow',
        destructive:
          'bg-fleet-danger text-white hover:bg-fleet-danger/90',
        outline:
          'border border-subtle-active bg-transparent text-text-secondary hover:bg-subtle hover:text-text-primary',
        secondary:
          'bg-surface-elevated border border-subtle text-text-secondary hover:bg-surface-hover hover:text-text-primary hover:border-subtle-hover',
        ghost:
          'text-text-secondary hover:bg-subtle hover:text-text-primary',
        link:
          'text-accent underline-offset-4 hover:underline',
        muted:
          'bg-subtle text-text-secondary hover:bg-subtle-hover hover:text-text-primary',
      },
      size: {
        default: 'h-9 px-4 py-2 text-[13px]',
        sm: 'h-7 rounded-md px-2.5 text-xs',
        lg: 'h-11 rounded-xl px-6 text-sm',
        icon: 'h-9 w-9',
        'icon-sm': 'h-7 w-7 rounded-md',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : 'button'
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = 'Button'

export { Button, buttonVariants }
