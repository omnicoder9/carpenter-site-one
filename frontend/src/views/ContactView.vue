<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const form = ref({
  name: '',
  email: '',
  message: ''
})

const status = ref('')
const loading = ref(false)

const submitForm = async () => {
  loading.value = true
  status.value = ''
  try {
    await axios.post('/api/contact', form.value)
    status.value = 'success'
    form.value = { name: '', email: '', message: '' }
  } catch (err) {
    status.value = 'error'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="container py-5">
    <h1 class="mb-4">Contact Us</h1>
    <div class="row">
      <div class="col-md-6">
        <p class="lead">Ready to transform your space? Send us a message.</p>
        <ul class="list-unstyled">
          <li><strong>Email:</strong> info@slickcabinets.com</li>
          <li><strong>Phone:</strong> (555) 123-4567</li>
          <li><strong>Address:</strong> 123 Woodwork Way, Craftsville</li>
        </ul>
      </div>
      <div class="col-md-6">
        <div v-if="status === 'success'" class="alert alert-success">
          Message sent successfully! We'll get back to you soon.
        </div>
        <div v-if="status === 'error'" class="alert alert-danger">
          Something went wrong. Please try again later.
        </div>

        <form @submit.prevent="submitForm">
          <div class="mb-3">
            <label for="name" class="form-label">Name</label>
            <input type="text" class="form-control" id="name" v-model="form.name" required>
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" class="form-control" id="email" v-model="form.email" required>
          </div>
          <div class="mb-3">
            <label for="message" class="form-label">Message</label>
            <textarea class="form-control" id="message" rows="5" v-model="form.message" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary" :disabled="loading">
            {{ loading ? 'Sending...' : 'Send Message' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>
