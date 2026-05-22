'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'
import { Search, Bell, Plus, Menu } from 'lucide-react'
import { cn } from '@/lib/utils'
import { format } from 'date-fns'

interface TopBarProps {
  onMenuClick?: () => void
  onAddVehicle?: () => void
}

export function TopBar({ onMenuClick, onAddVehicle }: TopBarProps) {
  const [searchFocused, setSearchFocused] = useState(false)
  const [searchValue, setSearchValue] = useState('')

  const today = format(new Date(), 'EEEE, MMMM d')

  return (
    <header className="h-14 flex items-center justify-between px-6 border-b border-subtle bg-base/80 backdrop-blur-sm flex-shrink-0 z-10">
      {/* Left: Mobile menu + Search */}
      <div className="flex items-center gap-3 flex-1 min-w-0">
        <button
          onClick={onMenuClick}
          className="md:hidden w-8 h-8 flex items-center justify-center rounded-lg text-text-muted hover:text-text-secondary hover:bg-subtle transition-colors"
        >
          <Menu className="w-4 h-4" />
        </button>

        <div
          className={cn(
            'relative flex items-center gap-2 h-8 rounded-lg border transition-all duration-200 max-w-xs w-full',
            searchFocused
              ? 'border-subtle-active bg-surface-elevated'
              : 'border-subtle bg-surface/60 hover:border-subtle-hover'
          )}
        >
          <Search
            className={cn(
              'absolute left-2.5 w-3.5 h-3.5 transition-colors',
              searchFocused ? 'text-text-secondary' : 'text-text-muted'
            )}
          />
          <input
            type="text"
            placeholder="Search vehicles, drivers…"
            value={searchValue}
            onChange={(e) => setSearchValue(e.target.value)}
            onFocus={() => setSearchFocused(true)}
            onBlur={() => setSearchFocused(false)}
            className="w-full h-full bg-transparent pl-8 pr-3 text-[13px] text-text-primary placeholder:text-text-muted focus:outline-none"
          />
          {searchValue && (
            <kbd className="hidden md:flex items-center gap-0.5 mr-2 px-1.5 py-0.5 rounded text-[10px] text-text-muted bg-subtle font-mono">
              esc
            </kbd>
          )}
        </div>
      </div>

      {/* Center: Date (desktop) */}
      <div className="hidden lg:flex items-center absolute left-1/2 -translate-x-1/2">
        <span className="text-[13px] text-text-muted font-medium">{today}</span>
      </div>

      {/* Right: Actions */}
      <div className="flex items-center gap-2 flex-shrink-0">
        {/* Notifications */}
        <button className="relative w-8 h-8 flex items-center justify-center rounded-lg text-text-muted hover:text-text-secondary hover:bg-subtle transition-colors">
          <Bell className="w-4 h-4" />
          <span className="absolute top-1.5 right-1.5 w-1.5 h-1.5 rounded-full bg-fleet-maintenance" />
        </button>

        {/* Add Vehicle */}
        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={onAddVehicle}
          className="flex items-center gap-1.5 h-8 px-3 rounded-lg bg-accent hover:bg-accent-light text-white text-[13px] font-medium transition-colors shadow-glow-sm"
        >
          <Plus className="w-3.5 h-3.5" />
          <span className="hidden sm:inline">Add Vehicle</span>
        </motion.button>

        {/* Avatar */}
        <button className="w-7 h-7 rounded-full bg-accent/20 border border-accent/30 flex items-center justify-center text-[11px] font-semibold text-accent-light transition-all hover:border-accent/50 ml-1">
          SA
        </button>
      </div>
    </header>
  )
}
