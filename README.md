# Proyecto QA Automation – Debora Carrizo

## 1. Descripción del proyecto

Este proyecto tiene como objetivo implementar pruebas automatizadas funcionales sobre aplicaciones web y servicios API, utilizando Python, Pytest, Selenium WebDriver y Requests.

Se utiliza el patrón de diseño **Page Object Model (POM)** para organizar y reutilizar el código de automatización.

El proyecto contempla pruebas de interfaz de usuario (UI), pruebas de API, validaciones funcionales, manejo de datos externos y generación de reportes automatizados.

## 2. Objetivos

- Automatizar escenarios funcionales de una aplicación web.
- Validar el inicio de sesión, catálogo de productos y carrito de compras.
- Realizar pruebas de servicios REST API.
- Aplicar buenas prácticas de programación y organización del código.
- Implementar validaciones múltiples mediante Soft Assertions.
- Incorporar reintentos automáticos para pruebas inestables.
- Integrar la ejecución de pruebas mediante GitHub Actions.

## 3. Tecnologías y herramientas

| Tecnología | Utilización |
|---|---|
| Python 3.12 | Lenguaje de programación |
| Pytest | Framework de testing |
| Selenium WebDriver | Automatización de interfaces web |
| Requests | Pruebas de servicios API |
| pytest-html | Generación de reportes HTML |
| pytest-check | Soft Assertions |
| pytest-rerunfailures | Reintentos automáticos |
| Faker | Generación de datos de prueba |
| CSV y JSON | Administración de datos externos |
| Git | Control de versiones |
| GitHub | Repositorio remoto |
| GitHub Actions | Integración continua (CI) |
| Visual Studio Code | Entorno de desarrollo |

## 4. Estructura del proyecto

```text
pre-entrega-debora-carrizo/
│
├── .github/
│   └── workflows/
│       └── qa-tests.yml
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_catalogo.py
│   ├── test_carrito.py
│   ├── test_carrito_json.py
│   ├── test_login_csv.py
│   └── test_soft_asserts.py
│
├── tests_api/
│   ├── test_create_user_api.py
│   ├── test_login_api.py
│   ├── test_post_lifecycle.py
│   └── test_users_api.py
│
├── utils/
│   ├── api_utils.py
│   └── datos.py
│
├── datos/
│   ├── login.csv
│   └── productos.json
│
├── reports/
├── logs/
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

## 5. Instalación y configuración

### Requisitos previos

- Python 3.12.
- Google Chrome.
- Git.
- Anaconda o entorno virtual de Python.

### Activar el entorno de trabajo

```bash
conda activate qa-automation
```

### Instalar las dependencias

Desde la raíz del proyecto ejecutar:

```bash
pip install -r requirements.txt
```

## 6. Ejecución de las pruebas

### Ejecutar las pruebas de interfaz de usuario

```bash
pytest tests -v
```

### Ejecutar las pruebas de API

```bash
pytest tests_api -v
```

### Ejecutar todas las pruebas

```bash
pytest tests tests_api -v
```

### Ejecutar pruebas Smoke

```bash
pytest tests -m smoke
```

### Ejecutar pruebas API

```bash
pytest tests_api -m api
```

### Ejecutar una prueba específica

```bash
pytest tests/test_login.py -v
```

## 7. Funcionalidades implementadas

### Pruebas UI con Selenium

Se automatizan escenarios funcionales sobre SauceDemo:

- Inicio de sesión.
- Validación de acceso al inventario.
- Visualización del catálogo.
- Verificación de productos y precios.
- Agregado de productos al carrito.
- Validación del contenido del carrito.

### Page Object Model (POM)

Las clases de la carpeta `pages/` encapsulan los localizadores y las acciones de cada página.

Los tests utilizan estos objetos para separar la interacción con la aplicación de las validaciones funcionales.

### Pruebas API con Requests

Se realizan validaciones sobre servicios REST API, verificando:

- Códigos de respuesta HTTP.
- Estructura de los datos JSON.
- Existencia de campos obligatorios.
- Creación y autenticación de usuarios.
- Ciclo de vida de recursos.

### Datos externos

Se utilizan archivos CSV y JSON para ejecutar pruebas con distintos conjuntos de datos.

### Soft Assertions

Se implementa `pytest-check` para permitir múltiples validaciones dentro de una misma prueba, registrando los errores sin detener inmediatamente su ejecución.

### Reintentos automáticos

Se utiliza `pytest-rerunfailures` para repetir pruebas seleccionadas ante posibles fallos transitorios.

Ejemplo:

```python
@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_obtener_usuarios(respuesta_usuarios):
    ...
```

## 8. Configuración de Pytest

El archivo `pytest.ini` establece:

- Directorios de búsqueda de pruebas.
- Convención de nombres de archivos y funciones.
- Rutas de importación.
- Marcadores personalizados.
- Generación automática de reportes HTML.

## 9. Reportes y evidencias

Los reportes HTML se generan en la carpeta `reports/`.

El archivo principal configurado es:

```text
reports/report.html
```

Se utiliza `pytest-html` con la opción `--self-contained-html` para generar un informe HTML independiente.

También se registran logs y capturas de pantalla para facilitar el análisis de las ejecuciones y los errores.

## 10. Integración continua – GitHub Actions

El proyecto utiliza GitHub Actions mediante el workflow:

```text
.github/workflows/qa-tests.yml
```

La integración continua permite ejecutar automáticamente las pruebas ante los eventos configurados en el workflow y comprobar que los cambios no afecten el funcionamiento del proyecto.

## 11. Aplicación bajo prueba

**SauceDemo**

https://www.saucedemo.com/

## 12. Autora

**Debora Carrizo**

Proyecto desarrollado como práctica de formación en QA Manual y QA Automation, aplicando herramientas de automatización de pruebas, validaciones funcionales y control de versiones.