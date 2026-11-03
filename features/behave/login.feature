# language: es

@ui
Característica: Autenticación de usuarios en SauceDemo

  Como usuario de SauceDemo
  Quiero iniciar sesión en la aplicación
  Para acceder al catálogo de productos

  Antecedentes:
    Dado que estoy en la página de login

  @smoke
  Escenario: Inicio de sesión exitoso
    Cuando ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    Y presiono el botón de login
    Entonces debo acceder al inventario de productos

  @regression
  Esquema del escenario: Inicio de sesión con credenciales incorrectas
    Cuando ingreso el usuario "<usuario>" y la contraseña "<password>"
    Y presiono el botón de login
    Entonces debo visualizar el mensaje de error "<mensaje>"

    Ejemplos:
      | usuario          | password     | mensaje                                                    |
      | usuario_invalido | secret_sauce | Epic sadface: Username and password do not match any user in this service |
      | locked_out_user  | secret_sauce | Epic sadface: Sorry, this user has been locked out.        |
      | standard_user    | clave_incorrecta   | Epic sadface: Username and password do not match any user in this service |