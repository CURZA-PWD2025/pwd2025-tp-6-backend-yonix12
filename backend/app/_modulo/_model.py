from database import get_db

#marcas:
class MarcaModel:
    """
    Modelo para la entidad Marca.
    """
    def __init__(self, id_marca=None, descripcion=None):
        self.id_marca = id_marca
        self.descripcion = descripcion

    def serializar(self):
        """Convierte el objeto a un diccionario para la respuesta JSON."""
        return {
            'id': self.id_marca,
            'descripcion': self.descripcion
        }

    def serializar(self):
        """Convierte el objeto a un diccionario para la respuesta JSON."""
        return {
            'id': self.id_marca,
            'descripcion': self.descripcion
        }

    @staticmethod
    def deserializar(data):
        """Convierte un diccionario a un objeto MarcaModel."""
        return MarcaModel(data.get('id'), data.get('descripcion'))

    def create(self):
        """Inserta la instancia actual de MarcaModel en la base de datos."""
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO MARCAS (nombre) VALUES (?)",
            (self.descripcion,)
        )
        self.id_marca = cursor.lastrowid
        db.commit()
        db.close()

    @staticmethod
    def get_all():
        """Obtiene todas las marcas de la base de datos."""
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, nombre FROM MARCAS")
        filas = cursor.fetchall()
        marcas = [MarcaModel(fila['id'], fila['nombre']) for fila in filas]
        db.close()
        return marcas

    @staticmethod
    def get_one(id_marca):
        """Obtiene una única marca por su ID."""
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, nombre FROM MARCAS WHERE id = ?", (id_marca,))
        fila = cursor.fetchone()
        db.close()
        if fila:
            return MarcaModel(fila['id'], fila['nombre'])
        return None
    def update(self):
        """
        Actualiza la marca actual en la base de datos.
        """
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE MARCAS SET nombre = ? WHERE id = ?",
            (self.descripcion, self.id_marca)
        )
        db.commit()
        db.close()
    @staticmethod
    def delete(id_marca):
        """
        Elimina una marca de la base de datos por su ID.
        """
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM MARCAS WHERE id = ?", (id_marca,))
        db.commit()
        db.close()

        return cursor.rowcount
    
#categoria:
class CategoriaModel:
    def __init__(self, id_categoria=None, descripcion=None):
        self.id_categoria = id_categoria
        self.descripcion = descripcion

    def serializar(self):
        return {
            'id': self.id_categoria,
            'descripcion': self.descripcion
        }

    @staticmethod
    def deserializar(data):
        return CategoriaModel(data.get('id'), data.get('descripcion'))

    def create(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO CATEGORIAS (nombre) VALUES (?)", 
            (self.descripcion,)
        )
        self.id_categoria = cursor.lastrowid
        db.commit()
        db.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, nombre FROM CATEGORIAS")
        filas = cursor.fetchall()
        categorias = [CategoriaModel(fila['id'], fila['nombre']) for fila in filas]
        db.close()
        return categorias

    @staticmethod
    def get_one(id_categoria):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, nombre FROM CATEGORIAS WHERE id = ?", (id_categoria,))
        fila = cursor.fetchone()
        db.close()
        if fila:
            return CategoriaModel(fila['id'], fila['nombre'])
        return None
    def update(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE CATEGORIAS SET nombre = ? WHERE id = ?", # <-- ESTO FALTABA
            (self.descripcion, self.id_categoria)
        )
        db.commit()
        db.close()
        
    @staticmethod
    def delete(id_categoria):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM CATEGORIAS WHERE id = ?", (id_categoria,))
        db.commit()
        db.close()
        return cursor.rowcount
    
    
# PROVEEDORES
class ProveedorModel:
    def __init__(self, id_proveedor=None, nombre=None, telefono=None, direccion=None, email=None):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            'id': self.id_proveedor,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'email': self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            data.get('id'),
            data.get('nombre'),
            data.get('telefono'),
            data.get('direccion'),
            data.get('email')
        )

    def create(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (?, ?, ?, ?)", 
            (self.nombre, self.telefono, self.direccion, self.email)
        )
        self.id_proveedor = cursor.lastrowid
        db.commit()
        db.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM PROVEEDORES")
        filas = cursor.fetchall()
        proveedores = [ProveedorModel(
            fila['id'], fila['nombre'], fila['telefono'], fila['direccion'], fila['email']
        ) for fila in filas]
        db.close()
        return proveedores

    @staticmethod
    def get_one(id_proveedor):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM PROVEEDORES WHERE id = ?", (id_proveedor,))
        fila = cursor.fetchone()
        db.close()
        if fila:
            return ProveedorModel(
                fila['id'], fila['nombre'], fila['telefono'], fila['direccion'], fila['email']
            )
        return None

    def update(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE PROVEEDORES SET nombre = ?, telefono = ?, direccion = ?, email = ? WHERE id = ?", 
            (self.nombre, self.telefono, self.direccion, self.email, self.id_proveedor)
        )
        db.commit()
        db.close()
        
    @staticmethod
    def delete(id_proveedor):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM PROVEEDORES WHERE id = ?", (id_proveedor,))
        db.commit()
        db.close()
        return cursor.rowcount
    
#articulo
class ArticuloModel:
    def __init__(self, id_articulo=None, descripcion=None, precio=None, stock=None, 
                 marca=None, proveedor=None, categorias=None, 
                 marca_id=None, proveedor_id=None, categorias_ids=None):
        self.id_articulo = id_articulo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        self.categorias = categorias if categorias is not None else []
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id
        self.categorias_ids = categorias_ids if categorias_ids is not None else []

    def serializar(self):
        return {
            'id': self.id_articulo,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'marca': self.marca.serializar() if self.marca else None,
            'proveedor': self.proveedor.serializar() if self.proveedor else None,
            'categorias': [cat.serializar() for cat in self.categorias]
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT 
                a.id as articulo_id, a.descripcion as articulo_descripcion, a.precio, a.stock,
                m.id as marca_id, m.nombre as marca_nombre,
                p.id as proveedor_id, p.nombre as proveedor_nombre, p.telefono, p.direccion, p.email
            FROM 
                ARTICULOS a
            JOIN 
                MARCAS m ON a.marca_id = m.id
            JOIN 
                PROVEEDORES p ON a.proveedor_id = p.id
        """)
        
        articulos_filas = cursor.fetchall()
        
        articulos_list = []
        for fila in articulos_filas:
            marca = MarcaModel(id_marca=fila['marca_id'], descripcion=fila['marca_nombre'])
            proveedor = ProveedorModel(id_proveedor=fila['proveedor_id'], nombre=fila['proveedor_nombre'], 
                                       telefono=fila['telefono'], direccion=fila['direccion'], email=fila['email'])
            cursor_cat = db.cursor()
            cursor_cat.execute("""
                SELECT c.id, c.nombre
                FROM ARTICULOS_CATEGORIAS ac
                JOIN CATEGORIAS c ON ac.categoria_id = c.id
                WHERE ac.articulo_id = ?
            """, (fila['articulo_id'],))
            
            categorias_filas = cursor_cat.fetchall()
            
            categorias_list = [CategoriaModel(id_categoria=cat_fila['id'], descripcion=cat_fila['nombre']) for cat_fila in categorias_filas]
            
            articulo = ArticuloModel(
                id_articulo=fila['articulo_id'],
                descripcion=fila['articulo_descripcion'],
                precio=fila['precio'],
                stock=fila['stock'],
                marca=marca,
                proveedor=proveedor,
                categorias=categorias_list
            )
            articulos_list.append(articulo)

        db.close()
        return articulos_list
    @staticmethod
    def get_one(id_articulo):
        db = get_db()
        cursor = db.cursor()
        
        cursor.execute("""
            SELECT 
                a.id as articulo_id, a.descripcion as articulo_descripcion, a.precio, a.stock,
                m.id as marca_id, m.nombre as marca_nombre,
                p.id as proveedor_id, p.nombre as proveedor_nombre, p.telefono, p.direccion, p.email
            FROM 
                ARTICULOS a
            JOIN 
                MARCAS m ON a.marca_id = m.id
            JOIN 
                PROVEEDORES p ON a.proveedor_id = p.id
            WHERE a.id = ?
        """, (id_articulo,))
        
        fila = cursor.fetchone()
        
        if not fila:
            db.close()
            return None 

        marca = MarcaModel(id_marca=fila['marca_id'], descripcion=fila['marca_nombre'])
        proveedor = ProveedorModel(id_proveedor=fila['proveedor_id'], nombre=fila['proveedor_nombre'], 
                                   telefono=fila['telefono'], direccion=fila['direccion'], email=fila['email'])

        cursor_cat = db.cursor()
        cursor_cat.execute("""
            SELECT c.id, c.nombre
            FROM ARTICULOS_CATEGORIAS ac
            JOIN CATEGORIAS c ON ac.categoria_id = c.id
            WHERE ac.articulo_id = ?
        """, (fila['articulo_id'],))
        
        categorias_filas = cursor_cat.fetchall()
        categorias_list = [CategoriaModel(id_categoria=cat_fila['id'], descripcion=cat_fila['nombre']) for cat_fila in categorias_filas]
        
        articulo = ArticuloModel(
            id_articulo=fila['articulo_id'],
            descripcion=fila['articulo_descripcion'],
            precio=fila['precio'],
            stock=fila['stock'],
            marca=marca,
            proveedor=proveedor,
            categorias=categorias_list
        )
        
        db.close()
        return articulo
    
    def create(self):
        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (?, ?, ?, ?, ?)",
            (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
        )

        self.id_articulo = cursor.lastrowid


        if self.categorias_ids:
            values_to_insert = []
            for cat_id in self.categorias_ids:
                values_to_insert.append((self.id_articulo, cat_id))
            
            cursor.executemany(
                "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (?, ?)",
                values_to_insert
            )

        db.commit()
        db.close()
        
    def update(self):
        """Actualiza un artículo existente en la base de datos."""
        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            """
            UPDATE ARTICULOS 
            SET descripcion = ?, precio = ?, stock = ?, marca_id = ?, proveedor_id = ?
            WHERE id = ?
            """,
            (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id, self.id_articulo)
        )

        cursor.execute(
            "DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = ?",
            (self.id_articulo,)
        )

        if self.categorias_ids:
            values_to_insert = [(self.id_articulo, cat_id) for cat_id in self.categorias_ids]
            cursor.executemany(
                "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (?, ?)",
                values_to_insert
            )

        db.commit()
        db.close()

    @staticmethod
    def delete(id_articulo):
        """Elimina un artículo de la base de datos."""
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM ARTICULOS WHERE id = ?", (id_articulo,))
        db.commit()
        db.close()
        return cursor.rowcount       
    