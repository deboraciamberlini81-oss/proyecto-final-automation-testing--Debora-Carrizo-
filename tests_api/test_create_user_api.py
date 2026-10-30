from datetime import datetime

import pytest

from utils.api_utils import crear_usuario

pytestmark = pytest.mark.api


@pytest.mark.parametrize(
    "nombre, trabajo",
    [
        ("Debora QA", "QA Tester"),
        ("Ana Automation", "Automation Tester"),
        ("Lucia Testing", "QA Analyst"),
        ("", "QA Tester"),
        ("Debora QA", ""),
    ],
)
def test_crear_usuario(nombre, trabajo):
    payload = {
        "name": nombre,
        "job": trabajo,
    }

    respuesta = crear_usuario(payload)
    print("Estado HTTP:", respuesta.status_code)
    print("Respuesta:", respuesta.text)

    if respuesta.status_code == 429:
        pytest.skip("API temporalmente limitada: cupo diario agotado")
    assert respuesta.status_code == 201
    datos = respuesta.json()

    assert datos["name"] == nombre
    assert datos["job"] == trabajo
    assert "id" in datos
    assert datos["id"]
    assert "createdAt" in datos
    assert datos["createdAt"]

    anio_actual = str(datetime.now().year)
    assert anio_actual in datos["createdAt"]