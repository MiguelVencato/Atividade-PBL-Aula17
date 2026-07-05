# tests/test_order.py
from src.order import calcular_total

def test_calcular_total_valido():
    assert calcular_total(10.0, 2) == 20.0

def test_calcular_total_negativo():
    assert calcular_total(-10, 2) == 0