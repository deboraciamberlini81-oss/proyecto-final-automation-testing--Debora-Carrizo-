
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_catalogo_muestra_productos(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.hacer_login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    assert "/inventory.html" in driver.current_url
    assert inventory_page.obtener_titulo() == "Products"

    productos = inventory_page.obtener_productos()
    assert len(productos) >= 1

    nombre = inventory_page.obtener_nombre_primer_producto()
    precio = inventory_page.obtener_precio_primer_producto()
    
    assert nombre.strip() != ""
    assert precio.strip() != ""

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")
