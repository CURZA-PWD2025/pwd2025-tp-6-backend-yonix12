<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import type { Articulo } from '@/interfaces/Articulo';
import type { ArticuloPayload } from '@/stores/articuloStore';
import { useMarcaStore } from '@/stores/marcaStore';
import { useCategoriaStore } from '@/stores/categoriaStore';
import { useProveedorStore } from '@/stores/proveedorStore';

const props = defineProps<{
  articuloParaEditar?: Articulo | null;
}>();
const emit = defineEmits(['articulo-guardado', 'cancelar']);

const marcaStore = useMarcaStore();
const categoriaStore = useCategoriaStore();
const proveedorStore = useProveedorStore();

const articuloEditable = ref<ArticuloPayload>({
  descripcion: '',
  precio: 0,
  stock: 0,
  marca_id: 0,
  proveedor_id: 0,
  categorias_ids: []
});

onMounted(() => {
  marcaStore.obtenerMarcas();
  categoriaStore.obtenerCategorias();
  proveedorStore.obtenerProveedores();
});

watch(() => props.articuloParaEditar, (nuevoArticulo) => {
  if (nuevoArticulo) {
    articuloEditable.value = {
      id: nuevoArticulo.id,
      descripcion: nuevoArticulo.descripcion,
      precio: nuevoArticulo.precio,
      stock: nuevoArticulo.stock,
      marca_id: nuevoArticulo.marca.id,
      proveedor_id: nuevoArticulo.proveedor.id,
      categorias_ids: nuevoArticulo.categorias.map(cat => cat.id)
    };
  } else {
    articuloEditable.value = {
      descripcion: '', precio: 0, stock: 0, marca_id: 0, proveedor_id: 0, categorias_ids: []
    };
  }
}, { immediate: true });

const guardarArticulo = () => {
  if (!articuloEditable.value.descripcion || !articuloEditable.value.marca_id || !articuloEditable.value.proveedor_id) {
    alert('Descripción, Marca y Proveedor son campos requeridos.');
    return;
  }
  emit('articulo-guardado', articuloEditable.value);
};
</script>

<template>
  <div class="articulo-form">
    <form @submit.prevent="guardarArticulo">
      <h3>{{ articuloParaEditar ? 'Editar Artículo' : 'Crear Nuevo Artículo' }}</h3>
      
      <div>
        <label for="descripcion">Descripción:</label>
        <input type="text" id="descripcion" v-model="articuloEditable.descripcion" required />
      </div>
      <div>
        <label for="precio">Precio:</label>
        <input type="number" step="0.01" id="precio" v-model="articuloEditable.precio" required />
      </div>
      <div>
        <label for="stock">Stock:</label>
        <input type="number" id="stock" v-model="articuloEditable.stock" required />
      </div>

      <div>
        <label for="marca">Marca:</label>
        <select id="marca" v-model="articuloEditable.marca_id" required>
          <option disabled :value="0">Seleccione una marca</option>
          <option v-for="marca in marcaStore.listaMarcas" :key="marca.id" :value="marca.id">
            {{ marca.descripcion }}
          </option>
        </select>
      </div>

      <div>
        <label for="proveedor">Proveedor:</label>
        <select id="proveedor" v-model="articuloEditable.proveedor_id" required>
          <option disabled :value="0">Seleccione un proveedor</option>
          <option v-for="proveedor in proveedorStore.listaProveedores" :key="proveedor.id" :value="proveedor.id">
            {{ proveedor.nombre }}
          </option>
        </select>
      </div>

      <div>
        <label for="categorias">Categorías:</label>
        <select id="categorias" v-model="articuloEditable.categorias_ids" multiple>
          <option v-for="cat in categoriaStore.listaCategorias" :key="cat.id" :value="cat.id">
            {{ cat.descripcion }}
          </option>
        </select>
      </div>

      <div class="acciones-form">
        <button type="submit">Guardar</button>
        <button type="button" @click="$emit('cancelar')">Cancelar</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.articulo-form { border: 1px solid #ccc; padding: 20px; margin-top: 20px; border-radius: 8px; }
.acciones-form { margin-top: 15px; }
div { margin-bottom: 10px; }
input, select { width: 100%; padding: 8px; margin-top: 5px; }
select[multiple] { height: 120px; }
</style>