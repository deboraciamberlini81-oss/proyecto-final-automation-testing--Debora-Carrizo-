
from selenium.webdriver.common.by import By


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

    def obtener_titulo(self):
        return self.driver.find_element(
            *self.CART_TITLE
        ).text

    def obtener_productos(self):
        return self.driver.find_elements(
            *self.CART_ITEMS
        )

    def obtener_nombre_producto(self):
        return self.driver.find_element(
            *self.CART_PRODUCT_NAME
        ).text

    def obtener_precio_producto(self):
        return self.driver.find_element(
            *self.CART_PRODUCT_PRICE
        ).text
