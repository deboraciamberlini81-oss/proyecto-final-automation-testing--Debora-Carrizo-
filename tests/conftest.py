
import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    navegador.maximize_window()

    yield navegador

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    reporte = outcome.get_result()

    if reporte.when == "call" and reporte.failed:
        navegador = item.funcargs.get("driver")

        if navegador:
            os.makedirs("reports", exist_ok=True)
            navegador.save_screenshot(
                "reports/fallo_test_saucedemo.png"
            )
