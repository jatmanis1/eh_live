<template>
  <div class="container mt-4">
    <div class="booking-box">
      <div v-if="flag" class="success-box">
        <h1>Booking Successful 🎉</h1>
        <h2>Go To <router-link to="/dashboard" class="dashboard-link">Dashboard</router-link></h2>
      </div>

      <div v-else>
        <ul v-if="messages.length" class="message-box">
          <li v-for="(message, index) in messages" :key="index" v-html="message"></li>
        </ul>
        <div v-else class="service-details">
          <h1 class="service-title">{{ s1.pro_name }}</h1>
          <form @submit.prevent="bookService">
            <button type="submit" class="btn-book">📅 Book Now</button>
          </form>
        </div>
      </div>
    </div>

    <!-- Recent Services Section -->
    <h2 class="table-label">Recent Services</h2>
    <div class="service-container">
      <div v-for="service in service_h" :key="service.id" class="service-box">
        <div class="service-header">
          <b class="customer-name">{{ service.req_cust }}</b>
        </div>
        <div class="service-body">
          <b class="date">{{ service.req_completed_date }}</b>
        </div>
        <div class="rating">
          <span v-for="star in service.req_rating" :key="star">⭐</span>
        </div>
        <div v-if="service.req_remark" class="remark">
          <span>{{ service.req_remark }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      flag: false, // Will be set from API response
      messages: [], // Flash messages
      s1: {}, // Service details
      service_h: [], // Recent services
      token: localStorage.getItem("token") || null, // Fetch token from local storage
    };
  },
  methods: {
    async fetchServiceDetails() {
      try {
        const proId = this.$route.params.id; // Get service ID from route
        const response = await this.$axios.get(
          `http://localhost:5000/api/booking/${proId}`,
          {
            headers: {
              Authorization: `Bearer ${this.token}`,
            },
          }
        );
        this.s1 = response.data.service;
        this.service_h = response.data.recent_services || [];

      } catch (error) {
        console.error("Error fetching service details:", error);
      }
    },
    async bookService() {
      try {
        const proId = this.$route.params.id; // Get service ID from route
        const response = await this.$axios.post(
          `http://localhost:5000/api/booking/${proId}`,
          {},
          {
            headers: {
              Authorization: `Bearer ${this.token}`,
            },
          }
        );

        this.msg = response.data.msg
        if (response.data.success) {
          this.flag = true; // Booking success
        } else {
          this.messages.push(response.data.message);
        }
        alert(`Booking update: ${this.msg}`);
      }catch (error) {
        alert(`Booking error:, ${this.msg}`);
      }
    },
  },
  mounted() {
    this.fetchServiceDetails();
  },
};
</script>

<style scoped>
.container {
  max-width: 700px;
  margin: auto;
  text-align: center;
}

.booking-box {
  background: #fff4e6;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.success-box {
  background: #d4edda;
  color: #155724;
  padding: 15px;
  border-radius: 8px;
  font-weight: bold;
}

.dashboard-link {
  color: #007bff;
  text-decoration: none;
  font-weight: bold;
}

.message-box {
  background: #ffcccc;
  padding: 10px;
  border-radius: 8px;
  color: #721c24;
  font-weight: bold;
}

.service-details {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  margin-top: 10px;
}

.service-title {
  color: #c82333;
  font-weight: bold;
}

.btn-book {
  background: #007bff;
  color: white;
  padding: 10px 20px;
  font-size: 18px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: 0.3s;
}

.btn-book:hover {
  background: #0056b3;
}

.table-label {
  margin-top: 20px;
  font-size: 24px;
  font-weight: bold;
}

.service-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
}

.service-box {
  background: #fff;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  width: 250px;
}

.service-header {
  font-size: 18px;
  font-weight: bold;
  color: #c12f2f;
}

.date {
  color: #2d7773;
}

.rating {
  color: #ffc107;
  font-size: 20px;
}

.remark {
  font-style: italic;
  color: #333;
}
</style>
