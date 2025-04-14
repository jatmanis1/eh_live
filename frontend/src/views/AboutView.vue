<template>
  <div class="container my-5">
    <!-- Heading -->
    <div class="text-center mb-5">
      <h1 class="fw-bold display-5">About <span class="text-primary">EasyHome</span></h1>
      <p class="text-muted fs-5">
        Reliable, Professional, and Affordable Home Services
      </p>
      <hr class="w-25 mx-auto">
    </div>

    <!-- Introduction Section -->
    <div class="row align-items-center">
      <div class="col-lg-6 text-center mb-4">
        <img :src="serviceImage" alt="EasyHome Services" class="img-fluid rounded-3 shadow-lg">
      </div>
      <div class="col-lg-6">
        <h3 class="fw-semibold">Who We Are</h3>
        <p class="text-secondary lead">
          At <strong>EasyHome</strong>, we provide top-quality home maintenance services including 
          cleaning, appliance repair, plumbing, and electrical solutions. Our expert team ensures 
          high-quality service with customer satisfaction as our top priority.
        </p>
        <button class="btn btn-outline-primary btn-lg mt-3">Learn More</button>
      </div>
    </div>

    <!-- Our Services -->
    <div class="mt-5">
      <h3 class="text-center fw-semibold mb-4">Our Services</h3>
      <div class="row g-4">
        <div class="col-md-4">
          <div class="card shadow-sm border-0 text-center p-4">
            <div class="icon-box mb-3">
              <i class="bi bi-house-door text-primary fs-1"></i>
            </div>
            <h5 class="fw-bold">Home Cleaning</h5>
            <p class="text-muted">Professional cleaning services for a spotless home.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card shadow-sm border-0 text-center p-4">
            <div class="icon-box mb-3">
              <i class="bi bi-tools text-success fs-1"></i>
            </div>
            <h5 class="fw-bold">Appliance Repair</h5>
            <p class="text-muted">Reliable repairs for ACs, refrigerators, and more.</p>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card shadow-sm border-0 text-center p-4">
            <div class="icon-box mb-3">
              <i class="bi bi-lightning text-danger fs-1"></i>
            </div>
            <h5 class="fw-bold">Electrical & Plumbing</h5>
            <p class="text-muted">Expert solutions for all home maintenance needs.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Call to Action -->
    <div class="text-center mt-5 py-5 bg-light rounded-3 shadow">
      <h4 class="fw-bold">Need Home Services?</h4>
      <p class="text-muted fs-5">Book an appointment today and experience hassle-free service.</p>
      <button @click.revent="$router.push('/services')" class="btn btn-success btn-lg">Get a Quote</button>
    </div>
  </div>
</template>

<script>
import serviceImage from '@/assets/service_1.jpg';

export default {
  data() {
    return {
      serviceImage
    };
  }
};
</script>
