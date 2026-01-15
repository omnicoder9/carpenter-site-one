<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const messages = ref([
  { id: 1, from: 'Alice', subject: 'Quote for Kitchen', date: '2023-10-25' },
  { id: 2, from: 'Bob', subject: 'Repair question', date: '2023-10-26' }
])

onMounted(() => {
  if (!localStorage.getItem('token')) {
    router.push('/login')
  }
})

const logout = () => {
  localStorage.removeItem('token')
  router.push('/login')
}
</script>

<template>
  <div class="container py-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1>Admin Dashboard</h1>
      <button @click="logout" class="btn btn-outline-danger">Logout</button>
    </div>
    
    <div class="card">
      <div class="card-header">
        Recent Inquiries
      </div>
      <ul class="list-group list-group-flush">
        <li v-for="msg in messages" :key="msg.id" class="list-group-item d-flex justify-content-between align-items-center">
          <div>
            <strong>{{ msg.from }}</strong> - {{ msg.subject }}
          </div>
          <span class="text-muted small">{{ msg.date }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>
