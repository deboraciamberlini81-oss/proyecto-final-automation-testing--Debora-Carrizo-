import logging
from pathlib import Path

from selenium import webdriver


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
REPORTS_DIR = ROOT_DIR / "reports"
SCREENS_DIR = REPORTS_DIR / "screens"


def before_all(context):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    SCREENS_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(
                ROOT_DIR / "logs" / "behave.log",
                encoding="utf-8"
            )
        ],
        force=True
    )


def before_scenario(context, scenario):
    logging.info("Iniciando escenario: %s", scenario.name)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    context.driver = webdriver.Chrome(options=options)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        nombre = "".join(
            c if c.isalnum() or c in "-_" else "_"
            for c in scenario.name
        )

        captura = SCREENS_DIR / f"BEHAVE_ERROR_{nombre}.png"

        context.driver.save_screenshot(str(captura))
        logging.error("Escenario fallido: %s", scenario.name)

    else:
        logging.info("Escenario aprobado: %s", scenario.name)

    context.driver.quit()