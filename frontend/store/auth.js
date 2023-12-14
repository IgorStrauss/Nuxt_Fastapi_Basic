import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: null,
  }),
  actions: {
    setAuthData({ user, token }) {
      this.user = user;
      this.token = token;
    },
    clearAuthData() {
      this.user = null;
      this.token = null;
    },
  },
  persist: true,
});
