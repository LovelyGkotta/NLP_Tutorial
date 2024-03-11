import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

axios.defaults.baseURL = "http://127.0.0.1:5173"

const app = createApp(App)
app.mount('#app')
