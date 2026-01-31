import os
import pyodbc

# Ruta de los archivos
RUTA = r"C:\ruta\a\tu\directorio"

# Cadena de conexión (ajusta servidor, bd, usuario, password)
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=TuBaseDeDatos;"
    "UID=usuario;"
    "PWD=password"
)

cursor = conn.cursor()

try:
    for archivo in os.listdir(RUTA):
        ruta_completa = os.path.join(RUTA, archivo)

        if os.path.isfile(ruta_completa):
            cursor.execute(
                "INSERT INTO archivos (nombre) VALUES (?)",
                (archivo,)
            )

    conn.commit()
    print("Archivos guardados en SQL Server.")
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()