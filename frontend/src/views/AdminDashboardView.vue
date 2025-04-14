<template>
  <div class="d-flex">
    <div class="flex-grow-1 p-4">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm mb-4">
        <div class="container-fluid d-flex justify-content-between">
          <h5 class="mb-0">Admin Dashboard</h5>
          <div  class=" text-primary">
            Get Data Of Closed Requests in mail
          <a @click="triggerjob" class="btn btn-outline-primary me-2 ">
            <i class="bi bi-person-circle"></i> Send Now
          </a>
          </div>
        </div>
      </nav>

      <!-- Customer Status Table -->
      <div class="card shadow-sm p-3 mb-4">
        <h5 class="fw-bold"><i class="bi bi-people text-primary"></i> Customer Status</h5>
        <table class="table table-bordered text-center">
          <thead class="table-light">
            <tr>
              <th>Status</th>
              <th>Count</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, key) in adminData.cust_status" :key="key">
              <td>{{ key }}</td>
              <td class="fw-bold">{{ value }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Professional Status Table -->
      <div class="card shadow-sm p-3 mb-4">
        <h5 class="fw-bold"><i class="bi bi-tools text-danger"></i> Professional Status</h5>
        <table class="table table-bordered text-center">
          <thead class="table-light">
            <tr>
              <th>Status</th>
              <th>Count</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, key) in adminData.pro_status" :key="key">
              <td>{{ key }}</td>
              <td class="fw-bold">{{ value }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Request Status Table -->
      <div class="card shadow-sm p-3 mb-4">
        <h5 class="fw-bold"><i class="bi bi-list-check text-success"></i> Request Status</h5>
        <table class="table table-bordered text-center">
          <thead class="table-light">
            <tr>
              <th>Status</th>
              <th>Count</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, key) in adminData.req_status" :key="key">
              <td>{{ key }}</td>
              <td class="fw-bold">{{ value }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Manage Services Button -->
      <!-- <div class="text-center mt-4">
        <button class="btn btn-primary px-4 py-2" @click="manageServices">
          <i class="bi bi-gear"></i> Manage Services
        </button>
      </div> -->
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      adminData: {
        cust_status: {},
        pro_status: {},
        req_status: {}
      }
    };
  },
  methods: {

    async triggerjob() {
      try {
        const response = await this.$axios.get('http://localhost:5000/job1', {
          
        });

        if (response.data) {
          alert('data will be send on registred mail soon ~jatmanis1')
        } else {
          alert(`data send failed: ${response.data.message}`);
        }
      } catch (error) {
        alert(`data send failed: ${error.response?.data?.message || 'Unknown error'}`);
      }
    },


    async fetchAdminData() {
      try {
        const response = await this.$axios.get("http://localhost:5000/api/admindata");
        if (response.data) {
          this.adminData = this.formatAdminData(response.data);
        } else {
          alert("Failed to fetch admin data!");
        }
      } catch (error) {
        alert(`Error fetching data: ${error.response?.data?.message || "Unknown error"}`);
      }
    },
    formatAdminData(data) {
      return {
        cust_status: this.mapData(data.cust_status),
        pro_status: this.mapData(data.pro_status),
        req_status: this.mapData(data.req_status)
      };
    },
    mapData(data) {
      let mappedData = {};
      data.keys.forEach((key, index) => {
        mappedData[key] = data.values[index];
      });
      return mappedData;
    },
    manageServices() {
      alert("Redirecting to Manage Services...");
      this.$router.push("/admin/service");
    }
  },
  mounted() {
    this.fetchAdminData();
  }
};
</script>
