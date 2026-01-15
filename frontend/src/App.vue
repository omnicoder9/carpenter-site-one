<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { RouterLink, RouterView } from 'vue-router'

interface ServiceItem {
  id: string;
  title: string;
}

interface ServiceCategory {
  id: string;
  title: string;
  items: ServiceItem[];
}

const categories = ref<ServiceCategory[]>([])

onMounted(async () => {
  try {
    const res = await axios.get('/api/services')
    categories.value = res.data
  } catch (err) {
    console.error("Failed to load services", err)
  }
})
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container">
      <RouterLink class="navbar-brand" to="/">Slick Cabinets</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
              Services
            </a>
            <ul class="dropdown-menu">
              <li v-for="cat in categories" :key="cat.id">
                <h6 class="dropdown-header">{{ cat.title }}</h6>
                <RouterLink 
                  v-for="item in cat.items" 
                  :key="item.id" 
                  class="dropdown-item" 
                  :to="{ name: 'home', hash: '#' + item.id }"
                >
                  {{ item.title }}
                </RouterLink>
                <li><hr class="dropdown-divider" v-if="cat !== categories[categories.length-1]"></li>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/reviews">Reviews</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/contact">Contact Me</RouterLink>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/login">Internal Portal</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <RouterView />

  <footer class="bg-dark text-white text-center py-3 mt-5">
    <div class="container">
      <p class="mb-0">&copy; 2026 Slick Cabinets. All rights reserved.</p>
    </div>
  </footer>
</template>

<style scoped>
/* Scoped styles if needed */
</style>
