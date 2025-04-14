<template>
    <div class="max-w-3xl mx-auto p-6 bg-white rounded-xl shadow-lg">
      <!-- Profile Header -->
      <h2 class="text-3xl font-semibold text-center mb-6 text-gray-800">User Profile</h2>
  
      <!-- Profile Grid -->
      <div class="grid grid-cols-2 gap-6">
        <!-- Left Column -->
        <div class="p-4 bg-gray-100 rounded-lg shadow">
          <p class="text-lg"><strong>Name:</strong> {{ user.user_name }}</p>
          <p class="text-lg"><strong>Username:</strong> {{ user.user_username }}</p>
          <p class="text-lg"><strong>Email:</strong> {{ user.user_email }}</p>
          <p class="text-lg"><strong>Address:</strong> {{ user.user_address }}</p>
          <p class="text-lg"><strong>Pincode:</strong> {{ user.user_pincode }}</p>
        </div>
  
        <!-- Right Column -->
        <div class="p-4 bg-gray-100 rounded-lg shadow">
          <p class="text-lg"><strong>Role:</strong> {{ user.user_role }}</p>
          <p class="text-lg"><strong>Experience:</strong> {{ user.user_exp || "N/A" }}</p>
          <p class="text-lg"><strong>Description:</strong> {{ user.user_desc || "N/A" }}</p>
          <p class="text-lg"><strong>Rating:</strong> ⭐ {{ user.user_rating }}</p>
          <p class="text-lg"><strong>Status:</strong> <span :class="getStatusClass(user.user_status)">{{ user.user_status }}</span></p>
        </div>
      </div>
  
      <!-- Edit Button -->
      <div class="text-center mt-6">
        <button @click="openEditModal" class="px-6 py-2 bg-primary text-white rounded-lg hover:bg-blue-700 shadow-md">
          Edit Profile
        </button>
      </div>
  
      <!-- Edit Profile Modal -->
      <div v-if="isEditModalOpen" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white p-6 rounded-lg shadow-lg w-96">
          <h3 class="text-xl font-semibold mb-4 text-gray-800">Edit Profile</h3>
  
          <div class="space-y-3">
            <label class="block text-sm font-semibold">Name:</label>
            <input v-model="editUser.user_name" class="w-full border rounded p-2" />
  
            <label class="block text-sm font-semibold">Email:</label>
            <input v-model="editUser.user_email" class="w-full border rounded p-2" />
  
            <label class="block text-sm font-semibold">Address:</label>
            <input v-model="editUser.user_address" class="w-full border rounded p-2" />
  
            <label class="block text-sm font-semibold">Pincode:</label>
            <input v-model="editUser.user_pincode" class="w-full border rounded p-2" />
  
            <label class="block text-sm font-semibold">Experience:</label>
            <input v-model="editUser.user_exp" class="w-full border rounded p-2" />
  
            <label class="block text-sm font-semibold">Description:</label>
            <textarea v-model="editUser.user_desc" class="w-full border rounded p-2"></textarea>
          </div>
  
          <!-- Modal Buttons -->
          <div class="flex justify-end mt-4">
            <button @click="saveProfile" class="px-4 py-2 bg-info text-white rounded-lg hover:bg-primary mr-2 shadow-md">
              Save
            </button>
            <button @click="isEditModalOpen = false" class="px-4 py-2 bg-secondary text-white rounded-lg hover:bg-warning shadow-md">
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        user: {}, // Store user data
        editUser: {}, // Store editable user data
        isEditModalOpen: false, // Controls edit modal
      };
    },
    methods: {
      async fetchUser() {
        try {
          const token = localStorage.getItem("token"); // Retrieve token from storage
          if (!token) {
            console.error("JWT Token missing!");
            return;
          }
  
          const response = await axios.get("http://localhost:5000/api/profile", {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
  
          this.user = response.data;
        } catch (error) {
          console.error("Profile Fetch error:", error.response || error);
        }
      },
      openEditModal() {
        this.editUser = { ...this.user };
        this.isEditModalOpen = true;
      },
      async saveProfile() {
        try {
          const token = localStorage.getItem("token"); // Ensure token is sent
          if (!token) {
            console.error("JWT Token missing!");
            return;
          }
  
          await axios.put("http://localhost:5000/api/profile", this.editUser, {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
  
          this.user = { ...this.editUser };
          this.isEditModalOpen = false;
        } catch (error) {
          console.error("Error updating profile:", error.response || error);
        }
      },
      getStatusClass(status) {
        return status === "Active" ? "text-green-600 font-semibold" : "text-red-600 font-semibold";
      },
    },
    mounted() {
      this.fetchUser();
    },
  };
  </script>
  