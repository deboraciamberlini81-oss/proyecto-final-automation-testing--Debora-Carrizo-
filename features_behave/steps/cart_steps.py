import logging

from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


@given("que inicié sesión como usuario estándar")
def iniciar_sesion(context):
    logger.info("Iniciando sesión con usuario estándar")

    context.login_page = LoginPage(context.driver)
    context.login_page.abrir()
    context.login_page.hacer_login(
        "standard_user",
        "secret_sauce"
    )

    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    context.inventory_page = InventoryPage(context.driver)
    context.cart_page = CartPage(context.driver)


@when('agrego el producto "{nombre}" al carrito')
def agregar_producto(context, nombre):
    logger.info("Agregando producto: %s", nombre)

    context.inventory_page.agregar_producto_por_nombre(nombre)


@then('el contador del carrito debe mostrar "{cantidad}"')
def verificar_contador(context, cantidad):
    logger.info("Verificando contador del carrito")

    WebDriverWait(context.driver, 10).until(
        lambda driver:
        context.inventory_page.obtener_cantidad_carrito() == cantidad
    )

    assert (
        context.inventory_page.obtener_cantidad_carrito()
        == cantidad
    )


@then('el carrito debe contener el producto "{nombre}"')
def verificar_producto(context, nombre):
    logger.info("Verificando producto en carrito")

    context.inventory_page.abrir_carrito()

    assert context.cart_page.obtener_nombre_producto() == nombre