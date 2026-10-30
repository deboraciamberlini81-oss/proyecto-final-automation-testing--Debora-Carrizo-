
import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "usuario, contrasena, login_exitoso, error_esperado",
    [
        ("standard_user", "secret_sauce", True, None),
        (
            "usuario_invalido",
            "secret_sauce",
            False,
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "standard_user",
            "clave_incorrecta",
            False,
            "Epic sadface: Username and password do not match any user in this service",
        ),
    ]
)
def test_login_parametrizado(
    driver, usuario, contrasena, login_exitoso, error_esperado
):
    login_page = LoginPage(driver)

    login_page.abrir()
    login_page.hacer_login(usuario, contrasena)

    if login_exitoso:
        assert "/inventory.html" in driver.current_url
        assert driver.title == "Swag Labs"
    else:
        assert login_page.obtener_error() == error_esperado