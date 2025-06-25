import sqlite3

DB_NAME = "tienda.db"

def get_db():
    """
    Función para conectarse a la base de datos.
    La conexión incluye sqlite3.Row para poder acceder a las columnas por nombre.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn