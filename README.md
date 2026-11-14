#  Proyecto Final – QA Automation | Python, Selenium y API Testing

##  Descripción del proyecto

Este proyecto consiste en el desarrollo de una solución integral de **QA Automation**, orientada a validar la calidad, funcionalidad y estabilidad de una aplicación web mediante pruebas automatizadas de interfaz de usuario, servicios API y escenarios BDD.

Se implementó una arquitectura organizada bajo el patrón **Page Object Model (POM)**, utilizando Python, Selenium WebDriver y Pytest. Además, se incorporaron pruebas parametrizadas, gestión de datos externos, reportes HTML, logging y ejecución continua mediante GitHub Actions.

El objetivo fue desarrollar una estructura de testing reutilizable, mantenible y escalable, aplicando buenas prácticas de automatización y control de calidad de software.

##  Tecnologías y herramientas

| Tecnología | Aplicación |
|---|---|
| Python 3.12 | Lenguaje de programación |
| Selenium WebDriver | Automatización de interfaz web |
| Pytest | Ejecución y organización de pruebas |
| Page Object Model | Arquitectura y reutilización de código |
| Requests | Consumo y validación de APIs |
| Behave | Automatización BDD |
| Gherkin | Definición de escenarios funcionales |
| Postman / API Testing | Validación de servicios |
| Git y GitHub | Control de versiones |
| GitHub Actions | Integración continua (CI) |
| pytest-html | Generación de reportes |
| Logging | Registro de ejecución y diagnóstico |
| JSON y CSV | Gestión de datos de prueba |

##  Módulos implementados

### 1. Automatización de interfaz de usuario (UI Testing)

Automatización de flujos funcionales sobre SauceDemo.

- Validación de inicio de sesión positivo y negativo.
- Verificación de mensajes de error.
- Validación del catálogo de productos.
- Selección y agregado de productos al carrito.
- Verificación de cantidades y contenido del carrito.
- Pruebas parametrizadas con diferentes datos.
- Uso de esperas explícitas para mejorar la estabilidad.

### 2. Arquitectura Page Object Model (POM)

Implementación de una estructura basada en objetos de página para separar la lógica de interacción de las pruebas.

Clases principales:
- `LoginPage`
- `InventoryPage`
- `CartPage`

Beneficios:
- Reutilización de métodos.
- Menor duplicación de código.
- Mantenimiento más sencillo.
- Separación de responsabilidades.
- Mayor escalabilidad de la automatización.

### 3. Pruebas API Testing

Implementación de pruebas automatizadas para validar servicios REST.

Servicios utilizados:
- JSONPlaceholder.
- Reqres.

Validaciones realizadas:
- Métodos HTTP GET, POST y DELETE.
- Códigos de estado HTTP.
- Validación de respuestas JSON.
- Creación y consulta de usuarios.
- Validación de autenticación.
- Pruebas de ciclo de vida y secuencias de operaciones.
- Gestión de API Key mediante variables de entorno y secretos de GitHub.

### 4. Automatización BDD – Behave

Implementación de escenarios funcionales utilizando metodología Behavior Driven Development.

- Escenarios escritos en lenguaje Gherkin.
- Separación entre archivos `.feature` y definiciones de pasos.
- Automatización de escenarios de login y carrito.
- Organización de pruebas Smoke y Regression.
- Generación de reportes específicos para BDD.

### 5. Pruebas parametrizadas y gestión de datos

Implementación de datos externos para ampliar la cobertura de pruebas.

- Archivos CSV para credenciales.
- Archivos JSON para información de productos.
- Ejecución de múltiples combinaciones de datos.
- Separación entre datos y lógica de automatización.

### 6. Reportes, evidencias y logging

Configuración de herramientas para facilitar el seguimiento y análisis de las ejecuciones.

- Reportes HTML de Pytest.
- Reportes HTML de Behave.
- Registro de eventos mediante Logging.
- Capturas de pantalla para evidenciar fallos.
- Organización de archivos de reportes, evidencias y logs.

### 7. Integración continua – GitHub Actions

Configuración de un workflow para ejecutar automáticamente la suite de pruebas.

Características:
- Ejecución en entorno Ubuntu.
- Configuración de Python 3.12.
- Instalación de dependencias.
- Configuración de Chrome.
- Ejecución automatizada con Pytest.
- Uso de secretos para credenciales sensibles.
- Publicación de reportes y evidencias como artefactos.

El workflow permite verificar el estado de las pruebas ante cambios en el repositorio y mantener un control continuo de calidad.

## 📂 Estructura principal del proyecto

```text
proyecto-final-automation-testing/
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
│   ├── behave/
│   ├── steps/
│   ├── cart.feature
│   └── login.feature
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── reports/
│   ├── behave_smoke.html
│   └── behave_regression.html
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_carrito.py
│   ├── test_catalogo.py
│   └── ...
│
├── tests_api/
│   ├── test_http.py
│   ├── test_login_api.py
│   ├── test_users_api.py
│   └── ...
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
├── pytest.ini
├── behave.ini
├── requirements.txt
└── README.md
```

##  Ejecución del proyecto

Clonar el repositorio:

```bash
git clone https://github.com/deboraciamberlini81-oss/pre-entrega-debora-carrizo.git
```

Ingresar al directorio:

```bash
cd pre-entrega-debora-carrizo
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la suite de pruebas:

```bash
python -m pytest
```

Los reportes se generan dentro del directorio `reports/`.

##  Resultado del proyecto

- Suite local validada: **39 pruebas aprobadas** en la última ejecución completa.
- Automatización UI, API y BDD implementada.
- Arquitectura POM organizada y reutilizable.
- Reportes HTML y logging configurados.
- Workflow de GitHub Actions ejecutado correctamente.
- Integración final publicada en la rama `master`.

<https://github.com/deboraciamberlini81-oss/pre-entrega-debora-carrizo>

##  Competencias aplicadas

- QA Automation.
- Python y programación orientada a objetos.
- Selenium WebDriver.
- Diseño y mantenimiento de pruebas automatizadas.
- API Testing.
- Metodología BDD.
- Gestión de datos de prueba.
- Análisis de resultados y debugging.
- Control de versiones con Git.
- Integración continua y CI/CD.

---

**Autora:** Débora Carrizo  
**Proyecto:** QA Automation – Proyecto Final  
**Rama principal:** `master`  
**Estado:** Finalizado – GitHub Actions en verde.

