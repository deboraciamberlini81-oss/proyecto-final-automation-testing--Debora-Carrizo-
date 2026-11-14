@ui
Feature: Autenticación de usuarios en SauceDemo

  Como usuario de SauceDemo
  Quiero iniciar sesión en la aplicación
  Para acceder al catálogo de productos

  Background:
    Given que estoy en la página de login

  @smoke
  Scenario: Inicio de sesión exitoso
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And presiono el botón de login
    Then debo acceder al inventario de productos

  @regression
  Scenario Outline: Inicio de sesión con credenciales incorrectas
    When ingreso el usuario "<usuario>" y la contraseña "<password>"
    And presiono el botón de login
    Then debo visualizar el mensaje de error "<mensaje>"

  Examples:
  | usuario          | password     | mensaje                                                                            |
  | usuario_invalido | secret_sauce | Epic sadface: Username and password do not match any user in this service          |
  | locked_out_user  | secret_sauce | Epic sadface: Sorry, this user has been locked out.                                |
  |                  |              | Epic sadface: Username is required                                                 | 