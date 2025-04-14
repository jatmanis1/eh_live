<template>
  <div class="container mt-4">
    <!-- Header Section -->
    <div class="d-flex justify-content-between align-items-center bg-light p-3 rounded shadow-sm">
      <h2 class="text-primary mb-0">{{ welcomeMessage }}</h2>
      <div class="input-group" style="max-width: 300px;">
        <input type="text" class="form-control" v-model="searchQuery" placeholder="Search Service">
        <button class="btn btn-outline-primary" type="submit">
          <i class="bi bi-search"></i>
        </button>
      </div>
    </div>

    <!-- Call-to-action -->
    <div class="text-center mt-3">
      <p class="fw-bold text-muted">Find the best services tailored just for you! 🚀</p>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="text-center mt-4">
      <p class="text-primary">Fetching services... Please wait <i class="bi bi-hourglass-split"></i></p>
    </div>

    <!-- No Services Found -->
    <div v-else-if="filteredServices.length === 0" class="text-center mt-4">
      <p class="text-danger">Oops! No matching services found. Try a different search! 🔍</p>
    </div>

    <!-- Services Grid -->
    <div v-else class="row mt-4">
      <div v-for="service in filteredServices" :key="service.id" class="col-md-4 mb-4">
        <div 
          class="card shadow-sm h-100 text-center p-3 service-card" 
          @click="$router.push(`/servicepage/${service.id}`)" 
          style="cursor: pointer;"
        >
          <div class="card-body">
            <h5 class="card-title text-danger">{{ service.service_name }}</h5>
            <p class="card-text text-muted">{{ service.service_desc }}</p>
            <p class="fw-bold text-purple">₹ {{ service.service_b_price }}</p>
            <p class="text-dark">
              Needs <b class="text-white bg-dark px-2 py-1 rounded">{{ service.time_required }} h</b> to complete
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      services: [],
      loading: true,
    };
  },
  computed: {
    welcomeMessage() {
      const hour = new Date().getHours();
      if (hour < 12) return "Good Morning! 🌞 Explore Our Services";
      else if (hour < 18) return "Good Afternoon! ☀️ Find What You Need";
      else return "Good Evening! 🌙 Discover Top Services";
    },
    filteredServices() {
      return this.services.filter(service =>
        service.service_name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  mounted() {
    this.fetchServices();
  },
  methods: {
    async fetchServices() {
      try {
        const response = await this.$axios.get('http://localhost:5000/api/admin/service');
        this.services = response.data.services;
      } catch (error) {
        console.error('Failed to fetch services:', error.response?.data || error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.service-card {
  transition: transform 0.2s ease-in-out, box-shadow 0.3s ease-in-out;
}
.service-card:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}
</style>
