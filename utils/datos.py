
import csv
import json
from pathlib import Path


# Ruta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_DIR = BASE_DIR / "datos"


def leer_csv(nombre_archivo):
    ruta = DATOS_DIR / nombre_archivo

    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo, delimiter=";")
        return list(lector)


def leer_json(nombre_archivo):
    ruta = DATOS_DIR / nombre_archivo

    with open(ruta, mode="r", encoding="utf-8") as archivo:
        return json.load(archivo)
