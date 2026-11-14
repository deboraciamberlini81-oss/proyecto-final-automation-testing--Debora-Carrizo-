
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    # Localizadores
    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def abrir(self):
        self.driver.get(self.URL)
        self.wait.until(
        EC.visibility_of_element_located(self.USERNAME)
        )

    def ingresar_usuario(self, usuario):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        campo.send_keys(usuario)

    def ingresar_contrasena(self, contrasena):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        campo.send_keys(contrasena)

    def hacer_login(self, usuario, contrasena):
        self.ingresar_usuario(usuario)
        self.ingresar_contrasena(contrasena)

        boton = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        boton.click()

    def obtener_error(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return elemento.text
