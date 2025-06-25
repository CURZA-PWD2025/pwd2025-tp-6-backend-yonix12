import { defineStore } from 'pinia';
import ApiService from '@/services/ApiService';
import type { Proveedor } from '@/interfaces/Proveedor';

interface ProveedorState {
  proveedores: Proveedor[];
  cargando: boolean;
}

export const useProveedorStore = defineStore('proveedor', {
  state: (): ProveedorState => ({
    proveedores: [],
    cargando: false
  }),
  getters: {
    listaProveedores: (state) => state.proveedores
  },
  actions: {
    async obtenerProveedores() {
      this.cargando = true;
      try {
        const data = await ApiService.getAll<Proveedor>('proveedores');
        this.proveedores = data;
      } catch (error) {
        console.error('Error al obtener los proveedores:', error);
      } finally {
        this.cargando = false;
      }
    },
    async crearProveedor(nuevoProveedor: Omit<Proveedor, 'id'>) {
      try {
        const proveedorCreado = await ApiService.create<Proveedor>('proveedores', nuevoProveedor);
        this.proveedores.push(proveedorCreado);
      } catch (error) {
        console.error('Error al crear el proveedor:', error);
        throw error;
      }
    },
    async actualizarProveedor(proveedorActualizado: Proveedor) {
      try {
        await ApiService.update<Proveedor>('proveedores', proveedorActualizado.id, proveedorActualizado);
        const index = this.proveedores.findIndex(p => p.id === proveedorActualizado.id);
        if (index !== -1) {
          this.proveedores[index] = proveedorActualizado;
        }
      } catch (error) {
        console.error('Error al actualizar el proveedor:', error);
        throw error;
      }
    },
    async eliminarProveedor(id: number) {
      try {
        await ApiService.destroy('proveedores', id);
        this.proveedores = this.proveedores.filter(p => p.id !== id);
      } catch (error) {
        console.error('Error al eliminar el proveedor:', error);
        throw error;
      }
    }
  }
});