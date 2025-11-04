import pytest
from src.calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(0, 3) == -3

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(0, 5) == 0

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero não permitida"):
        dividir(10, 0)
