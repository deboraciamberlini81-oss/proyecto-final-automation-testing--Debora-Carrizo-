
import pytest

from pages.login_page import LoginPage
from utils.datos import leer_csv_login


CASOS_LOGIN = leer_csv_login()


@pytest.mark.parametrize(
    "usuario, clave, debe_funcionar, descripcion",
    CASOS_LOGIN,
    ids=[caso[3] for caso in CASOS_LOGIN]
)
def test_login_desde_csv(
    driver, usuario, clave, debe_funcionar, descripcion
):
    """
    Verifica el inicio de sesión con datos provenientes del CSV.
    """
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.hacer_login(usuario, clave)

    if debe_funcionar:
        assert "/inventory.html" in driver.current_url, (
            f"{descripcion}: se esperaba un login exitoso"
        )
    else:
        mensaje = login_page.obtener_error()

        assert mensaje != "", (
            f"{descripcion}: se esperaba un mensaje de error"
        )


@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    """
    Smoke test: verifica que un usuario válido pueda iniciar sesión.
    """
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.hacer_login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url
