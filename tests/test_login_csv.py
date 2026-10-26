
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.datos import leer_csv


usuarios = leer_csv("login.csv")


@pytest.mark.parametrize("usuario_datos", usuarios)
def test_login_csv(usuario_datos):
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys(
            usuario_datos["usuario"]
        )
        driver.find_element(By.ID, "password").send_keys(
            usuario_datos["contrasena"]
        )
        driver.find_element(By.ID, "login-button").click()

        if usuario_datos["resultado"] == "exitoso":
            assert "/inventory.html" in driver.current_url
        else:
            mensaje = driver.find_element(
                By.CSS_SELECTOR, '[data-test="error"]'
            ).text
            assert mensaje != ""

    finally:
        driver.quit()
