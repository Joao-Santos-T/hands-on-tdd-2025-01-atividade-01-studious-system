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
        self.produto = Produto(
            codigo="001",
            nome="Caneta",
            preco=2.50,
            quantidade=20,
            data_validade=datetime.now() + timedelta(days=30),
            estoque_minimo=10
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.nome, "Caneta")
        self.assertEqual(self.produto.quantidade, 20)
        self.assertEqual(self.produto.preco, 2.50)
        self.assertFalse(self.produto.verificar_estoque_baixo())

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.quantidade, 30)

        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-5)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        resultado = self.produto.remover_estoque(5)
        self.assertTrue(resultado)
        self.assertEqual(self.produto.quantidade, 15)

        resultado_falso = self.produto.remover_estoque(100)
        self.assertFalse(resultado_falso)
        self.assertEqual(self.produto.quantidade, 15)

        with self.assertRaises(ValueError):
            self.produto.remover_estoque(-1)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.produto.quantidade = 5
        self.assertTrue(self.produto.verificar_estoque_baixo())

        self.produto.quantidade = 10
        self.assertFalse(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        self.assertEqual(self.produto.calcular_valor_total(), 50.00)

        self.produto.quantidade = 0
        self.assertEqual(self.produto.calcular_valor_total(), 0.0)

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.produto.data_validade = datetime.now() + timedelta(days=1)
        self.assertTrue(self.produto.verificar_validade())

        self.produto.data_validade = datetime.now() - timedelta(days=1)
        self.assertFalse(self.produto.verificar_validade())

        self.produto.data_validade = None
        self.assertTrue(self.produto.verificar_validade())