<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { baseURL } from '@/data/services'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const handleLogin = async () => {
  try {
    const res = await axios.post(`${baseURL}/api/login`, {
      username: username.value,
      password: password.value
    })
    localStorage.setItem('token', res.data.token)
    router.push('/admin')
  } catch (err) {
    error.value = 'Invalid credentials'
  }
}
</script>

<template>
  <div class="container py-5">
    <div class="row justify-content-center">
      <div class="col-md-4">
        <h2 class="text-center mb-4">Internal Portal Login</h2>
        <div v-if="error" class="alert alert-danger">{{ error }}</div>
        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label class="form-label">Username</label>
            <input type="text" class="form-control" v-model="username" required>
          </div>
          <div class="mb-3">
            <label class="form-label">Password</label>
            <input type="password" class="form-control" v-model="password" required>
          </div>
          <button type="submit" class="btn btn-dark w-100">Login</button>
        </form>
        <p class="mt-3 text-muted text-center small">Demo: admin / slick2024</p>
      </div>
    </div>
  </div>
</template>
