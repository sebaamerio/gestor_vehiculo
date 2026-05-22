'use client'

import { useState } from 'react'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { motion, AnimatePresence } from 'framer-motion'
import {
  LayoutDashboard,
  Car,
  Wrench,
  Users,
  FileText,
  BarChart3,
  Settings,
  ChevronLeft,
  ChevronRight,
  Zap,
} from 'lucide-react'
import { cn } from '@/lib/utils'

interface NavItem {
  label: string
  href: string
  icon: React.ElementType
  badge?: number
}

const NAV_ITEMS: NavItem[] = [
  { label: 'Dashboard', href: '/dashboard', icon: LayoutDashboard },
  { label: 'Vehicles', href: '/vehicles', icon: Car },
  { label: 'Maintenance', href: '/maintenance', icon: Wrench, badge: 3 },
  { label: 'Drivers', href: '/drivers', icon: Users },
  { label: 'Documents', href: '/documents', icon: FileText },
  { label: 'Analytics', href: '/analytics', icon: BarChart3 },
]

interface SidebarProps {
  collapsed: boolean
  onToggle: () => void
}

export function Sidebar({ collapsed, onToggle }: SidebarProps) {
  const pathname = usePathname()

  return (
    <motion.aside
      initial={false}
      animate={{ width: collapsed ? 64 : 240 }}
      transition={{ duration: 0.2, ease: [0.4, 0, 0.2, 1] }}
      className="relative flex flex-col h-full bg-[#0D0D0D] border-r border-subtle overflow-hidden flex-shrink-0"
    >
      {/* Logo */}
      <div className="flex items-center h-16 px-4 border-b border-subtle flex-shrink-0">
        <div className="flex items-center gap-3 min-w-0">
          <div className="w-8 h-8 rounded-xl bg-accent flex items-center justify-center flex-shrink-0 shadow-glow-sm">
            <Zap className="w-4 h-4 text-white" fill="white" />
          </div>
          <AnimatePresence mode="wait">
            {!collapsed && (
              <motion.span
                initial={{ opacity: 0, x: -8 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -8 }}
                transition={{ duration: 0.15 }}
                className="font-semibold text-text-primary text-[15px] tracking-tight whitespace-nowrap"
              >
                FleetOS
              </motion.span>
            )}
          </AnimatePresence>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 py-4 px-2 space-y-0.5 overflow-y-auto overflow-x-hidden">
        {NAV_ITEMS.map((item) => {
          const isActive = pathname === item.href || (item.href !== '/dashboard' && pathname.startsWith(item.href))
          const Icon = item.icon

          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                'group relative flex items-center h-9 rounded-lg transition-all duration-150',
                collapsed ? 'justify-center px-0 w-10 mx-auto' : 'px-3 gap-3',
                isActive
                  ? 'bg-accent/15 text-accent-light'
                  : 'text-text-muted hover:text-text-secondary hover:bg-subtle'
              )}
              title={collapsed ? item.label : undefined}
            >
              {isActive && (
                <motion.div
                  layoutId="sidebar-active"
                  className="absolute inset-0 rounded-lg bg-accent/15"
                  transition={{ type: 'spring', bounce: 0.15, duration: 0.4 }}
                />
              )}

              <div className="relative flex items-center gap-3 min-w-0">
                <Icon
                  className={cn(
                    'w-[18px] h-[18px] flex-shrink-0 transition-colors',
                    isActive ? 'text-accent-light' : 'text-text-muted group-hover:text-text-secondary'
                  )}
                />

                <AnimatePresence mode="wait">
                  {!collapsed && (
                    <motion.span
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ duration: 0.1 }}
                      className={cn(
                        'text-[13px] font-medium whitespace-nowrap',
                        isActive ? 'text-accent-light' : 'text-text-secondary group-hover:text-text-primary'
                      )}
                    >
                      {item.label}
                    </motion.span>
                  )}
                </AnimatePresence>
              </div>

              {!collapsed && item.badge && item.badge > 0 && (
                <motion.span
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  className="ml-auto flex-shrink-0 min-w-[18px] h-[18px] px-1 rounded-full bg-fleet-maintenance text-white text-[10px] font-semibold flex items-center justify-center"
                >
                  {item.badge}
                </motion.span>
              )}

              {collapsed && item.badge && item.badge > 0 && (
                <span className="absolute top-0.5 right-0.5 w-2 h-2 rounded-full bg-fleet-maintenance" />
              )}
            </Link>
          )
        })}
      </nav>

      {/* Bottom section */}
      <div className="border-t border-subtle py-3 px-2 space-y-0.5">
        <Link
          href="/settings"
          className={cn(
            'group flex items-center h-9 rounded-lg transition-all duration-150 text-text-muted hover:text-text-secondary hover:bg-subtle',
            collapsed ? 'justify-center px-0 w-10 mx-auto' : 'px-3 gap-3'
          )}
          title={collapsed ? 'Settings' : undefined}
        >
          <Settings className="w-[18px] h-[18px] flex-shrink-0" />
          <AnimatePresence mode="wait">
            {!collapsed && (
              <motion.span
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                transition={{ duration: 0.1 }}
                className="text-[13px] font-medium"
              >
                Settings
              </motion.span>
            )}
          </AnimatePresence>
        </Link>

        {/* Collapse toggle */}
        <button
          onClick={onToggle}
          className={cn(
            'group flex items-center h-9 rounded-lg transition-all duration-150 text-text-muted hover:text-text-secondary hover:bg-subtle w-full',
            collapsed ? 'justify-center px-0 w-10 mx-auto' : 'px-3 gap-3'
          )}
          title={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}
        >
          {collapsed ? (
            <ChevronRight className="w-[18px] h-[18px]" />
          ) : (
            <>
              <ChevronLeft className="w-[18px] h-[18px]" />
              <motion.span
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="text-[13px] font-medium"
              >
                Collapse
              </motion.span>
            </>
          )}
        </button>
      </div>
    </motion.aside>
  )
}
