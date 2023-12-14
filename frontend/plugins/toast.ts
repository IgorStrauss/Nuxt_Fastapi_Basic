import Vue3Toastify, { ToastContainerOptions, toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(Vue3Toastify, {
    autoClose: 2000,
  } as ToastContainerOptions);

  toast.error = (message: string) => {
      toast(message,{
        type: 'error',
        position: 'bottom-right',
        icon: true,
        theme: 'dark',
      })
  },
  toast.success = (message: string) => {
    toast(message,{
      
      type: 'success',
      position: 'top-right',
      icon: true,
      theme: 'light',
    })
  }

  // Note: No 'return' here

  nuxtApp.provide('toast', toast);
});
