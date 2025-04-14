<template>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="card shadow-lg p-4 col-md-6 col-lg-4">
      <div class="card-body text-center">
        <h2 class="mb-4">Login</h2>

       

        <!-- Login Form -->
        <form @submit.prevent="login">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input v-model="username" type="text" class="form-control" id="username" placeholder="Enter username" required>
          </div>

          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input v-model="password" type="password" class="form-control" id="password" placeholder="Enter password" required>
          </div>

          <button type="submit" class="btn btn-primary w-100">Login</button>
        </form>
      </div>
      
      <div class="text-center mt-3">
        <span>Don’t have an account?</span>
        <button class="btn btn-outline-secondary ms-2" @click="$router.push('/register')">Register Now</button>
      </div>
    </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await this.$axios.post('http://localhost:5000/api/login', {
          username: this.username,
          password: this.password
        });

        if (response.data.token) {
          localStorage.setItem('token', response.data.token);
          localStorage.setItem('user', JSON.stringify(response.data.user));
          if (response.data.user.user_role ==='admin'){
              this.$router.push('/admindashboard'); 


          }
          else {this.$router.push('/dashboard')}; 
        } else {
          alert(`Login failed: ${response.data.message}`);
        }
      } catch (error) {
        alert(`Login failed: ${error.response?.data?.message || 'Unknown error'}`);
      }
    }
  }
};
</script>
