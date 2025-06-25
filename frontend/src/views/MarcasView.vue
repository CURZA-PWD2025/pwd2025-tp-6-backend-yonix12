<script setup lang="ts">
import { ref } from 'vue';
import MarcaList from '@/components/marcas/MarcaList.vue';
import MarcaForm from '@/components/marcas/MarcaForm.vue';
import { useMarcaStore } from '@/stores/marcaStore';
import type { Marca } from '@/interfaces/Marca';

const marcaStore = useMarcaStore();
const mostrandoFormulario = ref(false); 
const marcaSeleccionada = ref<Marca | null>(null); 

const mostrarFormularioParaCrear = () => {
  marcaSeleccionada.value = null; 
  mostrandoFormulario.value = true;
};

const manejarEditar = (marca: Marca) => {
  marcaSeleccionada.value = marca; 
  mostrandoFormulario.value = true;
};

const manejarCancelar = () => {
  mostrandoFormulario.value = false;
};

const manejarGuardar = async (marca: Partial<Marca>) => {
  try {
    if (marca.id) {
      await marcaStore.actualizarMarca(marca as Marca);
      alert('Marca actualizada con éxito.');
    } else {
      await marcaStore.crearMarca({ descripcion: marca.descripcion || '' });
      alert('Marca creada con éxito.');
    }
    mostrandoFormulario.value = false;
  } catch (error) {
    alert('Error al guardar la marca.');
    console.error(error);
  }
};
</script>

<template>
  <div class="marcas-view">
    <h1>Gestión de Marcas</h1>

    <div v-if="mostrandoFormulario">
      <MarcaForm 
        :marca-para-editar="marcaSeleccionada"
        @marca-guardada="manejarGuardar"
        @cancelar="manejarCancelar"
      />
    </div>

    <div v-else>
      <button @click="mostrarFormularioParaCrear" class="crear">Crear Nueva Marca</button>
      <MarcaList @editar-marca="manejarEditar" />
    </div>
  </div>
</template>

<style scoped>
.marcas-view {
  padding: 20px;
}

button {
  margin-bottom: 15px;
  padding: 20px;
}

</style>