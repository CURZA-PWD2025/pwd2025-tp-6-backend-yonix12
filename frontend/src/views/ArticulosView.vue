<script setup lang="ts">
import { ref } from 'vue';
import ArticuloList from '@/components/articulos/ArticuloList.vue';
import ArticuloForm from '@/components/articulos/ArticuloForm.vue';
import { useArticuloStore, type ArticuloPayload } from '@/stores/articuloStore';
import type { Articulo } from '@/interfaces/Articulo';

const articuloStore = useArticuloStore();
const mostrandoFormulario = ref(false);
const articuloSeleccionado = ref<Articulo | null>(null);

const mostrarFormularioParaCrear = () => {
  articuloSeleccionado.value = null;
  mostrandoFormulario.value = true;
};

const manejarEditar = (articulo: Articulo) => {
  articuloSeleccionado.value = articulo;
  mostrandoFormulario.value = true;
};

const manejarCancelar = () => {
  mostrandoFormulario.value = false;
};

const manejarGuardar = async (articulo: ArticuloPayload) => {
  try {
    if (articulo.id) {
      await articuloStore.actualizarArticulo(articulo.id, articulo);
      alert('Artículo actualizado con éxito.');
    } else {
      await articuloStore.crearArticulo(articulo);
      alert('Artículo creado con éxito.');
    }
    mostrandoFormulario.value = false;
  } catch (error) {
    alert('Error al guardar el artículo.');
  }
};
</script>

<template>
  <div class="articulos-view">
    <h1>Gestión de Artículos</h1>

    <div v-if="mostrandoFormulario">
      <ArticuloForm 
        :articulo-para-editar="articuloSeleccionado"
        @articulo-guardado="manejarGuardar"
        @cancelar="manejarCancelar"
      />
    </div>

    <div v-else>
      <button @click="mostrarFormularioParaCrear">Crear Nuevo Artículo</button>
      <ArticuloList @editar-articulo="manejarEditar" />
    </div>
  </div>
</template>

<style scoped>
.articulos-view { padding: 20px; }
button { margin-bottom: 15px; 
padding: 20px;}
</style>