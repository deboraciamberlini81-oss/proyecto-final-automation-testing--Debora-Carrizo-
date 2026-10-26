
import pytest

from utils.api_utils import obtener_usuarios

pytestmark = pytest.mark.api
@pytest.fixture(scope="module")
def respuesta_usuarios():
    respuesta = obtener_usuarios(page=1)
    print("Estado de la API:", respuesta.status_code)
    print("Respuesta de la API:", respuesta.text[:500])
    return respuesta

def test_obtener_usuarios(respuesta_usuarios):
    respuesta = respuesta_usuarios


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


def test_avatar_termina_en_jpg(respuesta_usuarios):
    respuesta = respuesta_usuarios

    assert respuesta.status_code == 200, (
        f"Se esperaba 200, pero la API respondió {respuesta.status_code}"
    )

    usuarios = respuesta.json()["data"]

    assert len(usuarios) > 0

    for usuario in usuarios:
        assert usuario["avatar"].lower().endswith(".jpg"), (
            f"El avatar no termina en .jpg: {usuario['avatar']}"
        )
