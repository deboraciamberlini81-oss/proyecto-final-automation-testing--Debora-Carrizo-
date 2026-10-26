
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.datos import leer_json


productos = leer_json("productos.json")


@pytest.mark.parametrize("producto_datos", productos)
def test_carrito_json(producto_datos):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Abrir SauceDemo
        driver.get("https://www.saucedemo.com/")

        # 2. Iniciar sesión
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        # 3. Verificar que se abrió el inventario
        wait.until(
            EC.url_contains("/inventory.html")
        )

        # 4. Buscar el producto por su nombre
        items = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".inventory_item")
            )
        )

        producto_encontrado = None

        for item in items:
            nombre = item.find_element(
                By.CSS_SELECTOR, ".inventory_item_name"
            ).text

            if nombre == producto_datos["producto"]:
                producto_encontrado = item
                break

        assert producto_encontrado is not None, (
            f"No se encontró el producto: "
            f"{producto_datos['producto']}"
        )

        # 5. Comprobar el precio
        precio_texto = producto_encontrado.find_element(
            By.CSS_SELECTOR, ".inventory_item_price"
        ).text

        precio_real = float(precio_texto.replace("$", ""))

        assert precio_real == pytest.approx(
            producto_datos["precio"]
        ), (
            f"Precio incorrecto para {producto_datos['producto']}: "
            f"se esperaba {producto_datos['precio']} "
            f"y se encontró {precio_real}"
        )

        # 6. Agregar el producto al carrito una sola vez
        boton = producto_encontrado.find_element(
            By.CSS_SELECTOR, "button"
        )

        wait.until(
            EC.element_to_be_clickable(boton)
        ).click()

        # 7. Verificar que el botón cambió a Remove
        wait.until(
            lambda driver: producto_encontrado.find_element(
                By.CSS_SELECTOR, "button"
            ).text == "Remove"
        )

        # 8. Abrir el carrito
        wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        # 9. Verificar que se muestra el producto en el carrito
        productos_carrito = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".cart_item")
            )
        )

        nombres_carrito = [
            item.find_element(
                By.CSS_SELECTOR, ".inventory_item_name"
            ).text
            for item in productos_carrito
        ]

        assert producto_datos["producto"] in nombres_carrito, (
            f"El producto {producto_datos['producto']} "
            f"no aparece en el carrito. "
            f"Productos encontrados: {nombres_carrito}"
        )

        # 10. Verificar la cantidad del producto en el carrito
        producto_carrito = next(
            item for item in productos_carrito
            if item.find_element(
                By.CSS_SELECTOR, ".inventory_item_name"
            ).text == producto_datos["producto"]
        )

        cantidad_texto = producto_carrito.find_element(
            By.CSS_SELECTOR, ".cart_quantity"
        ).text

        assert int(cantidad_texto) == 1, (
            f"Se esperaba cantidad 1 para "
            f"{producto_datos['producto']}, "
            f"pero se encontró {cantidad_texto}"
        )

        print(
            f"\nTest OK: {producto_datos['producto']} "
            f"| Precio: ${precio_real} "
            f"| Cantidad en carrito: {cantidad_texto}"
        )

    finally:
        driver.quit()
