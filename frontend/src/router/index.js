import { createRouter, createWebHistory } from 'vue-router'
import { isAuthenticated } from '@/utils/auth'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import RegisterProView from '@/views/RegisterProView.vue'
import Home from '@/views/Home.vue'
import AdminPro from '@/views/AdminPro.vue'
import AdminCust from '@/views/AdminCust.vue'
import Dashboard from '@/views/Dashboard.vue'
import dbView from '@/views/dbView.vue'
import ServicesView from '@/views/ServicesView.vue'
import ServicePageView from '@/views/ServicePageView.vue'
import BookingView from '@/views/BookingView.vue'
import AdminServicesView from '@/views/AdminServicesView.vue'
import AdminDashboardView from '@/views/AdminDashboardView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ContactView from '@/views/ContactView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView, meta: { requiresAuth: true }, },
    { path: '/dashboard', name: 'dashboard', component: Dashboard, meta: { requiresAuth: true }, },
    { path: '/admindashboard', name: 'admindashboard', component: AdminDashboardView, meta: { requiresAuth: true }, },
    { path: '/h1', name: 'h1', component: Home, },
    { path: '/login', name: 'login', component: LoginView, },
    { path: '/register', name: 'register', component: RegisterView, },
    { path: '/registerpro', name: 'registerpro', component: RegisterProView, meta: { requiresAuth: true }, },
    { path: '/db', name: 'db', component: dbView, },
    { path: '/services', name: 'services', component: ServicesView, },
    { path: '/admin/service', name: 'adminservices', component: AdminServicesView, meta: { requiresAuth: true }, },
    { path: '/servicepage/:id', name: 'servicepage', component: ServicePageView, meta: { requiresAuth: true }, },
    { path: '/booking/:id', name: 'booking', component: BookingView, meta: { requiresAuth: true }, },
    { path: '/profile/', name: 'profile', component: ProfileView, meta: { requiresAuth: true }, },
    { path: '/contact/', name: 'contact', component: ContactView, },

    {
      path: '/about', name: 'about',  // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    { path: '/admin/pro', name: 'adminPro', component: AdminPro, meta: { requiresAuth: true }, },
    { path: '/admin/cust', name: 'adminCust', component: AdminCust, meta: { requiresAuth: true }, },

  ],


})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {

    next({ path: '/login' });
  } else {
    next();
  }
});
export default router
