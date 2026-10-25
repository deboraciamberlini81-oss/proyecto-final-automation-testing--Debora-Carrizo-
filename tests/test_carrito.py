
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_agregar_producto_al_carrito(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.hacer_login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    assert inventory_page.obtener_titulo() == "Products"

    nombre_producto = (
        inventory_page.obtener_nombre_primer_producto()
    )

    inventory_page.agregar_primer_producto_al_carrito()

    assert inventory_page.obtener_cantidad_carrito() == "1"

    inventory_page.abrir_carrito()

    cart_page = CartPage(driver)

    productos_carrito = cart_page.obtener_productos()
    assert len(productos_carrito) == 1

    assert (
        cart_page.obtener_nombre_producto()
        == nombre_producto
    )

    print(f"Producto agregado correctamente: {nombre_producto}")
    print("Carrito OK")
