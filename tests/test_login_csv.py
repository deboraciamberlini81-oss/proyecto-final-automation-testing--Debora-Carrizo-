
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.datos import leer_csv_login


CASOS_LOGIN = leer_csv_login()


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    yield navegador
    navegador.quit()


@pytest.mark.parametrize(
    "usuario, clave, debe_funcionar, descripcion",
    CASOS_LOGIN,
    ids=[caso[3] for caso in CASOS_LOGIN]
)
def test_login_desde_csv(
    driver, usuario, clave, debe_funcionar, descripcion
):
    """
    Verifica el inicio de sesión con datos provenientes del CSV.
    """
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(clave)
    driver.find_element(By.ID, "login-button").click()

    if debe_funcionar:
        assert "/inventory.html" in driver.current_url, (
            f"{descripcion}: se esperaba un login exitoso"
        )
    else:
        mensaje = driver.find_element(
            By.CSS_SELECTOR, '[data-test="error"]'
        ).text

        assert mensaje != "", (
            f"{descripcion}: se esperaba un mensaje de error"
        )


@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    """
    Smoke test: verifica que un usuario válido pueda iniciar sesión.
    """
    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.ID, "user-name"
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url
