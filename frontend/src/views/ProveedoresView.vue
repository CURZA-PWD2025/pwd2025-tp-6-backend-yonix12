<script setup lang="ts">
import { ref } from 'vue';
import ProveedorList from '@/components/proveedores/ProveedorList.vue';
import ProveedorForm from '@/components/proveedores/ProveedorForm.vue';
import { useProveedorStore } from '@/stores/proveedorStore';
import type { Proveedor } from '@/interfaces/Proveedor';

const proveedorStore = useProveedorStore();
const mostrandoFormulario = ref(false);
const proveedorSeleccionado = ref<Proveedor | null>(null);

const mostrarFormularioParaCrear = () => {
  proveedorSeleccionado.value = null;
  mostrandoFormulario.value = true;
};

const manejarEditar = (proveedor: Proveedor) => {
  proveedorSeleccionado.value = proveedor;
  mostrandoFormulario.value = true;
};

const manejarCancelar = () => {
  mostrandoFormulario.value = false;
};

const manejarGuardar = async (proveedor: Partial<Proveedor>) => {
  try {
    if (proveedor.id) {
      await proveedorStore.actualizarProveedor(proveedor as Proveedor);
      alert('Proveedor actualizado con éxito.');
    } else {
      await proveedorStore.crearProveedor(proveedor as Omit<Proveedor, 'id'>);
      alert('Proveedor creado con éxito.');
    }
    mostrandoFormulario.value = false;
  } catch (error) {
    alert('Error al guardar el proveedor.');
  }
};
</script>

<template>
  <div class="proveedores-view">
    <h1>Gestión de Proveedores</h1>

    <div v-if="mostrandoFormulario">
      <ProveedorForm 
        :proveedor-para-editar="proveedorSeleccionado"
        @proveedor-guardado="manejarGuardar"
        @cancelar="manejarCancelar"
      />
    </div>

    <div v-else>
      <button @click="mostrarFormularioParaCrear">Crear Nuevo Proveedor</button>
      <ProveedorList @editar-proveedor="manejarEditar" />
    </div>
  </div>
</template>

<style scoped>
.proveedores-view { padding: 20px; }
button { margin-bottom: 15px; 
padding: 20px;
}
</style>