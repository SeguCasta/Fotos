import os
import pyodbc
# import pymssql

# Ruta de los archivos
RUTA = r"C:\Users\seguc\OneDrive\Pictures\Álbum de cámara"

# Cadena de conexión (ajusta servidor, bd, usuario, password)
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=(localdb)\MSSQLLocalDB;"
    "DATABASE=Fotos;"
    "Trusted_Connection=yes;"
)

# conn = pymssql.connect(
#     server='(localdb)\MSSQLLocalDB)',
#     database='Fotos',
#     trusted=True  # Esto usa autenticación de Windows
# )
cursor = conn.cursor()

try:
    for i in range(30):
        for archivo in os.listdir(RUTA):
            ruta_completa = os.path.join(RUTA, archivo)

            if os.path.isfile(ruta_completa):
                cursor.execute(
                    "INSERT INTO FotosDCIM (nombre) VALUES (?)",
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