from ._model import MarcaModel,CategoriaModel,ProveedorModel,ArticuloModel

#marcas:
class MarcaController:
    """
    Controlador para la entidad Marca.
    """
    @staticmethod
    def get_all():
        """Obtiene todas las marcas y las serializa."""
        marcas_objetos = MarcaModel.get_all()
        return [marca.serializar() for marca in marcas_objetos]

    @staticmethod
    def get_one(id_marca):
        """Obtiene una marca por ID y la serializa, o devuelve error."""
        marca_obj = MarcaModel.get_one(id_marca)
        if marca_obj:
            return marca_obj.serializar()
        return {'error': 'Marca no encontrada'}, 404

    @staticmethod
    def create(data):
        """Crea una nueva marca a partir de los datos recibidos."""
        if 'descripcion' not in data or not data['descripcion']:
            return {'error': 'La descripción es requerida'}, 400

        nueva_marca = MarcaModel(descripcion=data['descripcion'])
        nueva_marca.create()
        
        return nueva_marca.serializar(), 201
    @staticmethod
    def update(id_marca, data):
        """
        Actualiza una marca existente.
        """
        marca_obj = MarcaModel.get_one(id_marca)
        
        if not marca_obj:
            return {'error': 'Marca no encontrada'}, 404
        
        if 'descripcion' not in data:
            return {'error': 'La descripción es requerida'}, 400
            
        marca_obj.descripcion = data['descripcion']
        
        marca_obj.update()
        
        return marca_obj.serializar(), 200 
    @staticmethod
    def delete(id_marca):
        """
        Elimina una marca por su ID.
        """
        rows_affected = MarcaModel.delete(id_marca)
        
        if rows_affected > 0:
            return {'message': 'Marca eliminada correctamente'}, 200 
        
        return {'error': 'Marca no encontrada'}, 404
    
    #categoria:
class categoriaController:
    @staticmethod
    def get_all():
        categoria_objetos = CategoriaModel.get_all()
        return [categoria.serializar() for categoria in categoria_objetos]

    @staticmethod
    def get_one(id_categoria):
        categoria_obj = CategoriaModel.get_one(id_categoria)
        if categoria_obj:
            return categoria_obj.serializar()
        return {'error': 'Categoria no encontrada'}, 404

    @staticmethod
    def create(data):
        if 'descripcion' not in data or not data['descripcion']:
            return {'error': 'La descripción es requerida'}, 400

        nueva_categoria = CategoriaModel(descripcion=data['descripcion'])
        nueva_categoria.create()
        
        return nueva_categoria.serializar(), 201
    @staticmethod
    def update(id_categoria, data):
        categoria_obj = CategoriaModel.get_one(id_categoria)
        
        if not categoria_obj:
            return {'error': 'Categoria no encontrada'}, 404
        
        if 'descripcion' not in data:
            return {'error': 'La descripción es requerida'}, 400
            
        categoria_obj.descripcion = data['descripcion']
        
        categoria_obj.update()
        
        return categoria_obj.serializar(), 200 
    @staticmethod
    def delete(id_categoria):

        rows_affected = CategoriaModel.delete(id_categoria)
        
        if rows_affected > 0:
            return {'message': 'Categoria eliminada correctamente'}, 200 
        
        return {'error': 'Categoria no encontrada'}, 404
    
    
#proveedores
class ProveedorController:
    @staticmethod
    def get_all():
        """Obtiene todos los proveedores."""
        proveedor_objetos = ProveedorModel.get_all()
        return [proveedor.serializar() for proveedor in proveedor_objetos]

    @staticmethod
    def get_one(id_proveedor):
        """Obtiene un proveedor por su ID."""
        proveedor_obj = ProveedorModel.get_one(id_proveedor)
        if proveedor_obj:
            return proveedor_obj.serializar()
        return {'error': 'Proveedor no encontrado'}, 404

    @staticmethod
    def create(data):
        """Crea un nuevo proveedor."""

        if 'nombre' not in data or 'email' not in data:
            return {'error': 'Los campos nombre y email son requeridos'}, 400

        nuevo_proveedor = ProveedorModel.deserializar(data)
        nuevo_proveedor.create()
        
        return nuevo_proveedor.serializar(), 201

    @staticmethod
    def update(id_proveedor, data):
        """Actualiza un proveedor existente."""
        proveedor_obj = ProveedorModel.get_one(id_proveedor)
        
        if not proveedor_obj:
            return {'error': 'Proveedor no encontrado'}, 404
        

        proveedor_obj.nombre = data.get('nombre', proveedor_obj.nombre)
        proveedor_obj.telefono = data.get('telefono', proveedor_obj.telefono)
        proveedor_obj.direccion = data.get('direccion', proveedor_obj.direccion)
        proveedor_obj.email = data.get('email', proveedor_obj.email)
        
        proveedor_obj.update()
        
        return proveedor_obj.serializar(), 200 

    @staticmethod
    def delete(id_proveedor):
        """Elimina un proveedor."""
        rows_affected = ProveedorModel.delete(id_proveedor)
        
        if rows_affected > 0:
            return {'message': 'Proveedor eliminado correctamente'}, 200 
        
        return {'error': 'Proveedor no encontrado'}, 404

#articulos
class ArticuloController:
    @staticmethod
    def get_all():
        """Obtiene todos los artículos y los serializa."""
        articulos_objetos = ArticuloModel.get_all()
        return [articulo.serializar() for articulo in articulos_objetos]
    
    @staticmethod
    def get_one(id_articulo):
        """Obtiene un artículo por su ID y lo serializa."""
        articulo_obj = ArticuloModel.get_one(id_articulo)
        if articulo_obj:
            return articulo_obj.serializar()
        return {'error': 'Artículo no encontrado'}, 404
    
    @staticmethod
    def create(data):
        required_fields = ['descripcion', 'precio', 'stock', 'marca_id', 'proveedor_id', 'categorias_ids']
        for field in required_fields:
            if field not in data:
                return {'error': f'El campo {field} es requerido'}, 400

        nuevo_articulo = ArticuloModel(
            descripcion=data['descripcion'],
            precio=data['precio'],
            stock=data['stock'],
            marca_id=data['marca_id'],
            proveedor_id=data['proveedor_id'],
            categorias_ids=data['categorias_ids']
        )
        
        nuevo_articulo.create()


        articulo_completo = ArticuloModel.get_one(nuevo_articulo.id_articulo)
        if articulo_completo:
            return articulo_completo.serializar(), 201
        
        return {'error': 'No se pudo crear el artículo'}, 500

    @staticmethod
    def update(id_articulo, data):
        """Actualiza un artículo existente."""
        articulo_obj = ArticuloModel.get_one(id_articulo)
        if not articulo_obj:
            return {'error': 'Artículo no encontrado'}, 404
        

        articulo_actualizado = ArticuloModel(
            id_articulo=id_articulo,
            descripcion=data.get('descripcion', articulo_obj.descripcion),
            precio=data.get('precio', articulo_obj.precio),
            stock=data.get('stock', articulo_obj.stock),
            marca_id=data.get('marca_id', articulo_obj.marca.id_marca),
            proveedor_id=data.get('proveedor_id', articulo_obj.proveedor.id_proveedor),
            categorias_ids=data.get('categorias_ids', [cat.id_categoria for cat in articulo_obj.categorias])
        )

        articulo_actualizado.update()
        
        articulo_completo = ArticuloModel.get_one(id_articulo)
        return articulo_completo.serializar(), 200

    @staticmethod
    def delete(id_articulo):
        """Elimina un artículo."""
        rows_affected = ArticuloModel.delete(id_articulo)
        if rows_affected > 0:
            return {'message': 'Artículo eliminado correctamente'}, 200
        return {'error': 'Artículo no encontrado'}, 404
