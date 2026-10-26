
import pytest

from utils.api_utils import iniciar_sesion

pytestmark = pytest.mark.api

@pytest.mark.parametrize(
    "email, password, status_esperado, debe_tener_token",
    [
        ("eve.holt@reqres.in", "cityslicka", 200, True),
        ("eve.holt@reqres.in", "", 400, False),
    ],
)
def test_login_api(email, password, status_esperado, debe_tener_token):
    respuesta = iniciar_sesion(email, password or None)

    assert respuesta.status_code == status_esperado

    datos = respuesta.json()

    if debe_tener_token:
        assert "token" in datos
        assert datos["token"]
    else:
        assert "error" in datos
