<script setup lang="ts">
import { ref, watch } from 'vue';
import type { Categoria } from '@/interfaces/Categoria';

const props = defineProps<{
  categoriaParaEditar?: Categoria | null;
}>();

const emit = defineEmits(['categoria-guardada', 'cancelar']);

const categoriaEditable = ref<Partial<Categoria>>({
  id: undefined,
  descripcion: ''
});

watch(() => props.categoriaParaEditar, (nuevaCategoria) => {
  categoriaEditable.value = { ...nuevaCategoria };
}, { immediate: true });

const guardarCategoria = () => {
  if (!categoriaEditable.value.descripcion) {
    alert('La descripción no puede estar vacía.');
    return;
  }
  emit('categoria-guardada', categoriaEditable.value);
};
</script>

<template>
  <div class="categoria-form">
    <form @submit.prevent="guardarCategoria">
      <h3>{{ categoriaParaEditar ? 'Editar Categoría' : 'Crear Nueva Categoría' }}</h3>
      
      <div>
        <label for="descripcion">Descripción:</label>
        <input type="text" id="descripcion" v-model="categoriaEditable.descripcion" required />
      </div>

      <div class="acciones-form">
        <button type="submit">Guardar</button>
        <button type="button" @click="$emit('cancelar')">Cancelar</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.marca-form {
  border: 1px solid #ccc;
  padding: 20px;
  margin-top: 20px;
  border-radius: 8px;
}
.acciones-form {
  margin-top: 15px;
}
input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
}
</style>