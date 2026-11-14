import pytest_check as check


def test_validaciones_multiples():

    nombre = "Sauce Labs Backpack"
    precio = 29.99
    stock = 10

    check.equal(nombre, "Sauce Labs Backpack", "El nombre del producto es incorrecto")
    check.equal(precio, 29.99, "El precio del producto es incorrecto")
    check.is_true(stock > 0, "El producto no tiene stock disponible")

    print("Se ejecutaron todas las validaciones")