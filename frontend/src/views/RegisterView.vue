<template>
  <div v-if="showForm" class="container d-flex justify-content-center align-items-center vh-100">
    <div class="card p-5 shadow-lg rounded-4" style="max-width: 500px; width: 100%;">
      <h2 class="text-center mb-4 fw-bold text-primary">Register</h2>
      <form @submit.prevent="register">
        <div class="mb-3">
          <label for="username" class="form-label fw-semibold">Username</label>
          <input v-model="username" class="form-control" id="username" placeholder="Enter Username" required />
        </div>

        <div class="mb-3">
          <label for="password" class="form-label fw-semibold">Password</label>
          <input v-model="password" type="password" class="form-control" id="password" placeholder="Enter Password" required />
        </div>

        <div class="mb-3">
          <label for="email" class="form-label fw-semibold">Email</label>
          <input v-model="email" type="email" class="form-control" id="email" placeholder="Enter Email" required />
        </div>

        <div class="mb-3">
          <label for="pincode" class="form-label fw-semibold">Pincode</label>
          <input v-model="pincode" type="number" class="form-control" id="pincode" placeholder="Enter Pincode" required />
        </div>

        <div class="mb-3">
          <label for="address" class="form-label fw-semibold">Address</label>
          <input v-model="address" class="form-control" id="address" placeholder="Enter Address" required />
        </div>

        <button type="submit" class="btn btn-primary w-100 py-2 fw-bold">Register</button>
        <p v-if="error1" class="text-danger text-center mt-3">{{ error1 }}</p>
      </form>

      <div class="text-center mt-3">
        <span>Already have an account?</span>
        <button class="btn btn-outline-secondary ms-2" @click="$router.push('/login')">Login</button>
      </div>
    </div>
  </div>

  <!-- Modal -->
  <transition name="fade">
    <div v-if="showModal" class="modal fade show d-block" tabindex="-1" style="background: rgba(0, 0, 0, 0.5);">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content shadow-lg rounded-3">
          <div class="modal-header">
            <h5 class="modal-title fw-bold">Registration Complete</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body text-center">
            <p class="fw-semibold">Choose the role you want to register as:</p>
            <div class="d-flex justify-content-center gap-3">
              <button type="button" class="btn btn-outline-secondary px-4" @click="$router.push('/services')">Customer</button>
              <button type="button" class="btn btn-primary px-4" @click="$router.push('/registerpro')">Service Professional</button>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      email: '',
      address: '',
      pincode: '',
      error1: null,
      showModal: false,
      showForm: true,
    };
  },
  methods: {
    closeModal() {
      this.$router.push('/dashboard');
      this.showModal = false;
    },
    async register() {
      try {
        const response = await this.$axios.post('http://localhost:5000/api/register', {
          username: this.username,
          password: this.password,
          user_email: this.email,
          user_pincode: this.pincode,
          user_address: this.address,
        });

        if (response.data.message) {
          alert(response.data.message);
          localStorage.setItem('token', response.data.response.token);
          localStorage.setItem('user', JSON.stringify(response.data.response.user));
          this.showModal = true;
          this.showForm = false;
        } else {
          alert('Unexpected response');
        }
      } catch (error) {
        this.error1 = error.response?.data?.message || 'Registration failed';
        alert(`Register failed: ${this.error1}`);
      }
    },
  },
};
</script>

<style scoped>
.card {
  border-radius: 12px;
  background: #fff;
}

.modal-content {
  border-radius: 12px;
}

/* Smooth transition for the modal */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
