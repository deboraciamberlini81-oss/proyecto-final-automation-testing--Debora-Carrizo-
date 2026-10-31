import pytest

from pytest_bdd import given, when, then, parsers

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@given("que inicié sesión como usuario estándar")
def iniciar_sesion(inventory_page, driver):
    login = LoginPage(driver)
    login.abrir()
    login.hacer_login("standard_user", "secret_sauce")

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )


@when(parsers.parse('agrego el producto "{nombre}" al carrito'))
def agregar_producto(inventory_page, nombre):
    inventory_page.agregar_producto_por_nombre(nombre)


@then(parsers.parse('el contador del carrito debe mostrar "{cantidad}"'))
def verificar_contador(inventory_page, cantidad):
    assert inventory_page.obtener_cantidad_carrito() == cantidad


@then(parsers.parse('el carrito debe contener el producto "{nombre}"'))
def verificar_producto_en_carrito(inventory_page, cart_page, nombre):
    inventory_page.abrir_carrito()

    assert cart_page.obtener_nombre_producto() == nombre