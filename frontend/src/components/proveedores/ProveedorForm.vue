<script setup lang="ts">
import { ref, watch } from 'vue';
import type { Proveedor } from '@/interfaces/Proveedor';

const props = defineProps<{
  proveedorParaEditar?: Proveedor | null;
}>();

const emit = defineEmits(['proveedor-guardado', 'cancelar']);

const proveedorEditable = ref<Partial<Proveedor>>({});

watch(() => props.proveedorParaEditar, (nuevoProveedor) => {
  proveedorEditable.value = { ...nuevoProveedor };
}, { immediate: true });

const guardarProveedor = () => {
  if (!proveedorEditable.value.nombre || !proveedorEditable.value.email) {
    alert('Nombre y Email son campos requeridos.');
    return;
  }
  emit('proveedor-guardado', proveedorEditable.value);
};
</script>

<template>
  <div class="proveedor-form">
    <form @submit.prevent="guardarProveedor">
      <h3>{{ proveedorParaEditar ? 'Editar Proveedor' : 'Crear Nuevo Proveedor' }}</h3>
      
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" v-model="proveedorEditable.nombre" required />
      </div>
      <div>
        <label for="telefono">Teléfono:</label>
        <input type="tel" id="telefono" v-model="proveedorEditable.telefono" />
      </div>
      <div>
        <label for="direccion">Dirección:</label>
        <input type="text" id="direccion" v-model="proveedorEditable.direccion" />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="proveedorEditable.email" required />
      </div>

      <div class="acciones-form">
        <button type="submit">Guardar</button>
        <button type="button" @click="$emit('cancelar')">Cancelar</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.proveedor-form { border: 1px solid #ccc; padding: 20px; margin-top: 20px; border-radius: 8px; }
.acciones-form { margin-top: 15px; }
div { margin-bottom: 10px; }
input { width: 100%; padding: 8px; margin-top: 5px; }
</style>