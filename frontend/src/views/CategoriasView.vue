<script setup lang="ts">
import { ref } from 'vue';
import CategoriaList from '@/components/categorias/CategoriaList.vue';
import CategoriaForm from '@/components/categorias/CategoriaForm.vue';
import { useCategoriaStore } from '@/stores/categoriaStore';
import type { Categoria } from '@/interfaces/Categoria';

const categoriaStore = useCategoriaStore();
const mostrandoFormulario = ref(false);
const categoriaSeleccionada = ref<Categoria | null>(null);

const mostrarFormularioParaCrear = () => {
  categoriaSeleccionada.value = null;
  mostrandoFormulario.value = true;
};

const manejarEditar = (categoria: Categoria) => {
  categoriaSeleccionada.value = categoria;
  mostrandoFormulario.value = true;
};

const manejarCancelar = () => {
  mostrandoFormulario.value = false;
};

const manejarGuardar = async (categoria: Partial<Categoria>) => {
  try {
    if (categoria.id) {
      await categoriaStore.actualizarCategoria(categoria as Categoria);
      alert('Categoría actualizada con éxito.');
    } else {
      await categoriaStore.crearCategoria({ descripcion: categoria.descripcion || '' });
      alert('Categoría creada con éxito.');
    }
    mostrandoFormulario.value = false;
  } catch (error) {
    alert('Error al guardar la categoría.');
    console.error(error);
  }
};
</script>

<template>
  <div class="categorias-view">
    <h1>Gestión de Categorías</h1>

    <div v-if="mostrandoFormulario">
      <CategoriaForm 
        :categoria-para-editar="categoriaSeleccionada"
        @categoria-guardada="manejarGuardar"
        @cancelar="manejarCancelar"
      />
    </div>

    <div v-else>
      <button @click="mostrarFormularioParaCrear" class="crear">Crear Nueva Categoría</button>
      <CategoriaList @editar-categoria="manejarEditar" />
    </div>
  </div>
</template>

<style scoped>
.categorias-view {
  padding: 20px;
}
button {
  margin-bottom: 15px;
  padding: 20px;
}

</style>