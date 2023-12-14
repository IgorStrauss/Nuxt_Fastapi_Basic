
import { useAuthStore } from '~/store/auth';
export default function (to, from) {
  const authStore = useAuthStore();

  
  if (!authStore.token) {
    return navigateTo('/login')
    }
}

