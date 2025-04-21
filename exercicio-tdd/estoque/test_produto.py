"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta

from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        produto = Produto("01","monitor",1200.00,2,datetime(2025, 2, 17),5)
        return produto

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        produto = self.setUp()
        assert produto.codigo == "01"
        assert produto.nome == "monitor"
        assert produto.preco == 1200.00
        assert produto.quantidade == 2
        assert produto.data_validade == datetime(2025, 2, 17)
        assert produto.estoque_minimo == 5

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        produto = self.setUp()
        produto.adicionar_estoque(2)
        assert produto.quantidade == 4

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        produto = self.setUp()
        produto.remover_estoque(2)
        assert produto.quantidade == 0

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        produto = self.setUp()
        estoque_baixo = produto.verificar_estoque_baixo()
        assert estoque_baixo == True

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        produto = self.setUp()
        valor_total = produto.calcular_valor_total()
        assert valor_total == 2400.00

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        produto = self.setUp()
        vencido = produto.verificar_validade()
        assert vencido == True