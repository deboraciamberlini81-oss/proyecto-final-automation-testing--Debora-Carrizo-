@ui
@regression
Feature: Gestión del carrito de compras

  Como usuario de SauceDemo
  Quiero agregar productos al carrito
  Para verificar que se guarden correctamente

  Background:
    Given que inicié sesión como usuario estándar

  Scenario: Agregar Sauce Labs Backpack al carrito
    When agrego el producto "Sauce Labs Backpack" al carrito
    Then el contador del carrito debe mostrar "1"
    And el carrito debe contener el producto "Sauce Labs Backpack"