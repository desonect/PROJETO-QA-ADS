import pytest

# Função que será testada
def adicionar_um(x):
    return x + 1

# Teste
def test_adicionar_um():
    assert adicionar_um(1) == 2
    assert adicionar_um(0) == 1
    assert adicionar_um(-1) == 0
