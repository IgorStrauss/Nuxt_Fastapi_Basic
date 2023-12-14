<template>
  <div class="container-md mt-3">
    <div v-if="user">
      <div class="card">
        <div class="card-header">Detalhes de @{{ user.name }}</div>
        <div class="card-body">
          <blockquote class="blockquote mb-0">
            <p>ID: {{ user.id }}.</p>
            <p>Nome: {{ user.name }}.</p>
            <p>E-mail: {{ user.email }}.</p>
          </blockquote>
        </div>
      </div>
    </div>
    <div v-else-if="loading">
      <h1 class="banner-loading">Loading...</h1>
    </div>
    <div v-else-if="errorType === 'notFound'">
      <h1 class="banner-error">Usuário não encontrado</h1>
      <NuxtLink to="/" class="flex flex-col items-center justify-center text-blue-500 hover:underline hover:dark:text-blue-800 mt-2">Voltar</NuxtLink>
    </div>
    <div v-else-if="errorType === 'unauthorized'">
      <h1 class="banner-error">Você não está autorizado</h1>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: "auth"
});
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "~/store/auth";

const authStore = useAuthStore();

const user = ref(null);
const loading = ref(true);
const errorType = ref(null);
const route = useRoute();
const router = useRouter();

onMounted(async () => {
  const user_id = route.params.id;

  try {
    const response = await fetch(`http://localhost:8000/api/users/${user_id}`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${authStore.token}`,
      },
    });

    if (response.status === 404) {
      errorType.value = 'notFound';
      loading.value = false;
    } else if (response.status === 401) {
      errorType.value = 'unauthorized';
      loading.value = false;
      router.push('/login');
    } else if (!response.ok) {
      throw new Error(`Failed to get user data for user ID ${user_id}`);
    } else {
      const data = await response.json();
      user.value = data;
      loading.value = false;
    }
  } catch (error) {
    console.error("Erro ao obter dados do usuário:", error);
    loading.value = false;
  }
});
</script>

<style scoped>
.banner-loading {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  margin-top: 20rem;
}

.banner-error {
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  color: red;
  margin-top: 20rem;
}
</style>
