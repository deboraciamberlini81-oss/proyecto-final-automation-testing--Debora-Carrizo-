import pytest

from calculadora import sumar, restar, multiplicar, dividir


# FIXTURE DE ENTEROS
@pytest.fixture
def numeros_enteros():
    return 10, 5


# FIXTURE DE FLOTANTES
@pytest.fixture
def numeros_flotantes():
    return 0.1, 0.2


# =========================
# SUMAR
# =========================

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (10, 5, 15),
    (0, 7, 7)
])
def test_sumar_exito(a, b, esperado):
    assert sumar(a, b) == esperado


def test_sumar_error(numeros_enteros):
    a, b = numeros_enteros
    assert sumar(a, b) != 20


# =========================
# RESTAR
# =========================

@pytest.mark.parametrize("a, b, esperado", [
    (5, 3, 2),
    (10, 5, 5),
    (7, 7, 0)
])
def test_restar_exito(a, b, esperado):
    assert restar(a, b) == esperado


def test_restar_error(numeros_enteros):
    a, b = numeros_enteros
    assert restar(a, b) != 20


# =========================
# MULTIPLICAR
# =========================

def test_multiplicar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 50


def test_multiplicar_error(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) != 100


# =========================
# DIVIDIR
# =========================

def test_dividir_exito(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 2.0


@pytest.mark.exception
def test_dividir_por_cero_exception():
    with pytest.raises(ValueError):
        dividir(10, 0)


# =========================
# FLOTANTES
# =========================

def test_sumar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert sumar(a, b) == pytest.approx(0.3)