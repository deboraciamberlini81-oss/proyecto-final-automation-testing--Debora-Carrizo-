
import logging
import os
import re
import base64
from pathlib import Path

import pytest
from selenium import webdriver
from html import escape


# ==========================================
# RUTAS DEL PROYECTO
# ==========================================

ROOT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT_DIR / "reports"
SCREENS_DIR = REPORTS_DIR / "screens"
LOGS_DIR = ROOT_DIR / "logs"
LOG_FILE = LOGS_DIR / "suite.log"


# ==========================================
# TABLA DE RESULTADOS HTML
# ==========================================

def pytest_html_results_table_header(cells):
    """Agrega la columna URL al reporte HTML."""
    cells.insert(2, "<th>URL</th>")


def pytest_html_results_table_row(report, cells):
    """Muestra la URL correspondiente a cada prueba."""
    url = escape(str(getattr(report, "page_url", "-")))
    cells.insert(2, f"<td>{url}</td>")

# ==========================================
# CONFIGURACIÓN Y LOGGING
# ==========================================

def pytest_configure(config):
    """Prepara carpetas, logging y metadata del reporte."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    SCREENS_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
        ],
        force=True,
    )


def pytest_metadata(metadata):
    """Agrega información del proyecto al reporte HTML."""
    metadata["Proyecto"] = "QA Automation"
    metadata["Autor"] = "Debora"
    metadata["UI"] = "SauceDemo"
    metadata["API"] = "JSONPlaceholder"


def pytest_html_report_title(report):
    """Define el título del reporte HTML."""
    report.title = "QA Automation - Reporte de pruebas"


# ==========================================
# FIXTURE SELENIUM
# ==========================================

@pytest.fixture
def driver():
    """Inicializa y cierra el navegador para las pruebas UI."""
    logging.info("Iniciando navegador Chrome")

    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--headless=new")
    opciones.add_argument("--disable-gpu")
    opciones.add_argument("--disable-extensions")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    opciones.add_argument("--window-size=1920,1080")

    navegador = webdriver.Chrome(options=opciones)

    try:
        yield navegador
    finally:
        logging.info("Cerrando navegador Chrome")
        navegador.quit()


# ==========================================
# REPORTE DE EJECUCIÓN Y CAPTURAS
# ==========================================

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Registra resultados, URL y capturas de fallos UI."""
    outcome = yield
    reporte = outcome.get_result()

    # Guardar URL de la prueba
    if reporte.when == "call":
        navegador = item.funcargs.get("driver")
        reporte.page_url = (
            navegador.current_url if navegador else "-"
        )

    # Registrar resultados en el log
    if reporte.when == "call":
        if reporte.failed:
            logging.error("FALLO: %s", item.nodeid)
        else:
            logging.info("OK: %s", item.nodeid)

    # Capturas solamente para fallos durante la ejecución
    if reporte.when != "call" or not reporte.failed:
        return

    navegador = item.funcargs.get("driver")
    if navegador is None:
        return

    nombre_seguro = re.sub(r"[^A-Za-z0-9_.-]", "_", item.nodeid)
    captura = SCREENS_DIR / f"{nombre_seguro}.png"
    try:
        if navegador.save_screenshot(str(captura)):
            logging.info("Captura guardada: %s", captura.name)

        plugin_html = item.config.pluginmanager.getplugin("html")
        if plugin_html:
            extras = getattr(reporte, "extras", [])

            imagen_base64 = base64.b64encode(
                captura.read_bytes()
    ).decode("utf-8")

            extras.append(
                plugin_html.extras.image(
                    imagen_base64,
            mime_type="image/png",
            name="Captura del fallo",
        )
    )

            reporte.extras = extras

    except Exception:
        logging.exception(
            "No se pudo guardar la captura de %s",
            item.nodeid
        )
