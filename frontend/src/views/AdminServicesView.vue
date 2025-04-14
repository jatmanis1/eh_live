<template>
  <div class="container mt-4">
    <!-- <div class="card shadow-sm mb-4 p-3">
      <div class="d-flex justify-content-between align-items-center">
        <h2 class="text-primary mb-0">All Services</h2>
        <div class="d-flex align-items-center">
          <input
            type="text"
            v-model="searchQuery"
            class="form-control me-2"
            placeholder="Search by ID, Name, or Description..."
          />
          <div>
          <button class="btn btn-primary" @click="showAddModal = true">
            <i class="bi bi-plus-lg"></i> Add Service
          </button>
          </div>
        </div>
      </div>
    </div> -->
    <div class="card shadow-sm mb-4">
      <div class="card-body d-flex justify-content-between align-items-center">
        <!-- <h2 class="text-primary mb-0">Welcome, {{ username }}!</h2> -->
        <h2 class="text-primary mb-0">All Services</h2>
        <div>
          <input
            v-model="searchQuery"
            type="text"
            class="form-control d-inline w-auto me-2"
            placeholder="Search by name"
          />
          <button class="btn btn-primary" @click="showAddModal = true">
            <i class="bi bi-plus-lg"></i> Add Service
          </button>
          <!-- <button @click="collect_data" class="btn btn-outline-primary me-2">
            <i class="bi bi-download"></i> Load Data
          </button>
          <button @click="logout" class="btn btn-outline-danger">
            <i class="bi bi-box-arrow-right"></i> Logout
          </button> -->
        </div>
      </div>
    </div>
    <!-- Loading Spinner -->
    <div v-if="loading" class="text-center my-4">
      <div class="spinner-border text-primary" role="status"></div>
      <p>Loading services...</p>
    </div>

    <!-- Services Table -->
    <div v-if="!loading">
      <table class="table table-striped table-hover text-center">
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Base Price</th>
            <th>Time Needed</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="service in filteredServices" :key="service.id">
            <td>{{ service.service_id }}</td>
            <td>{{ service.service_name }}</td>
            <td>{{ service.service_desc }}</td>
            <td>₹{{ service.service_b_price }}</td>
            <td>{{ service.time_required }} Hours</td>
            <td>
              <button class="btn btn-warning btn-sm me-2" @click="editService(service)">
                <i class="bi bi-pencil"></i> Edit
              </button>
              <button class="btn btn-danger btn-sm" @click="deleteService(service.id)">
                <i class="bi bi-trash"></i> Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- No Results Found -->
      <div v-if="filteredServices.length === 0" class="alert alert-warning text-center">
        No matching services found.
      </div>
    </div>
      <!-- Add Service Modal -->
      <div v-if="showAddModal" class="modal fade show d-block" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Add New Service</h5>
              <button type="button" class="btn-close" @click="showAddModal = false"></button>
            </div>
            <div class="modal-body">
              <input v-model="newService.service_name" class="form-control mb-2" placeholder="Service Name">
              <input v-model="newService.service_desc" class="form-control mb-2" placeholder="Description">
              <input v-model="newService.service_b_price" class="form-control mb-2" type="number" placeholder="Base Price">
              <input v-model="newService.time_required" class="form-control mb-2" type="number" placeholder="Time Required">
            </div>
            <div class="modal-footer">
              <button class="btn btn-secondary" @click="showAddModal = false">Cancel</button>
              <button class="btn btn-success" @click="addService">Add Service</button>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Edit Service Modal -->
      <div v-if="showEditModal" class="modal fade show d-block" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Edit Service</h5>
              <button type="button" class="btn-close" @click="showEditModal = false"></button>
            </div>
            <div class="modal-body">
              <input v-model="selectedService.service_name" class="form-control mb-2" placeholder="Service Name">
              <input v-model="selectedService.service_desc" class="form-control mb-2" placeholder="Description">
              <input v-model="selectedService.service_b_price" class="form-control mb-2" type="number" placeholder="Base Price">
              <input v-model="selectedService.time_required" class="form-control mb-2" type="number" placeholder="Time Required">
            </div>
            <div class="modal-footer">
              <button class="btn btn-secondary" @click="showEditModal = false">Cancel</button>
              <button class="btn btn-success" @click="saveService">Save</button>
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
      token: localStorage.getItem("token") || null,
      services: [],
        searchQuery: '',
        loading: false,
        currentPage: 1,
        totalPages: 1,
        showAddModal: false,
        showEditModal: false,
        newService: {
          service_name: '',
          service_desc: '',
          service_b_price: '',
          time_required: ''
        },
        selectedService: {},
      };
    },
    computed: {
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
        this.loading = true;
        try {
          const response = await this.$axios.get(`http://localhost:5000/api/admin/service?page=${this.currentPage}`);
          this.services = response.data.services;
          this.totalPages = response.data.total_pages;
        } catch (error) {
          console.error('Failed to fetch services:', error);
        } finally {
          this.loading = false;
        }
      },
      async addService() {
        try {
          await this.$axios.post(`http://localhost:5000/api/admin/service`, this.newService,
          {
            headers: {
              Authorization: `Bearer ${this.token}`,
            },
          });
          this.showAddModal = false;

          this.newService = { service_name: '', service_desc: '', service_b_price: '', time_required: '' };
          console.log(this.newService)
          this.fetchServices();
        } catch (error) {
          console.error('Error adding service:', error);
        }
      },
      editService(service) {
        this.selectedService = { ...service };
        this.showEditModal = true;
      },
      async saveService() {
        try {
          await this.$axios.put(`http://localhost:5000/api/admin/service/${this.selectedService.id}`, this.selectedService,
          {
            headers: {
              Authorization: `Bearer ${this.token}`,
            },
          }
          );
          this.showEditModal = false;
          this.fetchServices();
        } catch (error) {
          console.error('Error updating service:', error);
        }
      },
      async deleteService(id) {
        if (confirm('Are you sure you want to delete this service?')) {
          try {
            await this.$axios.delete(`http://localhost:5000/api/admin/service/${id}`);
            this.fetchServices();
          } catch (error) {
            console.error('Error deleting service:', error);
          }
        }
      }
    }
  };
  </script>