
from utils.api_utils import obtener_usuarios


def test_obtener_usuarios():
    respuesta = obtener_usuarios(page=1)

    assert respuesta.status_code == 200

    datos = respuesta.json()

    assert "data" in datos
    assert isinstance(datos["data"], list)
    assert len(datos["data"]) > 0

    claves_obligatorias = {
        "id",
        "email",
        "first_name",
        "last_name",
    }

    for usuario in datos["data"]:
        assert claves_obligatorias.issubset(usuario.keys())


def test_avatar_termina_en_jpg():
    respuesta = obtener_usuarios(page=1)

    assert respuesta.status_code == 200

    usuarios = respuesta.json()["data"]

    for usuario in usuarios:
        assert usuario["avatar"].lower().endswith(".jpg")
