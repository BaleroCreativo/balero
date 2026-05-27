import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
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
      }
    }
  }
})
