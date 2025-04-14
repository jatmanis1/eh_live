<template>
  <div class="container mt-4">
    <!-- Service Name -->
    <h1 class="text-center text-danger fw-bold">{{ service.service_name || "Loading..." }}</h1>

    <div class="text-center mb-3">
      <p class="text-muted">{{ service.service_desc }}</p>
      <h4 class="text-success">₹ {{ service.service_b_price }}</h4>
      <p class="fw-bold">Estimated Completion Time: <span class="badge bg-dark">{{ service.time_required }} h</span></p>
    </div>

    <!-- Loading Message -->
    <div v-if="loading" class="text-center">
      <p class="text-primary">Fetching service details... Please wait <i class="bi bi-hourglass-split"></i></p>
    </div>

    <!-- Error Message -->
    <div v-if="error" class="text-center text-danger">
      <p>{{ error }}</p>
    </div>

    <!-- Professionals List -->
    <div v-if="professionals.length > 0">
      <h3 class="text-center mt-4 text-dark">Our Best Professionals</h3>

      <table class="table table-striped mt-3">
        <thead class="table-dark">
          <tr>
            <th>Professional</th>
            <th>Service Name</th>
            <th>Pincode</th>
            <th>Rating</th>
            <th v-if="currentUser.user_role === 'cust'">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="pro in professionals" :key="pro.id">
            <td>{{ pro.name }}</td>
            <td>{{ pro.desc }}</td>
            <td>{{ pro.user_pincode }}</td>
            <td>{{ pro.user_rating === 0.0 ? "Not Rated" : pro.user_rating }}</td>
            <td v-if="currentUser.user_role === 'cust'">
              <button @click="visitProfessional(pro.id)" class="btn btn-primary btn-sm">
                Visit
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- No Professionals Found -->
    <div v-else-if="!loading && !error" class="text-center mt-4 text-muted">
      <p>No professionals available for this service at the moment. 🚀</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      service: {},
      professionals: [],
      currentUser: this.$currentUser, // Assumed globally set
      loading: true,
      error: null,
    };
  },
  mounted() {
    this.fetchServiceDetails();
  },
  methods: {
    async fetchServiceDetails() {
      try {
        const serviceId = this.$route.params.id;
        const response = await this.$axios.get(`http://localhost:5000/api/service/${serviceId}`);
        this.service = response.data.service;
        this.professionals = response.data.pros;
      } catch (error) {
        this.error = "Failed to fetch service details. Please try again.";
        console.error("Error fetching service:", error.response?.data || error);
      } finally {
        this.loading = false;
      }
    },
    visitProfessional(proId) {
      this.$router.push(`/booking/${proId}`);
    }
  }
};
</script>

<style scoped>
/* Styling for buttons and hover effects */
.btn-primary {
  transition: transform 0.2s ease-in-out;
}
.btn-primary:hover {
  transform: scale(1.05);
}
</style>
