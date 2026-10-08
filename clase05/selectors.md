# Selectores de la calculadora

| Elemento | ID | Name | Clase | Selector CSS |
|---|---|---|---|---|
| Contenedor principal | `calculadora` | — | `calculadora` | `#calculadora` |
| Título | `titulo-calculadora` | — | — | `#titulo-calculadora` |
| Primer número | `numero1` | `numero1` | `campo-numero` | `#numero1` |
| Segundo número | `numero2` | `numero2` | `campo-numero` | `#numero2` |
| Contenedor de botones | `botones-operaciones` | — | `botones-operaciones` | `#botones-operaciones` |
| Botón sumar | `btn-sumar` | `sumar` | `btn-operacion` | `#btn-sumar` |
| Botón restar | `btn-restar` | `restar` | `btn-operacion` | `#btn-restar` |
| Botón multiplicar | `btn-multiplicar` | `multiplicar` | `btn-operacion` | `#btn-multiplicar` |
| Botón dividir | `btn-dividir` | `dividir` | `btn-operacion` | `#btn-dividir` |
| Resultado | `resultado-valor` | `resultado` | `resultado-valor` | `#resultado-valor` |


# Selectores de SauceDemo

| Elemento | Selector CSS | XPath |
|---|---|---|
| Usuario | `#user-name` | `//*[@id='user-name']` |
| Contraseña | `#password` | `//input[@name='password']` |
| Login | `#login-button` | `//input[@value='Login']` |

### Verificación

Los selectores fueron comprobados en Chrome DevTools y cada uno identifica un único elemento.

- Usuario: `#user-name` → 1 elemento
- Contraseña: `#password` → 1 elemento
- Login: `#login-button` → 1 elemento
