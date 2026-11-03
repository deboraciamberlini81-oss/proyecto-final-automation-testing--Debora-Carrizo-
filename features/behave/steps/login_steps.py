import logging

from behave import given, when, then

from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


@given("que estoy en la página de login")
def abrir_pagina_login(context):
    logger.info("Abriendo página de login")

    context.login_page = LoginPage(context.driver)
    context.login_page.abrir()


@when('ingreso el usuario "{usuario}" y la contraseña "{password}"')
def ingresar_credenciales(context, usuario, password):
    logger.info("Ingresando usuario: %s", usuario)

    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_contrasena(password)


@when("presiono el botón de login")
def presionar_login(context):
    logger.info("Presionando botón de login")

    context.driver.find_element(
        *context.login_page.LOGIN_BUTTON
    ).click()


@then("debo acceder al inventario de productos")
def verificar_login_exitoso(context):
    logger.info("Verificando acceso al inventario")

    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in context.driver.current_url


@then('debo visualizar el mensaje de error "{mensaje}"')
def verificar_mensaje_error(context, mensaje):
    logger.info("Verificando mensaje de error")

    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(
            context.login_page.ERROR_MESSAGE
        )
    )

    assert context.login_page.obtener_error() == mensaje