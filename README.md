# Pre-Entrega Automation Testing — Debora Carrizo

## Propósito

Este proyecto tiene como objetivo automatizar pruebas funcionales sobre la aplicación web SauceDemo mediante Selenium WebDriver y Pytest, utilizando el patrón de diseño **Page Object Model (POM)**.

Las pruebas verifican el inicio de sesión, la visualización del catálogo de productos y la funcionalidad del carrito de compras.

## Tecnologías utilizadas

- Python 3.12
- Selenium WebDriver
- Pytest
- pytest-html
- Visual Studio Code
- Git y GitHub

## Estructura del proyecto

```text
pre-entrega-debora-carrizo/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
├── reports/
├── pytest.ini
├── README.md
└── preentrega_pom.html
```

## Instalación de dependencias

Activar el entorno de trabajo:

```bash
conda activate qa-automation
```

Instalar las dependencias necesarias:

```bash
pip install selenium pytest pytest-html
```

## Ejecución de las pruebas

Para ejecutar todas las pruebas del proyecto:

```bash
pytest -v
```

Para ejecutar únicamente las pruebas marcadas como `smoke` y generar el informe HTML:

```bash
pytest -m smoke --html=preentrega_pom.html
```

## Casos de prueba automatizados

- **Login:** verifica el inicio de sesión exitoso y la redirección al inventario.
- **Catálogo:** comprueba que se muestre el título `Products` y que existan productos.
- **Carrito:** verifica que se agregue un producto y que aparezca correctamente en el carrito.

## Patrón Page Object Model

Los localizadores y las acciones de cada página están organizados en la carpeta `pages/`. Los casos de prueba de la carpeta `tests/` utilizan estas clases para separar la lógica de interacción con la aplicación de las verificaciones funcionales.

## Reporte de ejecución

El archivo `preentrega_pom.html` contiene el informe generado por pytest-html. Puede abrirse en un navegador para consultar los resultados de la ejecución.

## Aplicación bajo prueba

[https://www.saucedemo.com/](https://www.saucedemo.com/)
