
import pytest

from pytest_bdd import (
    given,
    when,
    then,
    parsers,
)

from pages.login_page import LoginPage



@pytest.fixture
def login_page(driver):
    """Reutiliza el navegador y el Page Object existente."""
    return LoginPage(driver)


@given("que estoy en la página de login")
def abrir_pagina_login(login_page):
    login_page.abrir()


@when(
    parsers.re(
        r'ingreso el usuario "(?P<usuario>.*)" y la contraseña "(?P<password>.*)"'
    )
)
def ingresar_credenciales(login_page, usuario, password):
    login_page.ingresar_usuario(usuario)
    login_page.ingresar_contrasena(password)


@when("presiono el botón de login")
def presionar_login(login_page):
    login_page.driver.find_element(
        *login_page.LOGIN_BUTTON
    ).click()


@then("debo acceder al inventario de productos")
def verificar_login_exitoso(login_page):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(login_page.driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in login_page.driver.current_url


@then(
    parsers.parse(
        'debo visualizar el mensaje de error "{mensaje}"'
    )
)
def verificar_mensaje_error(login_page, mensaje):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(login_page.driver, 10).until(
        EC.visibility_of_element_located(LoginPage.ERROR_MESSAGE)
    )

    assert login_page.obtener_error() == mensaje
