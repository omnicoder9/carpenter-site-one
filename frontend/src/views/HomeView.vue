<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ServiceCard from '../components/ServiceCard.vue'

interface ServiceItem {
  id: string;
  title: string;
  description: string;
  image_url: string;
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
    console.error(err)
  }
})
</script>

<template>
  <div>
    <div class="hero mb-5">
      <div class="container">
        <h1 class="display-3">Slick Cabinets</h1>
        <p class="lead">Premium Custom Cabinetry & Woodworking</p>
        <router-link to="/contact" class="btn btn-light btn-lg mt-3">Start Your Project</router-link>
      </div>
    </div>

    <div class="container">
      <div v-for="cat in categories" :key="cat.id" class="mb-5">
        <h2 class="border-bottom pb-2 mb-4">{{ cat.title }}</h2>
        <ServiceCard 
          v-for="item in cat.items"
          :key="item.id"
          :id="item.id"
          :title="item.title"
          :description="item.description"
          :image-url="item.image_url"
        />
      </div>
    </div>
  </div>
</template>
