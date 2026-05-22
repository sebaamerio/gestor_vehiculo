import type { Config } from 'tailwindcss'
import tailwindcssAnimate from 'tailwindcss-animate'

const config: Config = {
  darkMode: ['class'],
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      colors: {
        // Design system tokens
        base: '#0A0A0A',
        surface: {
          DEFAULT: '#111111',
          elevated: '#141414',
          hover: '#181818',
          overlay: '#1C1C1C',
        },
        accent: {
          DEFAULT: '#7C3AED',
          light: '#8B5CF6',
          dark: '#6D28D9',
          muted: 'rgba(124,58,237,0.15)',
          glow: 'rgba(124,58,237,0.25)',
        },
        subtle: {
          DEFAULT: 'rgba(255,255,255,0.06)',
          hover: 'rgba(255,255,255,0.08)',
          active: 'rgba(255,255,255,0.12)',
          strong: 'rgba(255,255,255,0.20)',
        },
        text: {
          primary: '#FAFAFA',
          secondary: 'rgba(255,255,255,0.60)',
          muted: 'rgba(255,255,255,0.38)',
          disabled: 'rgba(255,255,255,0.22)',
        },
        fleet: {
          active: '#10B981',
          'active-bg': 'rgba(16,185,129,0.12)',
          'active-border': 'rgba(16,185,129,0.25)',
          maintenance: '#F59E0B',
          'maintenance-bg': 'rgba(245,158,11,0.12)',
          'maintenance-border': 'rgba(245,158,11,0.25)',
          inactive: '#6B7280',
          'inactive-bg': 'rgba(107,114,128,0.12)',
          'inactive-border': 'rgba(107,114,128,0.25)',
          danger: '#EF4444',
          'danger-bg': 'rgba(239,68,68,0.12)',
          'danger-border': 'rgba(239,68,68,0.25)',
        },
        // Shadcn compatibility
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
        popover: {
          DEFAULT: 'hsl(var(--popover))',
          foreground: 'hsl(var(--popover-foreground))',
        },
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
        '2xl': '1rem',
        '3xl': '1.5rem',
        '4xl': '2rem',
      },
      boxShadow: {
        card: '0 0 0 1px rgba(255,255,255,0.06)',
        'card-hover': '0 0 0 1px rgba(255,255,255,0.10), 0 8px 32px rgba(0,0,0,0.5)',
        elevated: '0 0 0 1px rgba(255,255,255,0.06), 0 16px 48px rgba(0,0,0,0.6)',
        glow: '0 0 40px rgba(124,58,237,0.35)',
        'glow-sm': '0 0 20px rgba(124,58,237,0.25)',
        'inner-subtle': 'inset 0 1px 0 rgba(255,255,255,0.06)',
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-card': 'linear-gradient(135deg, rgba(255,255,255,0.03) 0%, transparent 100%)',
        'gradient-accent': 'linear-gradient(135deg, #7C3AED 0%, #8B5CF6 100%)',
        'gradient-hero': 'radial-gradient(ellipse at 50% 0%, rgba(124,58,237,0.15) 0%, transparent 60%)',
      },
      keyframes: {
        'accordion-down': {
          from: { height: '0' },
          to: { height: 'var(--radix-accordion-content-height)' },
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: '0' },
        },
        'fade-in': {
          from: { opacity: '0', transform: 'translateY(8px)' },
          to: { opacity: '1', transform: 'translateY(0)' },
        },
        'fade-in-scale': {
          from: { opacity: '0', transform: 'scale(0.96)' },
          to: { opacity: '1', transform: 'scale(1)' },
        },
        shimmer: {
          '0%': { backgroundPosition: '-1000px 0' },
          '100%': { backgroundPosition: '1000px 0' },
        },
        'pulse-glow': {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.5' },
        },
      },
      animation: {
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out',
        'fade-in': 'fade-in 0.3s ease-out',
        'fade-in-scale': 'fade-in-scale 0.2s ease-out',
        shimmer: 'shimmer 2s linear infinite',
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite',
      },
      transitionTimingFunction: {
        spring: 'cubic-bezier(0.175, 0.885, 0.32, 1.275)',
        smooth: 'cubic-bezier(0.4, 0, 0.2, 1)',
      },
    },
  },
  plugins: [tailwindcssAnimate],
}

export default config
