<template>
    <button @click="handleLogout" class="logout-button">
      Logout
    </button>
  </template>
  
  <script>
  import { useAuthStore } from '~/store/auth';
  import { useRouter } from 'vue-router';
  
  export default {
    setup() {
      const authStore = useAuthStore();
      const router = useRouter();
  
      const handleLogout = () => {
        authStore.clearAuthData();
        // Redirecione para a página de login após limpar os dados de autenticação
        router.push('/login');
      };
  
      return {
        handleLogout,
      };
    },
  };
  </script>
  
  <style scoped>
  .logout-button {
    background-color: #ff6347;
    color: #ffffff;
    padding: 8px 16px;
    margin-left: 5px;
    margin-top: 5px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
  }
  
  .logout-button:hover {
    background-color: #dc143c;
  }
  </style>
  