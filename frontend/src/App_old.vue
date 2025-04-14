<template>
    <div id="app">
      <h1>Login</h1>
      <div v-if="!isLoggedIn">
        <form @submit.prevent="login">
          <div>
            <label for="username">Username:</label>
            <input type="text" v-model="username" id="username" required />
          </div>
          <div>
            <label for="password">Password:</label>
            <input type="password" v-model="password" id="password" required />
          </div>
          <button type="submit">Login</button>
        </form>
      </div>
  
      <div v-if="isLoggedIn">
        <h2>Welcome, {{ username }}!</h2>
        <button @click="getProtectedData">Go to Protected Route</button>
        <div v-if="protectedData">
          <h3>Protected Data:</h3>
          <pre>{{ protectedData }}</pre>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        isLoggedIn: false,
        protectedData: null,
        token: null // Store JWT token here
      };
    },
    mounted() {
      // Check if there is a token in localStorage when the component mounts
      const savedToken = localStorage.getItem('token');
      if (savedToken) {
        this.token = savedToken;
        this.isLoggedIn = true;
      }
    },
    methods: {
      async login() {
        try {
          const response = await this.$axios.post('http://localhost:5000/api/login', {
            username: this.username,
            password: this.password
          });
          console.log('Login success', response.data);
  
          // Store the token in localStorage for persistence
          if (response.data.token) {
            this.token = response.data.token;
            localStorage.setItem('token', this.token);  // Save token to localStorage
            this.isLoggedIn = true;
          } else {
            console.error('Token not returned');
            alert('Token not returned');
          }
        } catch (error) {
          console.error('Login failed', error.response ? error.response.data : error);
          alert('Login failed');
        }
      },
  
      async getProtectedData() {
        try {
          const response = await this.$axios.get('http://localhost:5000/api/user', {
            headers: {
              Authorization: `Bearer ${this.token}`
            }
          });
          console.log('Protected route data:', response.data);
          this.protectedData = response.data;
        } catch (error) {
          console.error('Failed to access protected route', error.response ? error.response.data : error);
          alert('Access denied');
        }
      },
  
      // Logout method to clear token from localStorage
      logout() {
        this.token = null;
        this.isLoggedIn = false;
        localStorage.removeItem('token');  // Remove token from localStorage on logout
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  