import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.order import calcular_total

def test_calcular_total_valido():
    assert calcular_total(10.0, 2) == 20.0

def test_calcular_total_negativo():
    assert calcular_total(-10, 2) == 0