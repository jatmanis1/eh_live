<template>
  <div class="container mt-4">
    <div class="card shadow-sm mb-4">
      <div class="card-body d-flex justify-content-between align-items-center">
        <h2 class="text-primary mb-0">{{ welcomeMessage }}</h2>
        <h2 class="text-primary mb-0">Welcome, {{ $currentUser.username }}!</h2>
        <div>
          <button @click="getProtectedData" class="btn btn-outline-primary me-2">
            <i class="bi bi-download"></i> Load Data
          </button>
          <button @click="logout" class="btn btn-outline-danger">
            <i class="bi bi-box-arrow-right"></i> Logout
          </button>
        </div>
      </div>
    </div>

    <div class="card shadow-lg border-0 rounded mb-4">
      <div class="card-body">
        <h5 class="card-title text-primary text-center">User Information</h5>
        <table class="table table-borderless">
          <tbody>
            <tr>
              <td><strong>Address:</strong></td>
              <td>{{ $currentUser.user_address }} | {{ $currentUser.user_pincode }}</td>
            </tr>
            <tr>
              <td><strong>Joined On:</strong></td>
              <td>{{ $currentUser.user_date }}</td>
            </tr>
            <tr>
              <td><strong>Status:</strong></td>
              <td>
                <span :class="getStatusClass($currentUser.user_status)">
                  {{ getStatusText($currentUser.user_status) }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-if="protectedData" class="card shadow-sm mx-auto">
      <div class="card-header bg-primary text-white text-center">
        <h3 class="mb-0">{{ capitalize($currentUser.user_role) }} Dashboard</h3>
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <button v-if="$currentUser.user_role == 'cust'" @click="$router.push('/services')"
            class="btn btn-outline-danger">
            <i class="bi bi-box-arrow-right"> Request New Service</i>
          </button>
          <table class="table table-striped table-hover text-center align-middle">
            <thead class="table-dark">
              <tr>
                <th>S No.</th>
                <th v-if="$currentUser.user_role === 'cust'">Professional</th>
                <th v-else-if="$currentUser.user_role === 'pro'">Customer</th>
                <th v-if="$currentUser.user_role === 'cust'">Service</th>
                <th>Location</th>
                <th>Requested On</th>
                <th>Last Action On</th>
                <th>Completed On</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(req, index) in protectedData?.request_created" :key="index">
                <td>{{ index + 1 }}</td>
                <td v-if="$currentUser.user_role === 'cust'">{{ req.pro.name }} <br>
                  <small class="text-muted">@{{ req.pro.username }}</small></td>
                <td v-else-if="$currentUser.user_role === 'pro'">{{ req.cust.name }}<br>
                  <small class="text-muted">@{{ req.cust.username }}</small></td>
                <td v-if="$currentUser.user_role === 'cust'">{{ req.service.service_name }}</td>
                <td>{{ req.pro.user_pincode || req.cust.user_pincode }}<br>
                  <small class="text-muted">{{ req.pro.user_address || req.cust.user_address }}</small></td>
                <td>{{ req.req_date }}</td>
                <td>{{ req.req_action_date }}</td>
                <td>{{ req.req_completed_date }}</td>
                <td>
                  <span :class="getStatusClass(req.req_status)">{{ req.req_status }}</span>
                </td>
                <td>
                  <div v-if="$currentUser.user_role === 'cust' && req.req_status === 'Accepted'">
                    <button class="btn btn-sm btn-danger" @click="openModal(req.id, 'close')">Close Request</button>
                  </div>
                  <div v-else-if="$currentUser.user_role === 'pro' && req.req_status === 'Pending'">
                    <button class="btn btn-sm btn-success me-2" @click.prevent="reqAccept(req.id)">Accept</button>
                    <button class="btn btn-sm btn-danger" @click.prevent="reqReject(req.id)">Reject</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="modal fade show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirm Action</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <input v-model="rating" class="input-box" max="5" min="1" placeholder="Rate service out of 5" type="number">
            <input v-model="remarks" class="input-box" placeholder="Write your remarks" type="text">
            <p>Are you sure you want to close this request?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">Cancel</button>
            <button type="button" class="btn btn-primary" @click="reqClose(selectedRequestId)">Close Now</button>
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
      protectedData: null,
      token: localStorage.getItem("token") || null,
      showModal: false,
      rating: 0,
      remarks: null,
    };
  },
  computed: {
    welcomeMessage() {
      const hour = new Date().getHours();
      return hour < 12 ? "Good Morning! 🌞" : hour < 18 ? "Good Afternoon! ☀️" : "Good Evening! 🌙";
    },
  },
  mounted() {
    if (this.token) this.getProtectedData();
  },
  methods: {
    openModal(req_id) { this.selectedRequestId = req_id; this.showModal = true; },
    closeModal() { this.showModal = false; this.selectedRequestId = null; },
    capitalize(str) { return str.charAt(0).toUpperCase() + str.slice(1); },
    logout() { localStorage.clear(); this.$router.replace("/login"); },
  },
};
</script>

<style scoped>
.btn { min-width: 150px; }
</style>