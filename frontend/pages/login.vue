<template>
  <div class="w-full h-screen flex flex-col items-center justify-center">
    <h2 class="text-2xl font-bold mb-4">Login</h2>

    <!-- Username Input -->
    <div class="mb-4">
      <label for="username" class="block text-gray-600 text-sm font-medium mb-2">Username:</label>
      <input
        v-model="username"
        type="text"
        id="username"
        name="username"
        class="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500"
        autocomplete="off"
      />
    </div>

    <!-- Password Input -->
    <div class="mb-6">
      <label for="password" class="block text-gray-600 text-sm font-medium mb-2">Password:</label>
      <input
        v-model="password"
        type="password"
        id="password"
        name="password"
        class="w-full px-3 py-2 border rounded focus:outline-none focus:border-blue-500"
      />
    </div>

    <!-- Submit Button -->
    <button @click="handleSubmit" class="w-38 bg-blue-500 text-white py-2 px-4 rounded focus:outline-none focus:bg-blue-600">
      Login
    </button>
    <NuxtLink to="/" class="flex flex-col items-center justify-center text-blue-500 hover:underline hover:dark:text-blue-800 mt-2">Acessar rota não protegida</NuxtLink>
    <NuxtLink to="/api/users" class="flex flex-col items-center justify-center text-blue-500 hover:underline hover:dark:text-blue-800 mt-2">Acessar rota protegida</NuxtLink>

  </div>
</template>

<script setup>
import { jwtDecode } from 'jwt-decode';
import { useAuthStore } from '~/store/auth';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();
const username = ref('');
const password = ref('');

const handleSubmit = async () => {
  try {
    const formData = new FormData();
    formData.append('username', username.value);
    formData.append('password', password.value);

    const response = await fetch('http://localhost:8000/token', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('Falha na autenticação');
    }

    const responseData = await response.json();

    const decodedToken = jwtDecode(responseData.access_token);

    authStore.setAuthData({
      user: decodedToken.sub,
      token: responseData.access_token,
    });

    console.log("Estado Atual da Loja de Autenticação - User:", authStore.user);
    console.log("Estado Atual da Loja de Autenticação - Token:", authStore.token);

    username.value = '';
    password.value = '';

    router.push('/api/users');
  } catch (error) {
    console.error('Erro ao fazer login:', error);
    username.value = '';
    password.value = '';
  }
};
</script>
