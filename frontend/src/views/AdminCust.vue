<template>
  <div id="home" class="container mt-4">
    <!-- Header Section -->
    <div class="card shadow-sm mb-4">
      <div class="card-body d-flex justify-content-between align-items-center">
        <h2 class="text-primary mb-0">Welcome, {{ $currentUser.username }}!</h2>
        <div class="mb-3">
          </div>
          <div>
            <input
                type="text"
                v-model="searchQuery"
                    class="form-control d-inline w-auto me-2"
                placeholder="Search by Name or Username..."
            />
          </div>
    
        
      </div>
    </div>

    

    <!-- Data Table Section -->
    <div v-if="Data1.length" class="card shadow-sm mx-auto">
      <div class="card-header bg-primary text-white text-center">
        <h3 class="mb-0">All Registered Customers</h3>
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-striped table-hover text-center align-middle">
            <thead class="table-dark">
              <tr>
                <th>#</th>
                <th>Name | Username</th>
                <th>Location</th>
                <th>Date Of Joining</th>
                <th>Rating</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(req, index) in filteredPros" :key="index">
                <td>{{ index + 1 }}</td>
                <td>
                  <strong>{{ req.name }}</strong><br>
                  <small class="text-muted">@{{ req.username }}</small>
                </td>
                <td>
                  <span class="d-block">{{ req.user_pincode }}</span>
                  <small class="text-muted">{{ req.user_address }}</small>
                </td>
                <td>{{ req.user_date }}</td>
                <td>
                  <span class="badge bg-warning text-dark">{{ req.user_rating }}</span>
                </td>
                <td>
                  <span :class="getStatusClass(req.user_status)" class="badge">
                    {{ req.user_status === 'archive' ? 'Archived' : req.user_status }}
                  </span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button v-if="req.user_status == 'unblocked'" @click.prevent="Block(req)" class="btn btn-warning btn-sm">
                      <i class="bi bi-lock-fill"></i> Block
                    </button>
                    <button v-if="req.user_status == 'blocked'" @click.prevent="Unblock(req)" class="btn btn-success btn-sm">
                      <i class="bi bi-unlock-fill"></i> Unblock
                    </button>
                    <button v-if="!req.is_verified" @click.prevent="Accept(req)" class="btn btn-primary btn-sm">
                      <i class="bi bi-check-circle"></i> Accept
                    </button>
                    <button v-if="!req.is_verified" @click.prevent="Reject(req)" class="btn btn-danger btn-sm">
                      <i class="bi bi-x-circle"></i> Reject
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="filteredPros.length === 0">
                <td colspan="7" class="text-center">No matching results found.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      Data1: [],
      searchQuery: '',
      token: localStorage.getItem('token') || null,
    };
  },
  computed: {
    filteredPros() {
      return this.Data1.filter(pro =>
        pro.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
        pro.username.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  mounted() {
    this.collect_data();
    if (this.token) this.getUserData();
  },
  methods: {
    async collect_data() {
      try {
        const response = await this.$axios.get('http://localhost:5000/api/admin/cust', {
          headers: { Authorization: `Bearer ${this.token}` },
        });
        this.Data1 = response.data.custs;
      } catch (error) {
        console.error('Failed to access data', error);
        alert('Access denied');
      }
    },
    getUserData() {
      try {
        const decodedToken = JSON.parse(atob(this.token.split('.')[1]));
        this.username = decodedToken.identity;
      } catch (error) {
        console.error('Error decoding token', error);
      }
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/login');
    },
    getStatusClass(status) {
      return status === 'reject' || status === 'ban'
        ? 'text-danger'
        : status === 'archive'
        ? 'text-secondary'
        : 'text-success';
    },
    async Unblock(req) {
      try {
        await this.$axios.put(`http://localhost:5000/api/admin/cust/${req.id}`, {
          id: req,
          status: 'unblocked',
        }, {
          headers: { Authorization: `Bearer ${this.token}` },
        });
        req.user_status = 'unblocked';
        this.collect_data();
      } catch (error) {
        console.error('Failed to unblock user', error);
      }
    },
    async Block(req) {
      try {
        await this.$axios.put(`http://localhost:5000/api/admin/cust/${req.id}`, {
          id: req,
          status: 'blocked',
        }, {
          headers: { Authorization: `Bearer ${this.token}` },
        });
        req.user_status = 'blocked';
        this.collect_data();
      } catch (error) {
        console.error('Failed to block user', error);
      }
    },
    async Accept(req) {
      try {
        await this.$axios.put(`http://localhost:5000/api/admin/cust/${req.id}`, {
          id: req,
          verify: '1',
        }, {
          headers: { Authorization: `Bearer ${this.token}` },
        });
        this.collect_data();
        req.is_verified = true;
      } catch (error) {
        console.error('Failed to accept user', error);
      }
    },
    async Reject(req) {
      try {
        await this.$axios.put(`http://localhost:5000/api/admin/cust/${req.id}`, {
          id: req,
          verify: '0',
        }, {
          headers: { Authorization: `Bearer ${this.token}` },
        });
        this.collect_data();
      } catch (error) {
        console.error('Failed to reject user', error);
      }
    },
  },
};
</script>

<style scoped>
.text-danger { color: red; }
.text-success { color: green; }
.text-secondary { color: gray; }
</style>
