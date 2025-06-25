import sqlite3

# --- CONFIGURACIÓN ---
# Usamos un nombre de archivo fijo para la base de datos SQLite.
# El resto de la configuración de MySQL del .env se ignora.
DB_NAME = "tienda.db"

# --- ESTRUCTURA DE LAS TABLAS (SCHEMA) ---
# Adaptado para SQLite:
# - Los nombres de tablas y columnas no usan `backticks`.
# - `AUTO_INCREMENT` se reemplaza por `AUTOINCREMENT`.
# - `int(11)` se simplifica a `INTEGER`.
# - `varchar(x)` se simplifica a `TEXT`.
# - `decimal(10,2)` se reemplaza por `REAL` (para números con decimales).
TABLES = {}
TABLES['MARCAS'] = (
    "CREATE TABLE IF NOT EXISTS MARCAS ("
    "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "  nombre TEXT NOT NULL UNIQUE"
    ")"
)
TABLES['CATEGORIAS'] = (
    "CREATE TABLE IF NOT EXISTS CATEGORIAS ("
    "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "  nombre TEXT NOT NULL UNIQUE"
    ")"
)
TABLES['PROVEEDORES'] = (
    "CREATE TABLE IF NOT EXISTS PROVEEDORES ("
    "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "  nombre TEXT NOT NULL,"
    "  telefono TEXT NOT NULL,"
    "  direccion TEXT NOT NULL,"
    "  email TEXT NOT NULL UNIQUE"
    ")"
)
TABLES['ARTICULOS'] = (
    "CREATE TABLE IF NOT EXISTS ARTICULOS ("
    "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "  descripcion TEXT NOT NULL,"
    "  precio REAL NOT NULL,"
    "  stock INTEGER NOT NULL,"
    "  marca_id INTEGER NOT NULL,"
    "  proveedor_id INTEGER NOT NULL,"
    "  FOREIGN KEY (marca_id) REFERENCES MARCAS(id),"
    "  FOREIGN KEY (proveedor_id) REFERENCES PROVEEDORES(id)"
    ")"
)
TABLES["ARTICULOS_CATEGORIAS"] = (
    "CREATE TABLE IF NOT EXISTS ARTICULOS_CATEGORIAS ("
    "  articulo_id INTEGER NOT NULL,"
    "  categoria_id INTEGER NOT NULL,"
    "  PRIMARY KEY (articulo_id, categoria_id),"
    "  FOREIGN KEY (articulo_id) REFERENCES ARTICULOS(id) ON DELETE CASCADE,"
    "  FOREIGN KEY (categoria_id) REFERENCES CATEGORIAS(id) ON DELETE CASCADE"
    ")"
)

# --- DATOS INICIALES (SEEDS) ---
# La estructura de datos es la misma, pero la forma de insertar cambiará.
SEEDS = {}
SEEDS['PROVEEDORES'] = (
    "INSERT OR IGNORE INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (?, ?, ?, ?)",
    [
        ('Tech Solutions SRL', '1144556677', 'Av. Córdoba 1234, CABA', 'contacto@techsolutions.com.ar'),
        ('Informatica Total', '1167891234', 'Calle Falsa 456, Rosario', 'ventas@informatotal.com'),
        ('Redes & Cía', '1133445566', 'Av. San Martín 789, Mendoza', 'info@redesycia.com'),
        ('PC Express', '1122334455', 'Mitre 321, La Plata', 'soporte@pcexpress.com.ar'),
        ('DataSoft Argentina', '1198765432', 'Belgrano 987, Córdoba', 'contacto@datasoft.com.ar'),
        ('CompuMarket', '1177889900', 'Av. Rivadavia 4321, CABA', 'ventas@compumarket.com'),
        ('TechnoWorld', '1100112233', 'Urquiza 1111, Mar del Plata', 'info@technoworld.com.ar'),
        ('HardNet SRL', '1188997766', 'Alsina 654, Bahía Blanca', 'clientes@hardnet.com'),
        ('BitWare', '1155667788', 'Av. Colon 2020, Salta', 'bitware@correo.com'),
        ('Digital Point', '1133221100', 'San Juan 3030, Tucumán', 'digital@dp.com.ar')
    ]
)
SEEDS['MARCAS'] = (
    "INSERT OR IGNORE INTO MARCAS (nombre) VALUES (?)",
    [
        ('HP',), ('Dell',), ('Lenovo',), ('Asus',), ('Acer',),
        ('Apple',), ('Samsung',), ('LG',), ('Sony',), ('Toshiba',)
    ]
)
SEEDS['CATEGORIAS'] = (
    "INSERT OR IGNORE INTO CATEGORIAS (nombre) VALUES (?)",
    [
        ('Notebooks y Laptops',), ('Computadoras de Escritorio',), ('Tablets',), ('Monitores',), ('Impresoras',),
        ('Periféricos',), ('Redes y Conectividad',), ('Almacenamiento',), ('Software',), ('Componentes',)
    ]
)
SEEDS['ARTICULOS'] = (
    "INSERT OR IGNORE INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (?, ?, ?, ?, ?)",
    [
        ('Notebook HP Pavilion 15.6" i5 8GB RAM 512GB SSD', 450000.00, 12, 1, 1),
        ('PC de Escritorio Dell OptiPlex i7 16GB RAM 1TB HDD', 520000.00, 7, 2, 2),
        ('Tablet Lenovo M10 HD 10.1" 32GB WiFi', 190000.00, 25, 3, 3),
        ('Monitor Asus ProArt 27" 4K UHD IPS', 330000.00, 9, 4, 4),
        ('Impresora Láser HP LaserJet Pro M404dn', 240000.00, 6, 1, 5),
        ('Mouse Logitech M185 Inalámbrico', 8900.00, 60, 6, 6),
        ('Router TP-Link Archer C6 AC1200', 21000.00, 35, 7, 7),
        ('Disco Externo Seagate 2TB USB 3.0', 45000.00, 20, 8, 8),
        ('Microsoft Office 365 Personal - Licencia 1 año', 18000.00, 15, 9, 9),
        ('Memoria RAM Corsair Vengeance 8GB DDR4 3200MHz', 32000.00, 30, 10, 10)
    ]
)
SEEDS['ARTICULOS_CATEGORIAS'] = (
    "INSERT OR IGNORE INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (?, ?)",
    [
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
        (7, 7), (8, 8), (9, 9), (10, 10)
    ]
)

# --- FUNCIONES DE EJECUCIÓN PARA SQLITE ---

def create_and_seed_database():
    """Función principal que crea y puebla la base de datos SQLite."""
    try:
        # Conectarse a la base de datos (la crea si no existe)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        print(f"Base de datos '{DB_NAME}' abierta/creada correctamente.")

        # Crear las tablas
        print("\n--- Creando tablas ---")
        for table_name, table_sql in TABLES.items():
            try:
                print(f"Creando tabla {table_name}... ", end="")
                cursor.execute(table_sql)
                print("OK")
            except sqlite3.Error as e:
                print(f"Error al crear tabla {table_name}: {e}")
        
        # Poblar las tablas
        print("\n--- Poblando tablas (seeding) ---")
        for table_name, seed_data in SEEDS.items():
            query, values = seed_data
            try:
                print(f"Poblando tabla {table_name}... ", end="")
                cursor.executemany(query, values)
                # Opcional: imprimir filas insertadas
                # print(f"{cursor.rowcount} filas insertadas.")
                print("OK")
            except sqlite3.Error as e:
                print(f"Error al poblar tabla {table_name}: {e}")

        # Guardar cambios (commit) y cerrar la conexión
        conn.commit()
        print("\nCambios guardados en la base de datos.")

    except sqlite3.Error as e:
        print(f"Ha ocurrido un error con la base de datos: {e}")
    finally:
        if conn:
            conn.close()
            print("Conexión con la base de datos cerrada.")

# --- PUNTO DE ENTRADA DEL SCRIPT ---
if __name__ == "__main__":
    print("Iniciando la inicialización de la base de datos...")
    create_and_seed_database()
    print("\nProceso de inicialización finalizado.")