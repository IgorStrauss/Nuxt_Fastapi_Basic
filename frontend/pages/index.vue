<template>
  <div class="w-full h-screen flex flex-col items-center justify-center">
    <h1 class="text-3xl">Consumindo API</h1>
    <p>Status code: {{ apiResponse ? apiResponse.status : 'Carregando...' }}</p>
    <div v-if="apiResponse && apiResponse.data">
      <pre>{{ JSON.stringify(apiResponse.data, null, 2) }}</pre>
      <NuxtLink to="/login" class="flex flex-col items-center justify-center text-blue-500 hover:underline hover:dark:text-blue-800 mt-2">
      Login
    </NuxtLink>
    <NuxtLink to="/api/users" class="flex flex-col items-center justify-center text-blue-500 hover:underline hover:dark:text-blue-800 mt-2">
      Tabela de usuários
    </NuxtLink>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const apiResponse = ref(null);

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000');
    const data = await response.json();
    apiResponse.value = { status: response.status, data };
  } catch (error) {
    console.error('Erro ao carregar dados da API:', error);
    apiResponse.value = null;
  }
});
</script>
