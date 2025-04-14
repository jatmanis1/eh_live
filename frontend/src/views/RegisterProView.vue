<template>
  <div class="container mt-5">
    <div class="text-center mb-4">
      <button class="btn btn-primary mx-2" @click="$router.push('/dashboard')">Register as Customer</button>
    </div>
    
    
    <div class="card shadow p-4 mx-auto" style="max-width: 500px;">
      <h2 class="text-center text-primary">Register</h2>
      
      <form @submit.prevent="register">
        <div class="mb-3">
          <label for="exp" class="form-label">Experience (Years)</label>
          <input v-model="user_exp" type="number" class="form-control" id="exp" placeholder="Enter your experience" required>
        </div>
        
        <div class="mb-3">
          <label for="service" class="form-label">Select a Service</label>
          <select class="form-select" v-model="user_service" required>
            <option v-for="service in services" :key="service.id" :value="service.id">
              {{ service.service_name }}
            </option>
          </select>
        </div>
        
        <button type="submit" class="btn btn-primary w-100">Submit</button>
      </form>
      
      <p v-if="error1" class="text-danger text-center mt-3">{{ error1 }}</p>
    </div>
  </div>
  <br><br>
  <div v-if="services.length" class="alert alert-info">Available Services: {{ services.map(s => s.service_name).join(', ') }}</div>

</template>

<script>
export default {
  data() {
    return {
      user_exp: '',
      user_service: '',
      services: [],
      error1: null,
      currentUser: null,
    };
  },
  mounted() {
    this.fetchServices();
    const user = localStorage.getItem("user");
    this.currentUser = user ? JSON.parse(user) : null;
  },
  methods: {
    async fetchServices() {
      try {
        const response = await this.$axios.get('http://localhost:5000/api/admin/service');
        this.services = response.data.services;
      } catch (error) {
        console.error('Failed to fetch services:', error.response?.data || error);
      }
    },
    async register() {
      if (!this.currentUser || !this.currentUser.id) {
        this.error1 = "User is not logged in.";
        alert(this.error1);
        return;
      }
      
      try {
        const response = await this.$axios.put(
          `http://localhost:5000/api/register/${this.currentUser.id}`,
          { user_service: this.user_service, user_exp: this.user_exp }
        );
        
        if (response.status === 200) {
          alert(response.data.msg);
          this.$router.push('/dashboard');
        }
      } catch (error) {
        console.error('Register failed:', error.response?.data?.msg);
        this.error1 = error.response?.data?.msg || 'An error occurred';
        alert(`Register failed: ${this.error1}`);
      }
    }
  }
};
</script>

<!-- No need for extra CSS as Bootstrap is used -->