import os
import pyodbc
from datetime import datetime

# Cadena de conexión (ajusta servidor, bd, usuario, password)
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=(localdb)\MSSQLLocalDB;"
    "DATABASE=Fotos;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

try:
    # Leer la ruta de la tabla rutasorigen
    cursor.execute("SELECT ruta FROM rutasorigen")
    rutas = cursor.fetchall()
    
    # Vaciar la tabla antes de cargar los archivos
    cursor.execute("DELETE FROM FotosDCIM")
    
    for fila in rutas:
        RUTA = fila[0].strip()
        
        # Recorrer carpetas y subcarpetas
        for raiz, carpetas, archivos in os.walk(RUTA):
            for archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)

                # Filtrar solo archivos con extensión .jpg o .dng (no distingue mayúsculas/minúsculas)
                ext = os.path.splitext(archivo)[1].lower()
                if ext not in ('.jpg', '.dng'):
                    continue

                if os.path.isfile(ruta_completa):
                    # Obtener la fecha de creación
                    timestamp = os.path.getctime(ruta_completa)
                    fecha_creacion = datetime.fromtimestamp(timestamp)
                    
                    # Obtener la fecha de modificación
                    timestamp_mod = os.path.getmtime(ruta_completa)
                    fecha_modificacion = datetime.fromtimestamp(timestamp_mod)
                    
                    # Obtener el tamaño del archivo en bytes
                    size = os.path.getsize(ruta_completa)

                    # Tipo: extensión en minúsculas sin el punto (ej: 'jpg', 'dng')
                    tipo = ext.lstrip('.')
                    
                    cursor.execute(
                        "INSERT INTO FotosDCIM (nombre, fechacreacion, fechamodificacion, ruta, isize, Tipo) VALUES (?, ?, ?, ?, ?, ?)",
                        (archivo, fecha_creacion, fecha_modificacion, raiz, int(size), tipo)
                    )

    conn.commit()
    print("Archivos guardados en SQL Server.")
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()