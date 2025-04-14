<template>
  <div class="square-box" @click="redirect">
    <p class="text-2xl font-bold">{{ label }}</p>
    <div class="data-list">
      <p v-for="(num, idx) in data" :key="idx" class="text-lg">
        {{ dataLabels[idx] }}: {{ num }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    label: String,
    data: Array,
    dataLabels: Array, // Unique labels for each box
    link: String
  },
  methods: {
    redirect() {
      window.location.href = this.link;
    }
  }
};
</script>

<style scoped>
.square-box {
  width: 300px;
  height: 300px;
  background-color: #e0e0e0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  cursor: pointer;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  transition: background 0.3s;
  text-align: center;
}
.square-box:hover {
  background-color: #d6d6d6;
}
.data-list {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}
</style>
