import pytest
import pytest_check as check

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_catalogo_muestra_productos(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.hacer_login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    check.is_in(
        "/inventory.html",
        driver.current_url,
        "No se ingresó correctamente al inventario"
    )

    check.equal(
        inventory_page.obtener_titulo(),
        "Products",
        "El título del catálogo es incorrecto"
    )

    productos = inventory_page.obtener_productos()

    check.greater_equal(
        len(productos),
        1,
        "El catálogo no muestra productos"
    )

    nombre = inventory_page.obtener_nombre_primer_producto()
    precio = inventory_page.obtener_precio_primer_producto()

    check.is_true(
        nombre.strip() != "",
        "El nombre del primer producto está vacío"
    )

    check.is_true(
        precio.strip() != "",
        "El precio del primer producto está vacío"
    )

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")