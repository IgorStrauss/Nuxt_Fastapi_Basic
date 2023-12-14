// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  alias: {
    css: "/<rootDir>/assets/css",
  },
  css: ["@/assets/css/main.css",
  'bootstrap/dist/css/bootstrap.css',
  ],
  modules: [
    "nuxt-bootstrap-icons",
    "@nuxtjs/tailwindcss",
    "@invictus.codes/nuxt-vuetify",
    "@pinia/nuxt",
    "@pinia-plugin-persistedstate/nuxt",
  ],
  pinia: {
    storeDirs: ["./store/**"],
  },
  runtimeConfig: {
    public: {
      SECRET_KEY: process.env.SECRET_KEY
    }
  },
  optimizeDeps: {
    include: ["nuxt-cookie"]
  },
})
