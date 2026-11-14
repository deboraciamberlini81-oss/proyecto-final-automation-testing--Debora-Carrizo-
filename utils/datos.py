
import csv
import json
from pathlib import Path


# Ruta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_DIR = BASE_DIR / "datos"


def leer_csv(nombre_archivo):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios.
    """
    ruta = DATOS_DIR / nombre_archivo

    with open(ruta, mode="r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo, delimiter=";")
        return list(lector)


def leer_json(nombre_archivo):
    """
    Lee un archivo JSON y devuelve una lista de productos
    u otra estructura de datos.
    """
    ruta = DATOS_DIR / nombre_archivo

    with open(ruta, mode="r", encoding="utf-8") as archivo:
        return json.load(archivo)


def leer_csv_login(ruta_archivo="login.csv"):
    """
    Lee las credenciales desde el CSV.
    Retorna una lista de tuplas para pytest.mark.parametrize.

    Cada tupla contiene:
    usuario, clave, debe_funcionar, descripcion
    """
    casos = []

    for fila in leer_csv(ruta_archivo):
        usuario = fila["usuario"]
        clave = fila["contrasena"]
        debe_funcionar = fila["resultado"].strip().lower() == "exitoso"
        descripcion = f"Login {fila['resultado']} para {usuario}"

        casos.append(
            (usuario, clave, debe_funcionar, descripcion)
        )

    return casos


def leer_json_productos(ruta_archivo="productos.json"):
    """
    Lee los productos desde JSON.
    Retorna una lista de diccionarios para parametrizar los tests.
    """
    return leer_json(ruta_archivo)
