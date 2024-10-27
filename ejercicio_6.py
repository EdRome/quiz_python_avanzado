import sqlite3

class database_connection_manager:
    """Context manager to manage a SQLite database conection."""
    
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.conexion = None

    def __enter__(self):
        # Open connection to database
        self.conexion = sqlite3.connect(self.db_url)
        print(f"Connection to database '{self.db_url}' open.")
        return self.conexion

    def __exit__(self, exc_type, exc_value, traceback):
        # Close connection to database
        if self.conexion:
            self.conexion.close()
            print(f"Connection to database '{self.db_url}' close.")


db_url = 'example.db'

with database_connection_manager(db_url) as conexion:
    cursor = conexion.cursor()
    # Realiza operaciones en la base de datos, por ejemplo, crear una tabla
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT)")
    cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", ("Alice",))
    cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", ("Bob",))
    conexion.commit()

with database_connection_manager(db_url) as conn:
  cursor = conn.cursor()
  cursor = conn.execute("SELECT * FROM usuarios;")
  print(cursor.fetchall())