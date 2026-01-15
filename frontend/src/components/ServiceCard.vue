<script setup lang="ts">
defineProps<{
  id: string
  title: string
  description: string
  imageUrl: string
}>()
</script>

<template>
  <div :id="id" class="row align-items-center mb-5 pt-5">
    <div class="col-md-6">
      <img :src="imageUrl" :alt="title" class="img-fluid rounded shadow" />
    </div>
    <div class="col-md-6">
      <h3>{{ title }}</h3>
      <p class="lead">{{ description }}</p>
      <router-link to="/contact" class="btn btn-primary">Get a Quote</router-link>
    </div>
  </div>
</template>
