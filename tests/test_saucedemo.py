
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    yield navegador
    navegador.quit()


def iniciar_sesion(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Actividad 1: validar la redirección
    assert "/inventory.html" in driver.current_url

    # Reto extra: validar el título después de la redirección
    titulo = driver.find_element(
        By.CSS_SELECTOR, "div.header_secondary_container .title"
    ).text
    assert titulo == "Products"

    print("Test OK")


def test_actividad_1_login(driver):
    iniciar_sesion(driver)


def test_actividad_2_inventario(driver):
    iniciar_sesion(driver)

    # Confirmar que existe al menos un producto
    productos = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    assert len(productos) >= 1

    # Mostrar nombre y precio del primer producto
    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CSS_SELECTOR, ".inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CSS_SELECTOR, ".inventory_item_price"
    ).text

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")


def test_actividad_3_carrito(driver):
    iniciar_sesion(driver)

    # Seleccionar el primer producto
    productos = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    assert len(productos) >= 1

    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CSS_SELECTOR, ".inventory_item_name"
    ).text

    primer_producto.find_element(
        By.CSS_SELECTOR, "button"
    ).click()

    # Verificar que el contador del carrito muestre 1
    contador = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    ).text
    assert contador == "1"

    # Navegar al carrito
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    # Comprobar que el producto añadido está listado
    productos_carrito = driver.find_elements(
        By.CSS_SELECTOR, ".cart_item"
    )

    nombres_carrito = [
        producto.find_element(
            By.CSS_SELECTOR, ".inventory_item_name"
        ).text
        for producto in productos_carrito
    ]

    assert nombre in nombres_carrito

    print(f"Producto agregado correctamente: {nombre}")
    print("Carrito OK")
