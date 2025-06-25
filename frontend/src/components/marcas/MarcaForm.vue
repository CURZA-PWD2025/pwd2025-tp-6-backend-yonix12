<script setup lang="ts">
import { ref, watch } from 'vue';
import type { Marca } from '@/interfaces/Marca';


const props = defineProps<{
  marcaParaEditar?: Marca | null;
}>();

const emit = defineEmits(['marca-guardada', 'cancelar']);


const marcaEditable = ref<Partial<Marca>>({
  id: undefined,
  descripcion: ''
});

watch(() => props.marcaParaEditar, (nuevaMarca) => {
  marcaEditable.value = { ...nuevaMarca };
}, { immediate: true }); 

const guardarMarca = () => {
  if (!marcaEditable.value.descripcion) {
    alert('La descripción no puede estar vacía.');
    return;
  }
  emit('marca-guardada', marcaEditable.value);
};
</script>

<template>
  <div class="marca-form">
    <form @submit.prevent="guardarMarca">
      <h3>{{ marcaParaEditar ? 'Editar Marca' : 'Crear Nueva Marca' }}</h3>
      
      <div>
        <label for="descripcion">Descripción:</label>
        <input type="text" id="descripcion" v-model="marcaEditable.descripcion" required />
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