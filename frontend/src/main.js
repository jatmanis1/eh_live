import './assets/style.css';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

import { currentUser } from './utils/current_user';

// ✅ Define backend base URL
// const BACKEND_URL = 'http://127.0.0.1:5000'; // Change to your actual backend in production
const BACKEND_URL = 'https://easyhomebackend.vercel.app';

// ✅ Create a custom axios instance
const axiosInstance = axios.create({
    baseURL: BACKEND_URL,
    withCredentials: true,
});

const app = createApp(App);

// ✅ Global properties for use in any component
app.config.globalProperties.$axios = axiosInstance;
app.config.globalProperties.$backendUrl = BACKEND_URL;
app.config.globalProperties.$currentUser = currentUser();

app.use(router);
app.mount('#app');

// ✅ Call setup on app start
setupAutoLogout();

// ✅ Automatically log out user after token expiry
function setupAutoLogout() {
    const expiry = localStorage.getItem('tokenExpiry');

    if (!expiry) return;

    const timeLeft = parseInt(expiry) - Date.now();

    if (timeLeft <= 0) {
        // Token already expired
        clearAuthStorage();
        alert("Session expired. Please log in again.");
        router.push('/login');
        return;
    }

    setTimeout(() => {
        clearAuthStorage();
        alert("Session expired automatically (2hr passed). Please log in again.");
        router.push('/login');
    }, timeLeft);
}

// ✅ Clear all auth-related data
function clearAuthStorage() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    localStorage.removeItem('tokenExpiry');
}
// import './assets/style.css';
// import "bootstrap/dist/css/bootstrap.min.css";
// import "bootstrap/dist/js/bootstrap.bundle.min";

// import { createApp } from 'vue';
// import App from './App.vue';
// import router from './router';
// import axios from 'axios';

// import { currentUser } from './utils/current_user';

// // ✅ Define backend base URL in one place
// // const BACKEND_URL = 'https://easyhomebackend.vercel.app';
// const BACKEND_URL = 'http://127.0.0.1:5000';
// // console.log('asdfghgfds')
// // ✅ Create a custom axios instance
// const axiosInstance = axios.create({
//     baseURL: BACKEND_URL,
//     withCredentials: true, // Optional: if you send/receive cookies
// });

// const app = createApp(App);

// // ✅ Make it globally available across components
// app.config.globalProperties.$axios = axiosInstance;
// app.config.globalProperties.$backendUrl = BACKEND_URL;  // Optional, if you need raw URL
// app.config.globalProperties.$currentUser = currentUser();

// app.use(router);
// app.mount('#app');


// function setupAutoLogout() {
//     const expiry = localStorage.getItem('tokenExpiry');

//     if (!expiry) return;

//     const timeLeft = parseInt(expiry) - Date.now();

//     if (timeLeft <= 0) {
//         // Token already expired
//         clearAuthStorage();
//         alert("Session expired. Please log in again.");
//         return;
//     }

//     setTimeout(() => {
//         clearAuthStorage();
//         alert("Session expired automatically (2hr passed). Please log in again.");
//         // Optional: redirect to login
//         this.$router.push('/login');
//         // window.location.href = '/login';
//     }, timeLeft);
// }
