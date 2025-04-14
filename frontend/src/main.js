import './assets/style.css'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';

import { currentUser } from './utils/current_user';

const app = createApp(App)

// Set up axios to send credentials (cookies) with requests
axios.defaults.withCredentials = true;  // This ensures cookies are sent with requests
app.config.globalProperties.$axios = axios;
app.config.globalProperties.$currentUser = currentUser();

app.use(router)

app.mount('#app')

