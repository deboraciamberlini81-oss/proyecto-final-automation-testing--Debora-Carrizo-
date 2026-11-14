import logging
import pytest

from pytest_bdd import (
    given,
    when,
    then,
    parsers,
)

from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


@pytest.fixture
def login_page(driver):
    """Reutiliza el navegador y el Page Object existente."""
    logger.info("Inicializando LoginPage")
    return LoginPage(driver)


@given("que estoy en la página de login")
def abrir_pagina_login(login_page):
    logger.info("Abriendo la página de login")
    login_page.abrir()


@when(
    parsers.re(
        r'ingreso el usuario "(?P<usuario>.*)" y la contraseña "(?P<password>.*)"'
    )
)
def ingresar_credenciales(login_page, usuario, password):
    logger.info("Ingresando credenciales del usuario: %s", usuario)
    login_page.ingresar_usuario(usuario)
    login_page.ingresar_contrasena(password)


@when("presiono el botón de login")
def presionar_login(login_page):
    logger.info("Presionando el botón de login")
    login_page.driver.find_element(
        *login_page.LOGIN_BUTTON
    ).click()


@then("debo acceder al inventario de productos")
def verificar_login_exitoso(login_page):
    logger.info("Verificando acceso al inventario")

    WebDriverWait(login_page.driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in login_page.driver.current_url
    logger.info("Login exitoso: acceso al inventario confirmado")


@then(
    parsers.parse(
        'debo visualizar el mensaje de error "{mensaje}"'
    )
)
def verificar_mensaje_error(login_page, mensaje):
    logger.info("Verificando mensaje de error de login")

    WebDriverWait(login_page.driver, 10).until(
        EC.visibility_of_element_located(LoginPage.ERROR_MESSAGE)
    )

    assert login_page.obtener_error() == mensaje
    logger.info("Mensaje de error verificado correctamente")