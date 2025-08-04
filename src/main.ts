/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import { createPinia } from 'pinia'
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Styles
import 'unfonts.css'

const app = createApp(App)
app.use(createPinia())
registerPlugins(app)
app.config.warnHandler = (msg, vm, trace) => {
  if (msg.includes('Slot "default" invoked outside of the render function')) {
    return // ignore this specific warning
  }
  console.warn(msg + trace)
}
app.mount('#app')
