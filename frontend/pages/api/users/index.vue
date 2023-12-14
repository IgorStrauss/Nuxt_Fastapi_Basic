<template>
  <Logout />
  <div class="container mt-5">
    <div>
      <h1 id="banner-index">Lista de usuários</h1>
      <h3>Usuário: {{ authStore.user }}</h3>
      <p>Status code: {{ apiResponse ? apiResponse.status : 'Carregando...' }}</p>

      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Nome</th>
            <th scope="col">E-mail</th>
            <th scope="col">Ações</th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr v-for="user in userData" :key="user.id">
            <th scope="row">{{ user.id }}</th>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>
              <NuxtLink :to="`/api/users/${user.id}`" target="_blank">
                Ver detalhes
              </NuxtLink>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: "auth",
});
import { ref, onMounted } from 'vue';
import { useAuthStore } from '~/store/auth';
import { useRouter } from 'vue-router';

const router = useRouter();
const authStore = useAuthStore();
const userData = ref([]);
const apiResponse = ref(null);

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/api/users', {
      headers: {
        Authorization: `Bearer ${authStore.token}`,
      },
    });
    console.log('Status code:', response.status);
    if (response.status === 401) {
      router.push('/login');
    }

    if (!response.ok) {
      throw new Error('Falha ao obter dados dos usuários');
    }

    userData.value = await response.json();
    apiResponse.value = { status: response.status };
    
  } catch (error) {
    console.error('Erro ao obter dados dos usuários:', error);
  }
  
});
</script>
