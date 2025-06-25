<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Inicio</RouterLink>
        <RouterLink to="/marcas">Marcas</RouterLink>
        <RouterLink to="/categorias">Categorías</RouterLink>
        <RouterLink to="/proveedores">Proveedores</RouterLink>
        <RouterLink to="/articulos">Artículos</RouterLink> 
      </nav>
    </div>
  </header>


  <RouterView v-slot="{ Component }">
    <Transition name="fade" mode="out-in">
      <component :is="Component" />
    </Transition>
  </RouterView>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  border-bottom: 1px solid #ddd;
}

nav {
  width: 100%;
  font-size: 1rem;
  text-align: center;
  margin-top: 1rem;
  margin-bottom: 1rem;
  padding: 14px;
  font-size: 24px;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
  color: var(--color-text);
  text-decoration: none;

}

nav a:first-of-type {
  border: 0;
}

nav a.router-link-exact-active {
  color: rgb(148, 218, 131); 
}

.wrapper{
  background:linear-gradient(#2980B9,transparent)
}
</style>