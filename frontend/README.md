# Vue.js Frontend for Service Management Platform

## Overview
This is the frontend for a service management platform built with Vue.js. It provides user authentication, service browsing, booking management, and an admin dashboard for managing users and services.

## Features
- **User Authentication**: JWT-based login system
- **Role-based Routing**: Separate views for users and admins
- **Service Browsing**: View and search available services
- **Booking System**: Users can book services
- **Admin Dashboard**: Manage users, service providers, and bookings

## Technologies Used
- **Vue.js**: Frontend framework
- **Vue Router**: Client-side routing
- **Vuex (optional)**: State management
- **Axios**: API requests
- **Tailwind CSS**: Styling
- **Vite**: Build tool for fast development

## Recommended IDE Setup
[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (disable Vetur for best experience).

## Installation

### Prerequisites
Ensure you have Node.js and npm installed.

### 1. Clone the Repository
```bash
 git clone https://github.com/jatmanis11/mad2_project.git
 cd mad2_project/frontend
```


### 2. Install Dependencies
```bash
npm install
```

### 3. Run the Development Server
```bash
npm run dev
```

### 4. Compile and Minify for Production
```bash
npm run build
```

## Project Structure
```bash
src/
├── components/     # Reusable components
├── views/          # Page components
├── router/         # Vue Router setup
├── store/          # Vuex store (if used)
├── assets/         # Static assets
├── utils/          # Helper functions
└── main.js         # Application entry point
```

## Routing Setup
Defined in `router/index.js`:
```javascript
const routes = [
  { path: '/', name: 'home', component: HomeView, meta: { requiresAuth: true } },
  { path: '/login', name: 'login', component: LoginView },
  { path: '/register', name: 'register', component: RegisterView },
  { path: '/services', name: 'services', component: ServicesView },
  { path: '/booking/:id', name: 'booking', component: BookingView, meta: { requiresAuth: true } },
  { path: '/admin/dashboard', name: 'adminDashboard', component: AdminDashboardView, meta: { requiresAuth: true } }
];
```

## Deployment
To build for production:
```bash
npm run build
```

To deploy on a static host like Vercel or Netlify, use:
```bash
npm run build && npm run preview
```

## Contributors
- jatmanis1


## Customize Configuration
See [Vite Configuration Reference](https://vite.dev/config/).

