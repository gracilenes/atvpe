import pytest


# Teste para a função saudacao
@pytest.mark.parametrize("nome, saudacao_esperada", [("Alice", "Olá, Alice!"), ("Bob", "Olá, Bob!")])
def test_saudacao(nome, saudacao_esperada):
    assert saudacao(nome) == saudacao_esperada

# Teste para a função dobro
@pytest.mark.parametrize("numero, resultado_esperado", [(2, 4), (0, 0), (-2, -4)])
def test_dobro(numero, resultado_esperado):
    assert dobro(numero) == resultado_esperado
