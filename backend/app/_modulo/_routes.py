from flask import Blueprint, jsonify, request

from ._controller import MarcaController, categoriaController, ProveedorController,ArticuloController

modulo_bp = Blueprint('modulo_bp', __name__, url_prefix='/api')

#Marcas:
@modulo_bp.route('/marcas', methods=['GET'])
def get_all_marcas():
    """Endpoint para obtener todas las marcas."""
    marcas = MarcaController.get_all()
    return jsonify(marcas)

@modulo_bp.route('/marcas/<int:id>', methods=['GET'])
def get_one_marca(id):
    """Endpoint para obtener una marca por su ID."""
    resultado = MarcaController.get_one(id)
    if isinstance(resultado, tuple):
        error, status_code = resultado
        return jsonify(error), status_code
    return jsonify(resultado)

@modulo_bp.route('/marcas', methods=['POST'])
def create_marca():
    """Endpoint para crear una nueva marca."""
    data = request.get_json()
    resultado, status_code = MarcaController.create(data)
    return jsonify(resultado), status_code

@modulo_bp.route('/marcas/<int:id>', methods=['PUT'])
def update_marca(id):
    """
    Endpoint para actualizar una marca existente.
    """
    data = request.get_json()
    resultado, status_code = MarcaController.update(id, data)
    return jsonify(resultado), status_code


@modulo_bp.route('/marcas/<int:id>', methods=['DELETE'])
def delete_marca(id):

    resultado, status_code = MarcaController.delete(id)
    return jsonify(resultado), status_code


# --- RUTAS PARA CATEGORIAS ---

@modulo_bp.route('/categorias', methods=['GET'])
def get_all_categorias(): 
    categorias = categoriaController.get_all()
    return jsonify(categorias)

@modulo_bp.route('/categorias/<int:id>', methods=['GET'])
def get_one_categoria(id):
    resultado = categoriaController.get_one(id)
    if isinstance(resultado, tuple):
        error, status_code = resultado
        return jsonify(error), status_code
    return jsonify(resultado)

@modulo_bp.route('/categorias', methods=['POST'])
def create_categoria():
    data = request.get_json()
    resultado, status_code = categoriaController.create(data)
    return jsonify(resultado), status_code

@modulo_bp.route('/categorias/<int:id>', methods=['PUT'])
def update_categoria(id):
    data = request.get_json()
    resultado, status_code = categoriaController.update(id, data)
    return jsonify(resultado), status_code

@modulo_bp.route('/categorias/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    resultado, status_code = categoriaController.delete(id)
    return jsonify(resultado), status_code


# --- RUTAS PARA PROVEEDORES ---

@modulo_bp.route('/proveedores', methods=['GET'])
def get_all_proveedores():
    proveedores = ProveedorController.get_all()
    return jsonify(proveedores)

@modulo_bp.route('/proveedores/<int:id>', methods=['GET'])
def get_one_proveedor(id):
    resultado = ProveedorController.get_one(id)
    if isinstance(resultado, tuple):
        error, status_code = resultado
        return jsonify(error), status_code
    return jsonify(resultado)

@modulo_bp.route('/proveedores', methods=['POST'])
def create_proveedor():
    data = request.get_json()
    resultado, status_code = ProveedorController.create(data)
    return jsonify(resultado), status_code

@modulo_bp.route('/proveedores/<int:id>', methods=['PUT'])
def update_proveedor(id):
    data = request.get_json()
    resultado, status_code = ProveedorController.update(id, data)
    return jsonify(resultado), status_code

@modulo_bp.route('/proveedores/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    resultado, status_code = ProveedorController.delete(id)
    return jsonify(resultado), status_code

#articulo
@modulo_bp.route('/articulos', methods=['GET'])
def get_all_articulos():
    """Endpoint para obtener todos los artículos."""
    articulos = ArticuloController.get_all()
    return jsonify(articulos)

@modulo_bp.route('/articulos/<int:id>', methods=['GET'])
def get_one_articulo(id):
        """Endpoint para obtener un artículo específico."""
        resultado = ArticuloController.get_one(id)
        if isinstance(resultado, tuple):
            error, status_code = resultado
            return jsonify(error), status_code
        return jsonify(resultado)
    
@modulo_bp.route('/articulos', methods=['POST'])
def create_articulo():
    data = request.get_json()
    resultado, status_code = ArticuloController.create(data)
    return jsonify(resultado), status_code

@modulo_bp.route('/articulos/<int:id>', methods=['PUT'])
def update_articulo(id):
        """Endpoint para actualizar un artículo."""
        data = request.get_json()
        resultado, status_code = ArticuloController.update(id, data)
        return jsonify(resultado), status_code

@modulo_bp.route('/articulos/<int:id>', methods=['DELETE'])
def delete_articulo(id):
        """Endpoint para eliminar un artículo."""
        resultado, status_code = ArticuloController.delete(id)
        return jsonify(resultado), status_code
