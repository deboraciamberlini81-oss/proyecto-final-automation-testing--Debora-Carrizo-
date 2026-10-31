import logging
import pytest

from pytest_bdd import given, when, then, parsers

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


@pytest.fixture
def inventory_page(driver):
    logger.info("Inicializando InventoryPage")
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    logger.info("Inicializando CartPage")
    return CartPage(driver)


@given("que inicié sesión como usuario estándar")
def iniciar_sesion(inventory_page, driver):
    logger.info("Iniciando sesión con el usuario estándar")

    login = LoginPage(driver)
    login.abrir()
    login.hacer_login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    logger.info("Sesión iniciada correctamente")


@when(parsers.parse('agrego el producto "{nombre}" al carrito'))
def agregar_producto(inventory_page, nombre):
    logger.info("Agregando producto al carrito: %s", nombre)

    inventory_page.agregar_producto_por_nombre(nombre)

    logger.info("Producto agregado correctamente: %s", nombre)


@then(parsers.parse('el contador del carrito debe mostrar "{cantidad}"'))
def verificar_contador(inventory_page, cantidad):
    logger.info("Verificando contador del carrito: %s", cantidad)

    assert inventory_page.obtener_cantidad_carrito() == cantidad

    logger.info("Contador del carrito verificado correctamente")


@then(parsers.parse('el carrito debe contener el producto "{nombre}"'))
def verificar_producto_en_carrito(inventory_page, cart_page, nombre):
    logger.info("Abriendo carrito para verificar el producto: %s", nombre)

    inventory_page.abrir_carrito()

    assert cart_page.obtener_nombre_producto() == nombre

    logger.info("Producto encontrado correctamente en el carrito: %s", nombre)