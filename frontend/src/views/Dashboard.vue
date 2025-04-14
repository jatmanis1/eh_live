<template>
  <div class="container mt-4">

    <div class="card shadow-sm mb-4">
      <div class="card-body d-flex justify-content-between align-items-center">
      <h2 class="text-primary mb-0">{{ welcomeMessage }}</h2>
      <h2 class="text-primary mb-0">Welcome, {{ $currentUser.username }}!</h2>

        <!-- <div>
          <button @click="collect_data" class="btn btn-outline-primary me-2">
            <i class="bi bi-download"></i> Load Data
          </button>
          <button @click="logout" class="btn btn-outline-danger">
            <i class="bi bi-box-arrow-right"></i> Logout
          </button>
        </div> -->
      </div>
    </div>
    <!-- User Info Card -->
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


    <!-- Data Table Section -->
    <div v-if="protectedData" class="card shadow-sm  mx-auto">
      <div class="card-header bg-primary text-white text-center">
        <h3 class="mb-0">{{ capitalize($currentUser.user_role) }} Dashboard</h3>
      </div>
      <div class="card-body ">
        <div class="table-responsive">
           <button    v-if="$currentUser.user_role =='cust'"     @click="$router.push(`/services`)"
           class="btn btn-outline-danger">
            <i class="bi bi-box-arrow-right">  Request New Service</i> 
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
                <th>Review</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody v-if="protectedData">
              <tr v-for="(req, index) in protectedData?.request_created" :key="index">
            <!-- <tbody>
              <tr v-for="(req, index) in Data1" :key="index"> -->
                <td>{{ index + 1 }}</td>

                    <td v-if="$currentUser.user_role === 'cust'">{{ req.pro.name }} <br> 
                      <small class="text-muted">@{{ req.pro.username }}</small></td>
                <td v-else-if="$currentUser.user_role === 'pro'">{{ req.cust.name }}<br> 
                  <small class="text-muted">@{{ req.cust.username }}</small></td>
                <td v-if="$currentUser.user_role === 'cust'">{{ req.service.service_name }}</td>
                <td v-if="$currentUser.user_role ==='cust' ">
                  <span class="d-block">{{ req.pro.user_pincode }}</span>
                  <small class="text-muted">{{ req.pro.user_address }}</small>
                </td>
                <td v-else>
                  <span class="d-block">{{ req.cust.user_pincode }}</span>
                  <small class="text-muted">{{ req.cust.user_address }}</small>
                </td>
                <td>{{ req.req_date }}</td>
                <td>{{ req.req_action_date }}</td>
                <td>{{ req.req_completed_date }}</td>
                
                <td>
                  <span :class="getStatusClass(req.req_status)">
                    {{ req.req_status }}
                  </span>
                </td>
                <td >
                  <div v-if="req.req_rating">
                  {{ req.req_rating }} 
                </div>
                <div  v-if="req.req_remark">
                  <!-- {{ req.req_remark }}  -->
                  <small class="text-muted">~{{ req.req_remark}}</small>
                </div>
                
                </td>
                <td>
                  <div v-if="$currentUser.user_role === 'cust' && req.req_status === 'Accepted'">
                    <a href="#" class="btn btn-sm btn-danger" @click="openModal(req, 'close')">Close Request</a>
                  </div>
                  <div v-else-if="$currentUser.user_role === 'pro' && req.req_status === 'Pending'">
                    <a href="#" class="btn btn-sm btn-success me-2" @click.prevent="reqAccept(req.id)">Accept</a>
                    <a href="#" class="btn btn-sm btn-danger" @click.prevent="reqReject(req.id)">Reject</a>
                  </div>
                  <div v-else-if="$currentUser.user_role === 'cust' && req.req_status === 'Closed'">
                    <a href="#" class="btn btn-sm btn-info me-2" @click="openModal(req, 'edit')">Edit</a>
                  </div>
                    <!-- <div v-else> 
                      <a href="#" class="btn btn-sm btn-warning disable me-2" @click.prevent="reqAccept(req.id)">Accept</a>
                  </div> -->
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      <!-- </div> -->
    </div>
  </div>

    <!-- Logout Button -->
    <!-- <div class="text-center mt-4"> -->
      <!-- <button class="btn btn-danger" @click="logout">Logout</button> -->
    <!-- </div> -->

    <!-- Debugging -->
    <!-- <pre class="mt-4">{{ protectedData }}</pre> -->
  </div>

  <!-- model  -->
  <!-- <div v-if="showModal" class="modal fade show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirm Action</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
        <input v-model="selectedReq.req_rating" class="input-box" id="exp" max="5" min="1" placeholder="rate our service out of 5" type="number" ><br>
        <input v-model="selectedReq.req_remark" class="input-box" id="exp" placeholder="write your remarks" type="text" ><br>


            <p>Are you sure you want to close this request?</p>

          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">Cancel</button>
            <button type="button" class="btn btn-primary" @click="reqClose(selectedRequestId)">Close Now</button>
          </div>
        </div>
      </div>
    </div> -->
    <div v-if="showModal" class="modal fade show d-block" tabindex="-1">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content shadow-lg rounded-3">
      
      <!-- Modal Header -->
      <div class="modal-header bg-primary text-white">
        <h5 class="modal-title">Confirm Action</h5>
        <button type="button" class="btn-close" @click="closeModal"></button>
      </div>

      <!-- Modal Body -->
      <div class="modal-body px-4">
        <p class="mb-3 fw-semibold text-secondary">
          Please rate our service and leave a remark before closing this request.
        </p>

        <!-- Rating Input -->
        <div class="mb-3">
          <label for="exp-rating" class="form-label fw-bold">Rate Our Service (1-5)</label>
          <input 
            v-model="selectedReq.req_rating" 
            class="form-control border-primary" 
            id="exp-rating" 
            max="5" 
            min="1" 
            placeholder="Enter rating (1-5)" 
            type="number"
          >
        </div>

        <!-- Remarks Input -->
        <div class="mb-3">
          <label for="exp-remark" class="form-label fw-bold">Your Remarks</label>
          <textarea 
            v-model="selectedReq.req_remark" 
            class="form-control border-primary" 
            id="exp-remark" 
            rows="3" 
            placeholder="Write your remarks here..."
          ></textarea>
        </div>

        <p v-if="actionType==='close'" class="text-danger fw-bold">Are you sure you want to close this request?</p>
      </div>

      <!-- Modal Footer -->
      <div class="modal-footer d-flex justify-content-between px-4 pb-3">
        <button type="button" class="btn btn-secondary px-4 py-2" @click="closeModal">
          Cancel
        </button>
       
        <button v-if="actionType==='close'"  type="button" class="btn btn-danger px-4 py-2" @click="reqClose(selectedRequestId)">
          Close Now 
        </button>
        <button v-else  type="button" class="btn btn-danger px-4 py-2" @click="reqEdit(selectedRequestId)">
          Edit
        </button>
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
      modalTitle: "",
      modalMessage: "",
      actionType: null,
      requestId: null,
      showModal: false,
      rating: 0,
      remarks: null,

    };
  },
      computed: {
    welcomeMessage() {
      const hour = new Date().getHours();
      if (hour < 12) return "Good Morning! 🌞";
      else if (hour < 18) return "Good Afternoon! ☀️ ";
      else return "Good Evening! 🌙";
    }
  },
  mounted() {
    if (this.token) {
      this.getProtectedData();
    }
  },
  methods: {
    openModal(req, action) {
      this.selectedReq = req;
      this.selectedRequestId = req.id;
      console.log(this.selectedRequestId)
      console.log(this.selectedReq.req_remark)
      console.log(this.selectedReq.req_rating)
      this.actionType = action;
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
      this.selectedRequestId = null;
      this.selectedReq = null;
      this.actionType = '';
    },

    capitalize(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    },
    async getProtectedData() {
      try {
        const response = await this.$axios.get("http://localhost:5000/api/user", {
          headers: { Authorization: `Bearer ${this.token}` },
        });
        this.protectedData = response.data;
      } catch (error) {
        console.error("Failed to access protected route:", error.response?.data || error);
        alert("Access denied");
      }
    },
    async reqAccept(req_id) {
      try {
        const response = await this.$axios.put(
          `http://localhost:5000/api/user/${req_id}`,
          { update: "accept" 

          },
          {
            headers: { Authorization: `Bearer ${this.token}` },
          }
        );
        this.protectedData = response.data;
        this.getProtectedData();
      } catch (error) {
        console.error("Error updating request:", error.response?.data || error);
        alert("Request failed");
      }
    },
    async reqReject(req_id) {
      try {
        const response = await this.$axios.put(
          `http://localhost:5000/api/user/${req_id}`,
          { update: "reject" },
          {
            headers: { Authorization: `Bearer ${this.token}` },
          }
        );
        this.protectedData = response.data;
        this.getProtectedData();
      } catch (error) {
        console.error("Error updating request:", error.response?.data || error);
        alert("Request failed");
      }
    },
    async reqClose(req_id) {
      try {
        const response = await this.$axios.put(
          `http://localhost:5000/api/user/${req_id}`,
          { update: "close",
          req_rating: this.selectedReq.req_rating,
          req_remarks: this.selectedReq.req_remark,
           },
          {
            headers: { Authorization: `Bearer ${this.token}` },
          }
        );
        this.protectedData = response.data;
        this.showModal = false;
        this.getProtectedData();

      } catch (error) {
        console.error("Error updating request:", error.response?.data || error);
        alert("Request failed");
      }
    },
    async reqEdit(req_id) {
      try {
        const response = await this.$axios.put(
          `http://localhost:5000/api/user/${req_id}`,
          { 
            update: "edit",

            req: this.selectedReq,
            req_rating: this.selectedReq.req_rating,
            req_remarks: this.selectedReq.req_remark,
           }, 
          {
            headers: { Authorization: `Bearer ${this.token}` },
          }
        );
        this.protectedData = response.data;
        this.showModal = false;
        this.getProtectedData();

      } catch (error) {
        console.error("Error updating request:", error.response?.data || error);
        alert("Request failed");
      }
    },
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("user");
      this.token = null;
      this.$router.replace("/login");
    },
    redirectToServices() {
      this.$router.push("/services");
    },
    getStatusClass(status) {
      return {
        badge: true,
        "bg-success": status === "Accepted" || status === "unblocked",
        "bg-danger": status === "Rejected" || status === "blocked",
        "bg-secondary": status === "Archived" || status === "archive",
        "bg-warning": status === "Pending",
        "bg-info": status === "Closed",
      };
    },
    getStatusText(status) {
      return status === "archive"
        ? "Archived"
        : status === "allow"
        ? "Allowed"
        : status || "None";
    },
  },
};
</script>

<style scoped>
.btn {
  min-width: 150px;
}
</style>   