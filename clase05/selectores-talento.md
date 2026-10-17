# Práctica QA Automation: Selectores CSS y XPath

## 1. Objetivo

Identificar y validar selectores CSS y XPath relativos de los elementos del formulario de inicio de sesión de SauceDemo utilizando Chrome DevTools.

**URL:** https://www.saucedemo.com/

## 2. Tabla de selectores

| Elemento | Selector CSS | XPath relativo | Resultado |
|---|---|---|---|
| Input usuario | `#user-name` | `//*[@id='user-name']` | Validado |
| Input contraseña | `#password` | `//*[@id='password']` | Validado |
| Botón Login | `#login-button` | `//*[@id='login-button']` | Validado |

## 3. Validación de CSS

Se utilizó `document.querySelector()` para localizar los elementos y modificar temporalmente su borde.

```javascript
document.querySelector('#user-name').style.outline = '2px solid lime';
document.querySelector('#password').style.outline = '2px solid lime';
document.querySelector('#login-button').style.outline = '2px solid lime';
```

Se comprobó la cantidad de elementos encontrados mediante `document.querySelectorAll().length`. El resultado esperado para cada selector es 1.

## 4. Validación de XPath

Se utilizó `$x()` en la consola de Chrome para comprobar los selectores XPath.

```javascript
$x("//*[@id='user-name']").length
$x("//*[@id='password']").length
$x("//*[@id='login-button']").length
```

El resultado esperado para cada expresión es 1.

## 5. Snippet de prueba masiva CSS

```javascript
const selectores = {
  "Usuario": "#user-name",
  "Contraseña": "#password",
  "Botón Login": "#login-button"
};

const resultados = Object.entries(selectores).map(
  ([elemento, selector]) => {
    const encontrado = document.querySelectorAll(selector);

    return {
      elemento,
      selector,
      cantidad: encontrado.length,
      resultado: encontrado.length === 1 ? "OK" : "REVISAR"
    };
  }
);

console.table(resultados);
```

Este snippet permite comprobar de forma conjunta si cada selector encuentra exactamente un elemento.

## 6. Bonus: cambio de color

```javascript
const campos = [
  "#user-name",
  "#password",
  "#login-button"
];

campos.forEach((selector) => {
  document.querySelectorAll(selector).forEach((elemento) => {
    elemento.style.backgroundColor = "lightblue";
    elemento.style.outline = "2px solid blue";
  });
});
```

El código modifica temporalmente el estilo visual de los elementos encontrados para facilitar su identificación.

## 7. Conclusión

Se practicó la identificación de elementos HTML, la validación de selectores CSS y XPath y la ejecución de JavaScript desde Chrome DevTools. Estas técnicas son fundamentales para localizar elementos en pruebas automatizadas con Selenium.

**Estado:** selectores individuales comprobados en Chrome DevTools. Ejecutar el snippet masivo antes de la entrega final.

## 8. Snippet de test masivo y validación visual

El siguiente código comprueba los selectores CSS de usuario, contraseña y botón Login. Si encuentra los elementos, les aplica un cambio visual.

```javascript
['#user-name', 'input[type="password"]', '.btn_action']
.forEach(sel => {
  const el = document.querySelector(sel);

  if (el) {
    el.style.background = 'khaki';
    el.style.outline = '3px solid red';
  }
});
```

**Resultado:** los tres selectores encuentran un elemento y se aplica un borde rojo para identificarlos visualmente. El fondo puede conservar un tono celeste debido al autocompletado de Chrome.

## 9. Conclusión final

Se identificaron y comprobaron tres selectores CSS y sus correspondientes XPath relativos mediante Chrome DevTools. También se ejecutó un snippet masivo para localizar los elementos y comprobarlos visualmente antes de utilizarlos en pruebas automatizadas con Selenium.