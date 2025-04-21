import './assets/style.css';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

import { currentUser } from './utils/current_user';

// ✅ Define backend base URL in one place
const BACKEND_URL = 'https://easyhomebackend.vercel.app';
// console.log('asdfghgfds')
// ✅ Create a custom axios instance
const axiosInstance = axios.create({
    baseURL: BACKEND_URL,
    withCredentials: true, // Optional: if you send/receive cookies
});

const app = createApp(App);

// ✅ Make it globally available across components
app.config.globalProperties.$axios = axiosInstance;
app.config.globalProperties.$backendUrl = BACKEND_URL;  // Optional, if you need raw URL
app.config.globalProperties.$currentUser = currentUser();

app.use(router);
app.mount('#app');
