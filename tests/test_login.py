
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_login_exitoso(driver):
    login_page = LoginPage(driver)

    login_page.abrir()
    login_page.hacer_login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url

    inventory_page = InventoryPage(driver)
    assert inventory_page.obtener_titulo() == "Products"

    print("Test OK")
