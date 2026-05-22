export type FuelType = 'gasoline' | 'diesel' | 'electric' | 'hybrid' | 'cng'
export type VehicleStatus = 'active' | 'maintenance' | 'inactive' | 'out_of_service'
export type DriverStatus = 'active' | 'inactive' | 'on_leave'
export type DocumentType = 'insurance' | 'registration' | 'inspection' | 'permit' | 'other'
export type MaintenanceType =
  | 'oil_change'
  | 'tire_rotation'
  | 'brake_inspection'
  | 'air_filter'
  | 'transmission'
  | 'battery'
  | 'coolant'
  | 'alignment'
  | 'general_inspection'
  | 'other'

export interface Vehicle {
  id: string
  brand: string
  model: string
  year: number
  plateNumber: string
  vin: string
  mileage: number
  fuelType: FuelType
  status: VehicleStatus
  assignedDriverId?: string
  insuranceExpiration: string
  technicalInspectionExpiration: string
  color?: string
  purchaseDate?: string
  purchaseCost?: number
  notes?: string
  thumbnail?: string
  brandColor?: string
  createdAt: string
  updatedAt: string
}

export interface MaintenanceRecord {
  id: string
  vehicleId: string
  type: MaintenanceType
  description: string
  date: string
  cost: number
  mileage: number
  provider?: string
  nextScheduledDate?: string
  nextScheduledMileage?: number
  status: 'completed' | 'scheduled' | 'overdue'
}

export interface FuelLog {
  id: string
  vehicleId: string
  date: string
  liters: number
  cost: number
  mileage: number
  pricePerLiter: number
  fullTank: boolean
  station?: string
}

export interface Driver {
  id: string
  name: string
  email: string
  phone: string
  licenseNumber: string
  licenseExpiration: string
  status: DriverStatus
  assignedVehicleId?: string
  avatar?: string
  initials: string
  joinDate: string
  totalTrips?: number
  rating?: number
}

export interface VehicleDocument {
  id: string
  vehicleId: string
  type: DocumentType
  name: string
  issueDate: string
  expirationDate: string
  provider?: string
  cost?: number
  fileUrl?: string
  notes?: string
}

export interface Alert {
  id: string
  vehicleId: string
  type: 'insurance_expiry' | 'inspection_expiry' | 'maintenance_due' | 'license_expiry' | 'mileage_service'
  severity: 'critical' | 'warning' | 'info'
  message: string
  dueDate?: string
  daysUntil?: number
  dismissed?: boolean
}

export interface DashboardStats {
  totalVehicles: number
  activeVehicles: number
  inMaintenance: number
  outOfService: number
  totalDrivers: number
  activeDrivers: number
  monthlyFuelCost: number
  monthlyMaintenanceCost: number
  totalMileageThisMonth: number
  upcomingMaintenanceCount: number
}

export interface VehicleFormData {
  brand: string
  model: string
  year: number
  plateNumber: string
  vin: string
  mileage: number
  fuelType: FuelType
  status: VehicleStatus
  assignedDriverId?: string
  insuranceExpiration: string
  technicalInspectionExpiration: string
  color?: string
  purchaseDate?: string
  purchaseCost?: number
  notes?: string
}
