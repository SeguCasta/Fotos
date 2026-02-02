import os
import shutil
import pyodbc
import logging
from datetime import datetime

# --- CONFIGURACIÓN ---
SERVER = "TU_SERVIDOR"
DATABASE = "TU_BD"
TABLA = "dbo.CopiaFicheros"

CONN_STR = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=(localdb)\MSSQLLocalDB;"
    "DATABASE=Fotos;"
    "Trusted_Connection=yes;"
)


LOG_FILE = "copiador_ficheros.log"


def configurar_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


def copiar_ficheros():
    conn = pyodbc.connect(CONN_STR)
    conn.autocommit = False
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT Id, RutaOrigen, NombreFichero, RutaDestino
        FROM {TABLA}
        WHERE Copiado = 0
    """)

    filas = cursor.fetchall()

    for id_, ruta_origen, nombre_fichero, ruta_destino in filas:
        # Eliminar espacios finales en ruta_origen y nombre_fichero
        if isinstance(ruta_origen, str):
            ruta_origen = ruta_origen.strip()
        if isinstance(nombre_fichero, str):
            nombre_fichero = nombre_fichero.strip()

        origen = os.path.join(ruta_origen, nombre_fichero)
        destino = os.path.join(ruta_destino, nombre_fichero)

        try:
            os.makedirs(ruta_destino, exist_ok=True)

            if not os.path.isfile(origen):
                raise FileNotFoundError(f"No existe el fichero: {origen}")

            if os.path.exists(destino):
                raise FileExistsError(f"El fichero ya existe en destino: {destino}")

            shutil.move(origen, destino)

            cursor.execute(f"""
                UPDATE {TABLA}
                SET Copiado = 1,
                    FechaCopia = ?,
                    Error = NULL
                WHERE Id = ?
            """, datetime.now(), id_)

            conn.commit()
            logging.info(f"Movido OK: {origen} -> {destino}")

        except Exception as e:
            conn.rollback()

            cursor.execute(f"""
                UPDATE {TABLA}
                SET Error = ?
                WHERE Id = ?
            """, str(e), id_)

            conn.commit()
            logging.error(f"Error copiando {origen}: {e}")

    conn.close()


if __name__ == "__main__":
    configurar_logging()
    copiar_ficheros()
