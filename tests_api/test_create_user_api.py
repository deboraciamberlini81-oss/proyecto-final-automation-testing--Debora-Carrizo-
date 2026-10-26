
from datetime import datetime

import pytest

from utils.api_utils import crear_usuario


@pytest.mark.api
@pytest.mark.parametrize(
    "nombre, trabajo",
    [
        ("Debora QA", "QA Tester"),
        ("Ana Automation", "Automation Tester"),
        ("Lucia Testing", "QA Analyst"),
    ],
)
def test_crear_usuario(nombre, trabajo):
    payload = {
        "name": nombre,
        "job": trabajo,
    }

    respuesta = crear_usuario(payload)

    assert respuesta.status_code == 201

    datos = respuesta.json()

    assert datos["name"] == nombre
    assert datos["job"] == trabajo
    assert "id" in datos
    assert "createdAt" in datos

    anio_actual = str(datetime.now().year)
    assert anio_actual in datos["createdAt"]
