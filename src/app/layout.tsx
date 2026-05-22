import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'FleetOS — Vehicle Management Platform',
  description: 'Premium fleet management platform for modern teams',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      </head>
      <body className="antialiased">{children}</body>
    </html>
  )
}
