from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_saucedemo(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verificar redirección
    assert "/inventory.html" in driver.current_url

    # Reto extra: validar el título después de la redirección
    assert driver.title == "Swag Labs"

    # Actividad 2 - Explorar inventario
    titulo = driver.find_element(
        By.CSS_SELECTOR, "div.header_secondary_container .title"
    )

    assert titulo.text == "Products"

    # Confirmar que existe al menos un producto
    productos = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")

    assert len(productos) > 0
    
        # Mostrar nombre y precio del primer producto
    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CSS_SELECTOR, "div.inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CSS_SELECTOR, "div.inventory_item_price"
    ).text

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")
    
    # Actividad 3 - Agregar el primer producto al carrito
    boton_carrito = primer_producto.find_element(
        By.CSS_SELECTOR, "button"
    )
    boton_carrito.click()
    
        # Verificar que el contador del carrito sea 1
    contador_carrito = driver.find_element(
        By.CSS_SELECTOR, "span.shopping_cart_badge"
    )

    assert contador_carrito.text == "1"
    
        # Ir al carrito
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    
    # Verificar que el producto esté en el carrito
    producto_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
        )
    )

    nombre_carrito = producto_carrito.text

    assert nombre_carrito == nombre

    print("Test OK")