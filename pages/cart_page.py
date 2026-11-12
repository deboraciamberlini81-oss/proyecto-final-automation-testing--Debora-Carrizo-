from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_TITLE = (
        By.CSS_SELECTOR,
        ".header_secondary_container .title"
    )

    CART_ITEMS = (
        By.CSS_SELECTOR,
        ".cart_item"
    )

    CART_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        ".cart_item .inventory_item_name"
    )

    CART_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".cart_item .inventory_item_price"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def obtener_titulo(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(self.CART_TITLE)
        )
        return elemento.text

    def obtener_productos(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )
    def obtener_nombre_producto(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_PRODUCT_NAME
            )
        )
        return elemento.text

    def obtener_precio_producto(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_PRODUCT_PRICE
            )
        )
        return elemento.text

    def esta_vacio(self):
        return len(
            self.driver.find_elements(*self.CART_ITEMS)
        ) == 0
