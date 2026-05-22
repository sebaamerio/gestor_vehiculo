import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'
import { format, parseISO, differenceInDays, isPast, isWithinInterval, addDays } from 'date-fns'
import type { VehicleStatus, FuelType, MaintenanceType } from './types'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function formatDate(dateStr: string, fmt = 'MMM d, yyyy'): string {
  try {
    return format(parseISO(dateStr), fmt)
  } catch {
    return dateStr
  }
}

export function formatCurrency(amount: number, currency = 'USD'): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency,
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(amount)
}

export function formatMileage(mileage: number): string {
  return new Intl.NumberFormat('en-US').format(mileage) + ' km'
}

export function daysUntilExpiry(dateStr: string): number {
  try {
    const date = parseISO(dateStr)
    return differenceInDays(date, new Date())
  } catch {
    return 0
  }
}

export function isExpiringSoon(dateStr: string, withinDays = 30): boolean {
  try {
    const date = parseISO(dateStr)
    const today = new Date()
    return isWithinInterval(date, { start: today, end: addDays(today, withinDays) })
  } catch {
    return false
  }
}

export function isExpired(dateStr: string): boolean {
  try {
    return isPast(parseISO(dateStr))
  } catch {
    return false
  }
}

export function getExpiryStatus(dateStr: string): 'expired' | 'critical' | 'warning' | 'ok' {
  if (isExpired(dateStr)) return 'expired'
  const days = daysUntilExpiry(dateStr)
  if (days <= 7) return 'critical'
  if (days <= 30) return 'warning'
  return 'ok'
}

export function getStatusLabel(status: VehicleStatus): string {
  const labels: Record<VehicleStatus, string> = {
    active: 'Active',
    maintenance: 'In Maintenance',
    inactive: 'Inactive',
    out_of_service: 'Out of Service',
  }
  return labels[status]
}

export function getFuelTypeLabel(fuelType: FuelType): string {
  const labels: Record<FuelType, string> = {
    gasoline: 'Gasoline',
    diesel: 'Diesel',
    electric: 'Electric',
    hybrid: 'Hybrid',
    cng: 'CNG',
  }
  return labels[fuelType]
}

export function getMaintenanceTypeLabel(type: MaintenanceType): string {
  const labels: Record<MaintenanceType, string> = {
    oil_change: 'Oil Change',
    tire_rotation: 'Tire Rotation',
    brake_inspection: 'Brake Inspection',
    air_filter: 'Air Filter',
    transmission: 'Transmission',
    battery: 'Battery',
    coolant: 'Coolant',
    alignment: 'Wheel Alignment',
    general_inspection: 'General Inspection',
    other: 'Other',
  }
  return labels[type]
}

export function getBrandColor(brand: string): string {
  const brandColors: Record<string, string> = {
    BMW: '#1C69D4',
    Mercedes: '#A8B0B9',
    'Mercedes-Benz': '#A8B0B9',
    Toyota: '#EB0A1E',
    Ford: '#003499',
    Volkswagen: '#1E3A8A',
    Honda: '#CC0000',
    Hyundai: '#002C5F',
    Kia: '#BB162B',
    Nissan: '#C3002F',
    Audi: '#BB0A30',
    Chevrolet: '#F7B600',
    Renault: '#FFCC00',
    Peugeot: '#003B8E',
    Fiat: '#CC0000',
    Jeep: '#32502E',
    Land: '#005A2B',
    'Land Rover': '#005A2B',
    Volvo: '#003057',
    Porsche: '#AE9161',
    Tesla: '#CC0000',
  }
  return brandColors[brand] || '#7C3AED'
}

export function generateId(): string {
  return Math.random().toString(36).substring(2) + Date.now().toString(36)
}

export function getInitials(name: string): string {
  return name
    .split(' ')
    .map((n) => n[0])
    .join('')
    .toUpperCase()
    .slice(0, 2)
}

export function calculateFuelEfficiency(logs: { mileage: number; liters: number }[]): number {
  if (logs.length < 2) return 0
  const sorted = [...logs].sort((a, b) => a.mileage - b.mileage)
  const totalDistance = sorted[sorted.length - 1].mileage - sorted[0].mileage
  const totalFuel = sorted.slice(1).reduce((sum, log) => sum + log.liters, 0)
  if (totalFuel === 0) return 0
  return totalDistance / totalFuel
}

export function truncate(str: string, length: number): string {
  if (str.length <= length) return str
  return str.slice(0, length) + '…'
}
