import type { Marca } from './Marca';
import type { Categoria } from './Categoria';
import type { Proveedor } from './Proveedor';

export interface Articulo {
  id: number;
  descripcion: string;
  precio: number;
  stock: number;
  marca: Marca;
  proveedor: Proveedor;
  categorias: Categoria[];
}