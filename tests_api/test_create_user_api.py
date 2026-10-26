
from faker import Faker

from utils.api_utils import crear_usuario


fake = Faker("es_AR")


def test_crear_usuario():
    payload = {
        "name": fake.name(),
        "job": fake.job(),
    }

    respuesta = crear_usuario(payload)

    assert respuesta.status_code == 201

    datos = respuesta.json()

    assert datos["name"] == payload["name"]
    assert datos["job"] == payload["job"]
    assert "id" in datos
    assert "createdAt" in datos
