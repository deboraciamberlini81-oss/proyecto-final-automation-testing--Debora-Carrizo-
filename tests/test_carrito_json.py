
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.datos import leer_json
from pages.inventory_page import InventoryPage


PRODUCTOS = leer_json("productos.json")




@pytest.fixture
def usuario_logueado(driver):
    """Realiza login antes de cada test de carrito."""
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()

    wait.until(EC.url_contains("/inventory.html"))

    return driver


def buscar_producto(driver, nombre_producto):
    """Busca un producto del catálogo por su nombre."""
    wait = WebDriverWait(driver, 10)

    items = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".inventory_item")
        )
    )

    for item in items:
        nombre = item.find_element(
            By.CSS_SELECTOR, ".inventory_item_name"
        ).text

        if nombre == nombre_producto:
            return item

    return None


@pytest.mark.parametrize(
    "producto",
    PRODUCTOS,
    ids=[p["producto"] for p in PRODUCTOS]
)
def test_agregar_producto_desde_json(usuario_logueado, producto):
    """Agrega cada producto del JSON y verifica el carrito."""
    driver = usuario_logueado
    wait = WebDriverWait(driver, 10)

    producto_encontrado = buscar_producto(
        driver, producto["producto"]
    )

    assert producto_encontrado is not None, (
        f"No se encontró el producto: {producto['producto']}"
    )

    precio_texto = producto_encontrado.find_element(
        By.CSS_SELECTOR, ".inventory_item_price"
    ).text

    precio_real = float(precio_texto.replace("$", ""))

    assert precio_real == pytest.approx(producto["precio"])

    producto_encontrado.find_element(
        By.CSS_SELECTOR, "button"
    ).click()

    # Esperar a que el botón confirme que el producto fue agregado.
    wait.until(
    lambda d: producto_encontrado.find_element(
        By.CSS_SELECTOR, "button"
    ).text.strip() == "Remove"
)

# Esperar a que aparezca el contador del carrito.
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".shopping_cart_badge")
    )
)

# Verificar que el contador indique una unidad.
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".shopping_cart_badge"),
        "1"
    )
)

    inventory_page = InventoryPage(driver)
    inventory_page.abrir_carrito()

    productos_carrito = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".cart_item")
        )
    )

    producto_carrito = next(
        (
            item for item in productos_carrito
            if item.find_element(
                By.CSS_SELECTOR, ".inventory_item_name"
            ).text == producto["producto"]
        ),
        None
    )

    assert producto_carrito is not None, (
        f"{producto['producto']} no aparece en el carrito"
    )

    cantidad = int(
        producto_carrito.find_element(
            By.CSS_SELECTOR, ".cart_quantity"
        ).text
    )

    assert cantidad == 1

    print(
        f"\nTest OK: {producto['producto']} | "
        f"Precio: ${precio_real} | Cantidad: {cantidad}"
    )


@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado):
    """Verifica que se pueda agregar un producto al carrito."""
    driver = usuario_logueado
    wait = WebDriverWait(driver, 10)

    primer_producto = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".inventory_item")
        )
    )

    nombre = primer_producto.find_element(
        By.CSS_SELECTOR, ".inventory_item_name"
    ).text

    boton = primer_producto.find_element(
        By.CSS_SELECTOR, "button"
    )

    print(f"Botón antes del clic: {boton.text}")
    boton.click()

    boton_actualizado = wait.until(
        lambda d: d.find_element(
            By.CSS_SELECTOR, ".inventory_item button"
        ).text == "Remove"
    )

    print("El botón cambió a Remove")
    print(f"URL actual: {driver.current_url}")

    insignias = driver.find_elements(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    print(f"Cantidad de contadores encontrados: {len(insignias)}")

    if insignias:
        print(f"Texto del contador: {insignias[0].text}")

    assert insignias and insignias[0].text == "1", (
        "El producto no actualizó el contador del carrito"
    )

    inventory_page = InventoryPage(driver)
    inventory_page.abrir_carrito()
    
    wait.until(EC.url_contains("/cart.html"))

    producto_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
        )
    )

    assert producto_carrito.text == nombre

    print(f"\nSmoke OK: {nombre} agregado al carrito")
