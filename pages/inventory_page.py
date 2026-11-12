
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    INVENTORY_TITLE = (
        By.CSS_SELECTOR,
        "div.header_secondary_container .title"
    )

    INVENTORY_ITEMS = (
        By.CSS_SELECTOR,
        "div.inventory_item"
    )

    FIRST_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "div.inventory_item .inventory_item_name"
    )

    FIRST_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "div.inventory_item .inventory_item_price"
    )

    FIRST_ADD_TO_CART = (
        By.CSS_SELECTOR,
        "div.inventory_item button"
    )

    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    CART_LINK = (
        By.CSS_SELECTOR,
        '[data-test="shopping-cart-link"]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def obtener_titulo(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_TITLE)
        )
        return elemento.text

    def obtener_productos(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                self.INVENTORY_ITEMS
            )
        )

    def obtener_nombre_primer_producto(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_PRODUCT_NAME
            )
        )
        return elemento.text

    def obtener_precio_primer_producto(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_PRODUCT_PRICE
            )
        )
        return elemento.text

    def agregar_primer_producto_al_carrito(self):
        boton = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_ADD_TO_CART)
        )

        boton.click()

        self.wait.until(
            lambda driver: driver.find_element(
                *self.CART_BADGE
            ).text == "1"
        )

    def agregar_producto_por_nombre(self, nombre):
        cantidad_anterior = int(self.obtener_cantidad_carrito())
        productos = self.obtener_productos()

        for producto in productos:
            nombre_producto = producto.find_element(
                By.CSS_SELECTOR,
                ".inventory_item_name"
            ).text

            if nombre_producto == nombre:
                boton = producto.find_element(
                    By.CSS_SELECTOR,
                    "button"
                )
                boton.click()

                self.wait.until(
                    lambda driver: int(
                        driver.find_element(
                             *self.CART_BADGE
                        ).text
                    ) == cantidad_anterior + 1
                )
                return

        raise AssertionError(
        f"No se encontró el producto: {nombre}"
        )

    def obtener_cantidad_carrito(self):
        insignias = self.driver.find_elements(
            *self.CART_BADGE
        )

        if insignias:
            return insignias[0].text

        return "0"

    def abrir_carrito(self):
        enlace = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )


        self.driver.execute_script(
            "arguments[0].click();",
            enlace
        )

        self.wait.until(
            EC.url_contains("cart.html")
        )



