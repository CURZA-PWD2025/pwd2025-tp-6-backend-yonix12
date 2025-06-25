<script setup lang="ts">
import { onMounted } from 'vue';
import { useCategoriaStore } from '@/stores/categoriaStore';
import type { Categoria } from '@/interfaces/Categoria';

const emit = defineEmits(['editar-categoria']);

const categoriaStore = useCategoriaStore();

onMounted(() => {
  categoriaStore.obtenerCategorias();
});

const manejarEliminar = async (id: number) => {
  if (confirm('¿Estás seguro de que quieres eliminar esta categoría?')) {
    try {
      await categoriaStore.eliminarCategoria(id);
      alert('Categoría eliminada con éxito.');
    } catch (error) {
      alert('Hubo un error al eliminar la categoría.');
      console.error(error);
    }
  }
};

const editarCategoria = (categoria: Categoria) => {
  emit('editar-categoria', categoria);
};
</script>

<template>
  <div class="categoria-list">
    <h2>Listado de Categorías</h2>
    <div v-if="categoriaStore.estaCargando">Cargando...</div>
    
    <table v-else>
      <thead>
        <tr>
          <th>ID</th>
          <th>Descripción</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="categoria in categoriaStore.listaCategorias" :key="categoria.id">
          <td>{{ categoria.id }}</td>
          <td>{{ categoria.descripcion }}</td>
          <td class="botones">
            <button @click="editarCategoria(categoria)">Editar <svg fill="#a3ff99" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>pencil</title> <path d="M0 32l12-4 20-20-8-8-20 20zM4 28l2.016-5.984 4 4zM8 20l12-12 4 4-12 12z"></path> </g></svg></button>
            <button @click="manejarEliminar(categoria.id)">Eliminar <svg fill="#a3ff99" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 593.727 593.727" xml:space="preserve"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g> <g> <path d="M491.362,593.727H102.374c-20.865,0-37.84-16.975-37.84-37.84v-448.5h464.668v448.5 C529.202,576.752,512.228,593.727,491.362,593.727z M79.677,122.529v433.357c0,12.516,10.182,22.697,22.697,22.697h388.989 c12.516,0,22.697-10.182,22.697-22.697V122.529H79.677z"></path> </g> <g> <path d="M550.8,91.913H42.927V58.382c0-20.86,16.973-37.831,37.835-37.831h192.852C276.618,8.58,286.12,0,297.506,0 c11.399,0,20.907,8.578,23.905,20.551H512.97c20.859,0,37.83,16.971,37.83,37.831V91.913L550.8,91.913z M58.07,76.77h477.587 V58.382c0-12.51-10.178-22.688-22.688-22.688h-205.57l-0.148-7.42c-0.145-7.24-4.516-13.131-9.745-13.131 c-5.219,0-9.586,5.893-9.736,13.136l-0.154,7.415H80.762c-12.512,0-22.692,10.177-22.692,22.688V76.77z"></path> </g> <g> <path d="M144.621,546.275c-15.949,0-28.924-12.977-28.924-28.926V196.011c0-15.95,12.975-28.926,28.924-28.926 c15.95,0,28.926,12.976,28.926,28.926V517.35C173.547,533.299,160.571,546.275,144.621,546.275z M144.621,182.228 c-7.599,0-13.781,6.183-13.781,13.783V517.35c0,7.6,6.183,13.783,13.781,13.783c7.601,0,13.783-6.184,13.783-13.783V196.011 C158.404,188.411,152.222,182.228,144.621,182.228z"></path> </g> <g> <path d="M243.094,546.275c-15.95,0-28.925-12.977-28.925-28.926V196.011c0-15.95,12.976-28.926,28.925-28.926 c15.949,0,28.925,12.976,28.925,28.926V517.35C272.019,533.299,259.043,546.275,243.094,546.275z M243.094,182.228 c-7.6,0-13.782,6.183-13.782,13.783V517.35c0,7.6,6.183,13.783,13.782,13.783s13.782-6.184,13.782-13.783V196.011 C256.876,188.411,250.694,182.228,243.094,182.228z"></path> </g> <g> <path d="M341.565,546.275c-15.949,0-28.926-12.977-28.926-28.926V196.011c0-15.95,12.977-28.926,28.926-28.926 s28.926,12.976,28.926,28.926V517.35C370.491,533.299,357.515,546.275,341.565,546.275z M341.565,182.228 c-7.6,0-13.783,6.183-13.783,13.783V517.35c0,7.6,6.184,13.783,13.783,13.783s13.783-6.184,13.783-13.783V196.011 C355.347,188.411,349.165,182.228,341.565,182.228z"></path> </g> <g> <path d="M440.038,546.275c-15.955,0-28.934-12.977-28.934-28.926V196.011c0-15.95,12.979-28.926,28.934-28.926 c15.949,0,28.924,12.976,28.924,28.926V517.35C468.962,533.299,455.987,546.275,440.038,546.275z M440.038,182.228 c-7.605,0-13.791,6.183-13.791,13.783V517.35c0,7.6,6.186,13.783,13.791,13.783c7.6,0,13.781-6.184,13.781-13.783V196.011 C453.819,188.411,447.638,182.228,440.038,182.228z"></path> </g> </g> </g></svg></button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #f2f2f2;
}
td>button{
  margin: 10px;
  font-size: 14px;
}
.botones{
  width: 30%;
}
button { margin-right: 5px;
padding: 10px; }

</style>
