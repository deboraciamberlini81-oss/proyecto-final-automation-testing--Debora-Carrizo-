# Proyecto Final - QA Automation | Débora Carrizo

Framework de automatización de pruebas funcionales, de interfaz web y API, desarrollado con Python. Integra Selenium WebDriver, Pytest, Page Object Model (POM), Behave (BDD) y ejecución continua mediante GitHub Actions.

## Objetivo

Desarrollar una solución de automatización que permita validar funcionalidades críticas de una aplicación web, comprobar servicios REST y ejecutar escenarios de prueba bajo distintos enfoques de testing.

Aplicación web utilizada: [SauceDemo](https://www.saucedemo.com/).

Servicios de API utilizados: JSONPlaceholder y Reqres.

## Tecnologías y herramientas

- Python 3.12
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Behave y Gherkin (BDD)
- Requests
- Faker
- pytest-html
- Git y GitHub
- GitHub Actions
- Visual Studio Code

## Cobertura de pruebas

### 1. Pruebas de interfaz (UI Testing)

Automatización de funcionalidades de SauceDemo:

- Inicio de sesión exitoso.
- Validación de credenciales incorrectas.
- Verificación de usuarios bloqueados.
- Visualización del catálogo de productos.
- Incorporación de productos al carrito.
- Validación del contador y contenido del carrito.
- Pruebas parametrizadas.
- Validaciones múltiples mediante soft assertions.

### 2. Pruebas de API (API Testing)

Validación de servicios REST mediante Requests:

- GET: consulta de recursos.
- POST: creación de recursos.
- PUT: actualización completa.
- PATCH: actualización parcial.
- DELETE: eliminación de recursos.
- Validación de códigos HTTP y respuestas JSON.
- Pruebas positivas y negativas de autenticación.
- Ciclo de vida de un recurso mediante POST, PATCH y DELETE.

**Nota:** JSONPlaceholder y Reqres son servicios de demostración. Las operaciones de escritura no representan persistencia real de datos.

### 3. Pruebas BDD (Behavior Driven Development)

Implementación de escenarios con Behave y Gherkin:

- Suite Smoke: validación del inicio de sesión exitoso.
- Suite Regression: carrito de compras y escenarios de autenticación.
- Integración de Behave con Pytest.
- Generación de reportes HTML, JSON y texto.

### 4. Arquitectura y buenas prácticas

- Page Object Model para separar la lógica de interacción con la interfaz.
- Esperas explícitas para mejorar la sincronización.
- Fixtures reutilizables.
- Parametrización de escenarios.
- Marcadores de Pytest.
- Utilidades compartidas para solicitudes HTTP y datos.
- Logging y capturas automáticas ante fallos.

## Estructura del proyecto

```text
proyecto-final-automation-testing-debora-carrizo/
│
├── .github/
│   └── workflows/
│       └── qa-tests.yml
│
├── datos/
│   ├── login.csv
│   └── productos.json
│
├── features/
│   └── behave/
│       ├── cart.feature
│       ├── login.feature
│       ├── environment.py
│       └── steps/
│           ├── cart_steps.py
│           └── login_steps.py
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── reports/
│   ├── behave_smoke.html
│   ├── behave_smoke.json
│   ├── behave_smoke_pretty.txt
│   ├── behave_regression.html
│   ├── behave_regression.json
│   ├── behave_regression_pretty.txt
│   └── inventario_saucedemo.png
│
├── tests/
│   ├── conftest.py
│   ├── test_carrito.py
│   ├── test_carrito_json.py
│   ├── test_cart_bdd.py
│   ├── test_catalogo.py
│   ├── test_login.py
│   ├── test_login_bdd.py
│   ├── test_login_csv.py
│   ├── test_login_parametrizado.py
│   ├── test_soft_asserts.py
│   └── saucedemo_original.py
│
├── tests_api/
│   ├── __init__.py
│   ├── test_create_user_api.py
│   ├── test_http.py
│   ├── test_login_api.py
│   ├── test_post_lifecycle.py
│   └── test_users_api.py
│
├── tests_behave/
│   └── test_behave_suite.py
│
├── utils/
│   ├── api_utils.py
│   ├── datos.py
│   └── http.py
│
├── logs/
├── assets/
├── clase05/
├── .gitignore
├── behave.ini
├── pytest.ini
├── requirements.txt
└── README.md
```

## Instalación y configuración

### Requisitos previos

- Python 3.12.
- Anaconda o Miniconda.
- Google Chrome.
- Git.

### 1. Clonar el repositorio

```bash
git clone https://github.com/deboraciamberlini81-oss/pre-entrega-debora-carrizo.git
cd pre-entrega-debora-carrizo
```

### 2. Activar el entorno

```bash
conda activate qa-automation
```

### 3. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

## Ejecución de pruebas

### Suite completa

```bash
python -m pytest
```

### Pruebas de interfaz

```bash
python -m pytest tests -v
```

### Pruebas de API

```bash
python -m pytest tests_api -v
```

### Integración BDD

```bash
python -m pytest tests_behave -v
```

### Ejecución por marcadores

```bash
python -m pytest -m smoke
python -m pytest -m api
python -m pytest -m regression
```

## Reportes y evidencias

El proyecto genera reportes HTML mediante pytest-html y reportes específicos para las suites BDD.

Las evidencias incluyen:

- Resultados de ejecución.
- Capturas de pantalla ante fallos.
- Registros de actividad.
- Reportes HTML.
- Resultados estructurados en JSON.
- Detalle de escenarios y pasos BDD.
- Captura de referencia del inventario de SauceDemo.

Los reportes generales de Pytest y los registros se generan durante la ejecución. Los artefactos de CI se publican mediante GitHub Actions.

## Integración continua (CI)

El workflow ubicado en `.github/workflows/qa-tests.yml` ejecuta las pruebas automáticamente ante los eventos configurados en GitHub.

El pipeline contempla:

1. Descarga del repositorio.
2. Configuración de Python 3.12.
3. Instalación de Google Chrome.
4. Instalación de dependencias.
5. Ejecución de Pytest.
6. Publicación de reportes, logs y capturas como artefactos.

## Resultados de validación

En la ejecución documentada del 12 de noviembre de 2026:

| Suite | Aprobados | Fallidos | Omitidos |
|---|---:|---:|---:|
| Pytest general | 39 | 0 | 0 |
| BDD Smoke | 1 | 0 | 0 |
| BDD Regression | 4 | 0 | 0 |

Los resultados corresponden a una ejecución concreta y pueden variar en futuras ejecuciones.

## Autora

**Débora Carrizo**

Proyecto de práctica y desarrollo de habilidades en QA Automation, Testing funcional, pruebas de API y automatización basada en comportamiento.