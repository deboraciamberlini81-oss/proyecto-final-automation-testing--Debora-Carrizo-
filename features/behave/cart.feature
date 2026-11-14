# language: es

@ui
@regression
Característica: Gestión del carrito de compras

  Como usuario de SauceDemo
  Quiero agregar productos al carrito
  Para verificar que se guarden correctamente

  Antecedentes:
    Dado que inicié sesión como usuario estándar

  Escenario: Agregar Sauce Labs Backpack al carrito
    Cuando agrego el producto "Sauce Labs Backpack" al carrito
    Entonces el contador del carrito debe mostrar "1"
    Y el carrito debe contener el producto "Sauce Labs Backpack"