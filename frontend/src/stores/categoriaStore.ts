import { defineStore } from 'pinia';
import ApiService from '@/services/ApiService';
import type { Categoria } from '@/interfaces/Categoria';

interface CategoriaState {
  categorias: Categoria[];
  cargando: boolean;
}

export const useCategoriaStore = defineStore('categoria', {
  state: (): CategoriaState => ({
    categorias: [],
    cargando: false
  }),

  getters: {
    listaCategorias: (state) => state.categorias,
    estaCargando: (state) => state.cargando
  },

  actions: {
    async obtenerCategorias() {
      this.cargando = true;
      try {
        const data = await ApiService.getAll<Categoria>('categorias');
        this.categorias = data;
      } catch (error) {
        console.error('Error al obtener las categorías:', error);
      } finally {
        this.cargando = false;
      }
    },

    async crearCategoria(nuevaCategoria: Omit<Categoria, 'id'>) {
      try {
        const categoriaCreada = await ApiService.create<Categoria>('categorias', nuevaCategoria);
        this.categorias.push(categoriaCreada);
      } catch (error) {
        console.error('Error al crear la categoría:', error);
        throw error;
      }
    },

    async actualizarCategoria(categoriaActualizada: Categoria) {
      try {
        await ApiService.update<Categoria>('categorias', categoriaActualizada.id, categoriaActualizada);
        const index = this.categorias.findIndex(c => c.id === categoriaActualizada.id);
        if (index !== -1) {
          this.categorias[index] = categoriaActualizada;
        }
      } catch (error) {
        console.error('Error al actualizar la categoría:', error);
        throw error;
      }
    },

    async eliminarCategoria(id: number) {
      try {
        await ApiService.destroy('categorias', id);
        this.categorias = this.categorias.filter(c => c.id !== id);
      } catch (error) {
        console.error('Error al eliminar la categoría:', error);
        throw error;
      }
    }
  }
});