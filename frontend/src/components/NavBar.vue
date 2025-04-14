<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
    <div class="container">
      <a class="navbar-brand fw-bold" href="#">
        <i class="bi bi-house-door"></i> EasyHome
      </a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav" v-if="$currentUser">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item" >
            <a class="nav-link" v-if="$currentUser.user_role==='admin'" @click.prevent="$router.push('/admindashboard')" style="cursor: pointer;">Home</a>
            <a class="nav-link" v-else @click.revent="$router.push('/dashboard')" style="cursor: pointer;">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click.prevent="$router.push('/services')" style="cursor: pointer;">Services</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click.prevent="$router.push('/about')" style="cursor: pointer;">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click.prevent="$router.push('/contact')" style="cursor: pointer;">Contact</a>
          </li>
          <li class="nav-item dropdown" v-if="$currentUser.user_role==='admin'">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
              <i class="bi bi-person-circle"></i> Users
            </a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item"      style="cursor: pointer;"  @click.prevent="$router.push('/admin/pro')"><i class="bi bi-person"></i> Proffesionals</a></li>
              <li><a class="dropdown-item"      style="cursor: pointer;"  @click.prevent="$router.push('/admin/cust')"><i class="bi bi-gear"></i> Customers</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item text-info" style="cursor: pointer;" @click.prevent="$router.push('/admin/service')"><i class="bi bi-box-arrow-right"></i> Services</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
              <i class="bi bi-person-circle"></i> Account
            </a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item"      style="cursor: pointer;"  @click.prevent="$router.push('/profile')"><i class="bi bi-person"></i> Profile</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item text-danger" style="cursor: pointer;" @click.prevent="logout"><i class="bi bi-box-arrow-right"></i> Logout</a></li>
            </ul>
          </li>
          
        </ul>
      </div>
      <div class="collapse navbar-collapse" id="navbarNav" v-else>
        <ul class="navbar-nav ms-auto">
          
          <li class="nav-item">
            <a class="nav-link" @click.prevent="$router.push('/services')" style="cursor: pointer;">Services</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click.prevent="$router.push('/about')" style="cursor: pointer;">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click.prevent="$router.push('/login')" style="cursor: pointer;">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click.prevent="$router.push('/register')" style="cursor: pointer;">Register</a>
          </li>

          
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  methods: {
    logout() {
      alert("Logging out..."); 
      localStorage.removeItem("token");
      localStorage.removeItem("user");
      this.token = null;
      this.$router.replace("/login");
    },
    }
  // }
};
</script>

<style scoped>
/* Navbar Hover Effects */
.navbar-nav .nav-link {
  transition: all 0.3s ease-in-out;
}

.navbar-nav .nav-link:hover {
  color: #ffffff !important;
  text-decoration: underline;
}

/* Dropdown Styling */
.dropdown-menu {
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.dropdown-item:hover {
  background-color: #f8f9fa;
}
</style>
