import { defineStore } from 'pinia';
import ApiService from '@/services/ApiService'; 
import type { Marca } from '@/interfaces/Marca'; 

interface MarcaState {
  marcas: Marca[];
  cargando: boolean;
}

export const useMarcaStore = defineStore('marca', {
  state: (): MarcaState => ({
    marcas: [],
    cargando: false
  }),

  getters: {
    listaMarcas: (state) => state.marcas,
    estaCargando: (state) => state.cargando
  },

  actions: {
    async obtenerMarcas() {
      this.cargando = true; 
      try {

        const data = await ApiService.getAll<Marca>('marcas');
        this.marcas = data;
      } catch (error) {
        console.error('Error al obtener las marcas:', error);
      } finally {
        this.cargando = false; 
      }
    },

    async crearMarca(nuevaMarca: Omit<Marca, 'id'>) {
      try {
        const marcaCreada = await ApiService.create<Marca>('marcas', nuevaMarca);
        this.marcas.push(marcaCreada);
      } catch (error) {
        console.error('Error al crear la marca:', error);
        throw error; 
      }
    },

    async actualizarMarca(marcaActualizada: Marca) {
      try {
        await ApiService.update<Marca>('marcas', marcaActualizada.id, marcaActualizada);
        const index = this.marcas.findIndex(m => m.id === marcaActualizada.id);
        if (index !== -1) {
          this.marcas[index] = marcaActualizada;
        }
      } catch (error) {
        console.error('Error al actualizar la marca:', error);
        throw error;
      }
    },

    async eliminarMarca(id: number) {
      try {
        await ApiService.destroy('marcas', id);
        this.marcas = this.marcas.filter(m => m.id !== id);
      } catch (error) {
        console.error('Error al eliminar la marca:', error);
        throw error;
      }
    }
  }
});