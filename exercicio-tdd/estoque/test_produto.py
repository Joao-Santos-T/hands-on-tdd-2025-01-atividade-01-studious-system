"""
Testes da classe Produto.
"""
import pytest
from datetime import datetime, timedelta

from produto import Produto

@pytest.fixture
def produto():
    """Fixture to create a Produto instance."""
    return Produto(codigo="001", nome="Produto A", preco=10.0, quantidade=20, estoque_minimo=5)

def test_inicializacao(produto):
    """Verifica se o produto é inicializado corretamente."""
    assert produto.codigo == "001"
    assert produto.nome == "Produto A"
    assert produto.preco == 10.0
    assert produto.quantidade == 20
    assert produto.estoque_minimo == 5

def test_adicionar_estoque(produto):
    """Verifica se o estoque é adicionado corretamente."""
    produto.adicionar_estoque(10)
    assert produto.quantidade == 30

def test_adicionar_estoque_zero(produto):
    """Verifica se adicionar zero ao estoque não altera a quantidade."""
    produto.adicionar_estoque(0)
    assert produto.quantidade == 20

def test_adicionar_estoque_negativo(produto):
    """Verifica se adicionar uma quantidade negativa não altera a quantidade."""
    produto.adicionar_estoque(-5)
    assert produto.quantidade == 20

def test_remover_estoque(produto):
    """Verifica se o estoque é removido corretamente."""
    assert produto.remover_estoque(5)
    assert produto.quantidade == 15
    assert not produto.remover_estoque(100)

def test_remover_estoque_zero(produto):
    """Verifica se remover zero do estoque não altera a quantidade."""
    produto.remover_estoque(0)
    assert produto.quantidade == 20

def test_remover_estoque_negativo(produto):
    """Verifica se remover uma quantidade negativa não altera a quantidade."""
    produto.remover_estoque(-5)
    assert produto.quantidade == 20

def test_remover_estoque_mais_que_disponivel(produto):
    """Verifica se tentar remover mais do que disponível falha."""
    assert not produto.remover_estoque(25)
    assert produto.quantidade == 20

def test_verificar_estoque_baixo(produto):
    """Verifica se a detecção de estoque baixo funciona corretamente."""
    assert not produto.verificar_estoque_baixo()
    produto.remover_estoque(16)
    assert produto.verificar_estoque_baixo()

def test_verificar_estoque_baixo_quase_minimo(produto):
    """Verifica se o estoque é considerado baixo quando é um a menos que o mínimo."""
    produto.quantidade = produto.estoque_minimo - 1
    assert produto.verificar_estoque_baixo()

def test_verificar_estoque_igual_minimo(produto):
    """Verifica se o estoque não é considerado baixo quando igual ao mínimo."""
    produto.quantidade = produto.estoque_minimo
    assert not produto.verificar_estoque_baixo()

def test_calcular_valor_total(produto):
    """Verifica se o valor total é calculado corretamente."""
    assert produto.calcular_valor_total() == 200.0

def test_verificar_validade(produto):
    """Verifica se a validação de data de validade funciona corretamente."""
    produto.data_validade = datetime.now() + timedelta(days=1)
    assert produto.verificar_validade()
    produto.data_validade = datetime.now() - timedelta(days=1)
    assert not produto.verificar_validade()

def test_verificar_validade_exatamente_agora(produto):
    """Verifica se a validade é considerada válida quando a data é exatamente agora."""
    produto.data_validade = datetime.now() + timedelta(seconds=1)
    assert produto.verificar_validade()

def test_verificar_validade_none(produto):
    """Verifica se a validade é considerada válida quando data_validade é None."""
    produto.data_validade = None
    assert produto.verificar_validade()

def test_calcular_perdas(produto):
    """Verifica se o cálculo de perdas funciona corretamente."""
    produto.data_validade = datetime.now() - timedelta(days=1)
    assert produto.calcular_perdas() == 20
    produto.data_validade = datetime.now() + timedelta(days=1)
    assert produto.calcular_perdas() == 0

def test_remover_estoque_exatamente_disponivel(produto):
    """Verifica se remover exatamente a quantidade disponível funciona corretamente."""
    assert produto.remover_estoque(20)
    assert produto.quantidade == 0

def test_verificar_validade_proxima(produto):
    """Verifica se a validade é considerada válida quando a data é muito próxima do tempo atual."""
    produto.data_validade = datetime.now() + timedelta(milliseconds=1)
    assert produto.verificar_validade()

def test_calcular_valor_total_float(produto):
    """Verifica se o valor total é calculado corretamente com tolerância para floats."""
    assert pytest.approx(produto.calcular_valor_total(), 0.01) == 200.0

if __name__ == "__main__":  
    pytest.main() 