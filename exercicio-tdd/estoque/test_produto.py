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
            nome="Produto Teste",
            preco=10.0,
            quantidade=20,
            data_validade=datetime.now() + timedelta(days=10),
            estoque_minimo=10
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.codigo, "001")
        self.assertEqual(self.produto.nome, "Produto Teste")
        self.assertEqual(self.produto.preco, 10.0)
        self.assertEqual(self.produto.quantidade, 20)
        self.assertTrue(isinstance(self.produto.data_validade, datetime))
        self.assertEqual(self.produto.estoque_minimo, 10)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(5)
        self.assertEqual(self.produto.quantidade, 25)

        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(0)

        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-10)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        resultado = self.produto.remover_estoque(5)
        self.assertTrue(resultado)
        self.assertEqual(self.produto.quantidade, 15)

        resultado = self.produto.remover_estoque(20)
        self.assertFalse(resultado)
        self.assertEqual(self.produto.quantidade, 0)
        self.assertEqual(self.produto.calcular_perdas(), 5)

        with self.assertRaises(ValueError):
            self.produto.remover_estoque(0)

        with self.assertRaises(ValueError):
            self.produto.remover_estoque(-1)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.produto.quantidade = 15
        self.assertFalse(self.produto.verificar_estoque_baixo())

        self.produto.quantidade = 5
        self.assertTrue(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        self.assertEqual(self.produto.calcular_valor_total(), 200.0)

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.assertTrue(self.produto.verificar_validade())

        produto_vencido = Produto(
            codigo="002",
            nome="Vencido",
            preco=5.0,
            quantidade=10,
            data_validade=datetime.now() - timedelta(days=1)
        )
        self.assertFalse(produto_vencido.verificar_validade())

        produto_sem_validade = Produto(
            codigo="003",
            nome="Sem Validade",
            preco=5.0,
            quantidade=10,
            data_validade=None
        )
        self.assertTrue(produto_sem_validade.verificar_validade())

if __name__ == "__main__":
    unittest.main() 