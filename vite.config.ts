import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: { '@': resolve(__dirname, './src') },
  },
  build: {
    rollupOptions: {
      input: {
        // Existing Polar Construct pages
        main:          resolve(__dirname, 'index.html'),
        nosotros:      resolve(__dirname, 'nosotros.html'),
        sectores:      resolve(__dirname, 'sectores.html'),
        servicios:     resolve(__dirname, 'servicios.html'),
        refrigeracion: resolve(__dirname, 'refrigeracion.html'),
        congelacion:   resolve(__dirname, 'congelacion.html'),
        mantenimiento: resolve(__dirname, 'mantenimiento.html'),
        refacciones:   resolve(__dirname, 'refacciones.html'),
        contacto:      resolve(__dirname, 'contacto.html'),
        legal:         resolve(__dirname, 'legal.html'),
        // Eje Ocho React app
        ejeocho:       resolve(__dirname, 'ejeocho/index.html'),
      }
    }
  }
})
