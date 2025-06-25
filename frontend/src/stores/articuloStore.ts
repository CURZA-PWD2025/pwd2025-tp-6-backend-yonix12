import { defineStore } from 'pinia';
import ApiService from '@/services/ApiService';
import type { Articulo } from '@/interfaces/Articulo';

export interface ArticuloPayload {
  id?: number;
  descripcion: string;
  precio: number;
  stock: number;
  marca_id: number;
  proveedor_id: number;
  categorias_ids: number[];
}

interface ArticuloState {
  articulos: Articulo[];
  cargando: boolean;
}

export const useArticuloStore = defineStore('articulo', {
  state: (): ArticuloState => ({
    articulos: [],
    cargando: false
  }),
  getters: {
    listaArticulos: (state) => state.articulos
  },
  actions: {
    async obtenerArticulos() {
      this.cargando = true;
      try {
        const data = await ApiService.getAll<Articulo>('articulos');
        this.articulos = data;
      } catch (error) {
        console.error('Error al obtener los artículos:', error);
      } finally {
        this.cargando = false;
      }
    },
    async crearArticulo(nuevoArticulo: ArticuloPayload) {
      try {
        const articuloCreado = await ApiService.create<Articulo>('articulos', nuevoArticulo as any);        
        this.articulos.push(articuloCreado);
      } catch (error) {
        console.error('Error al crear el artículo:', error);
        throw error;
      }
    },
    async actualizarArticulo(id: number, articuloActualizado: ArticuloPayload) {
      try {
        const articuloDevuelto = await ApiService.update<Articulo>('articulos', id, articuloActualizado as any);        
        const index = this.articulos.findIndex(a => a.id === id);
        if (index !== -1) {
          this.articulos[index] = articuloDevuelto;
        }
      } catch (error) {
        console.error('Error al actualizar el artículo:', error);
        throw error;
      }
    },
    async eliminarArticulo(id: number) {
      try {
        await ApiService.destroy('articulos', id);
        this.articulos = this.articulos.filter(a => a.id !== id);
      } catch (error) {
        console.error('Error al eliminar el artículo:', error);
        throw error;
      }
    }
  }
});