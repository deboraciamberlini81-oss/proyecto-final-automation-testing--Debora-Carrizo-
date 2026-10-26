
from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    # Localizadores
    USERNAME = (By.CSS_SELECTOR, "#user-name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)

    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.USERNAME).send_keys(usuario)

    def ingresar_contrasena(self, contrasena):
        self.driver.find_element(*self.PASSWORD).send_keys(contrasena)

    def hacer_login(self, usuario, contrasena):
        self.ingresar_usuario(usuario)
        self.ingresar_contrasena(contrasena)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def obtener_error(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
