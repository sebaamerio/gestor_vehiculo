'use client'

import { AppShell } from '@/components/layout/AppShell'
import { PageHeader } from '@/components/shared/PageHeader'
import { Settings, User, Bell, Shield, Globe } from 'lucide-react'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Label } from '@/components/ui/label'
import { Separator } from '@/components/ui/separator'

export default function SettingsPage() {
  return (
    <AppShell>
      <div className="px-6 md:px-8 py-8 max-w-[720px] mx-auto">
        <PageHeader
          title="Settings"
          description="Manage your fleet preferences"
          icon={Settings}
        />

        <div className="space-y-6">
          {/* Company */}
          <div className="bg-surface rounded-2xl border border-subtle p-6">
            <div className="flex items-center gap-2 mb-5">
              <Globe className="w-4 h-4 text-text-muted" />
              <h3 className="text-[14px] font-semibold text-text-primary">Company</h3>
            </div>
            <div className="space-y-4">
              <div className="space-y-1.5">
                <Label>Company Name</Label>
                <Input defaultValue="Acme Corporation" />
              </div>
              <div className="space-y-1.5">
                <Label>Fleet Name</Label>
                <Input defaultValue="Main Fleet" />
              </div>
              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <Label>Currency</Label>
                  <Input defaultValue="USD" />
                </div>
                <div className="space-y-1.5">
                  <Label>Mileage Unit</Label>
                  <Input defaultValue="km" />
                </div>
              </div>
            </div>
            <div className="flex justify-end mt-5">
              <Button size="sm">Save Changes</Button>
            </div>
          </div>

          {/* Notifications */}
          <div className="bg-surface rounded-2xl border border-subtle p-6">
            <div className="flex items-center gap-2 mb-5">
              <Bell className="w-4 h-4 text-text-muted" />
              <h3 className="text-[14px] font-semibold text-text-primary">Notifications</h3>
            </div>
            <div className="space-y-4">
              {[
                { label: 'Insurance expiry alerts', desc: 'Get notified 30 days before insurance expires' },
                { label: 'Inspection due alerts', desc: 'Reminder when technical inspection is upcoming' },
                { label: 'Maintenance reminders', desc: 'Alerts for scheduled maintenance' },
                { label: 'Driver license expiry', desc: 'Warning when a driver license is expiring' },
              ].map((item) => (
                <div key={item.label} className="flex items-start justify-between gap-4">
                  <div>
                    <div className="text-[13px] font-medium text-text-primary">{item.label}</div>
                    <div className="text-[12px] text-text-muted">{item.desc}</div>
                  </div>
                  <button className="w-9 h-5 rounded-full bg-accent flex-shrink-0 relative transition-colors">
                    <div className="w-3.5 h-3.5 bg-white rounded-full absolute right-0.5 top-0.5 shadow-sm transition-transform" />
                  </button>
                </div>
              ))}
            </div>
          </div>

          {/* Account */}
          <div className="bg-surface rounded-2xl border border-subtle p-6">
            <div className="flex items-center gap-2 mb-5">
              <User className="w-4 h-4 text-text-muted" />
              <h3 className="text-[14px] font-semibold text-text-primary">Account</h3>
            </div>
            <div className="space-y-4">
              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <Label>First Name</Label>
                  <Input defaultValue="Sebastian" />
                </div>
                <div className="space-y-1.5">
                  <Label>Last Name</Label>
                  <Input defaultValue="Amerio" />
                </div>
              </div>
              <div className="space-y-1.5">
                <Label>Email</Label>
                <Input defaultValue="sebah.amerio@gmail.com" />
              </div>
            </div>
            <div className="flex justify-end mt-5">
              <Button size="sm">Save Changes</Button>
            </div>
          </div>
        </div>
      </div>
    </AppShell>
  )
}
