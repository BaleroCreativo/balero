/** @type {import('tailwindcss').Config} */
export default {
  content: ['./*.html', './src/**/*.{js,ts}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Plus Jakarta Sans', 'system-ui', 'sans-serif'],
      },
      colors: {
        polar: {
          50:  '#F0F9FF',
          100: '#E0F2FE',
          200: '#BAE6FD',
          300: '#7DD3FC',
          500: '#0EA5E9',
          600: '#0284C7',
          700: '#0369A1',
          800: '#075985',
          900: '#0C4A6E',
        },
        navy: {
          50:  '#F8FAFC',
          100: '#F1F5F9',
          200: '#E2E8F0',
          400: '#94A3B8',
          500: '#64748B',
          600: '#475569',
          700: '#334155',
          900: '#0F172A',
          950: '#020617',
        },
      },
      container: {
        center: true,
        padding: { DEFAULT: '1.25rem', sm: '1.5rem', lg: '2rem' },
        screens: { xl: '1280px' },
      },
    },
  },
  plugins: [require('@tailwindcss/forms')],
}
