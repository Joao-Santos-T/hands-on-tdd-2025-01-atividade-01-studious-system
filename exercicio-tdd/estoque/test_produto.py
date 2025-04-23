import unittest
from datetime import datetime
from produto import Produto     

class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        produto = Produto(
            codigo="001",
            nome="Produto A",
            preco=10.0,
            quantidade=5,
            data_validade=datetime(2025, 12, 31),
            estoque_minimo=1,
            max_estoque=100
        )
        self.assertEqual(produto.codigo, "001")
        self.assertEqual(produto.nome, "Produto A")
        self.assertEqual(produto.preco, 10.0)
        self.assertEqual(produto.quantidade, 5)
        self.assertEqual(produto.data_validade, datetime(2025, 12, 31))
        self.assertEqual(produto.estoque_minimo, 1)
        self.assertEqual(produto.max_estoque, 100)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        produto = Produto(
            codigo="002",
            nome="Produto B",
            preco=20.0,
            quantidade=5,
            data_validade=datetime(2025, 12, 31),
            estoque_minimo=1,
            max_estoque=100
        )
        produto.adicionar_estoque(5)
        self.assertEqual(produto.quantidade, 10)

        with self.assertRaises(ValueError):
            produto.adicionar_estoque(200)  # Excedendo o estoque máximo

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        produto = Produto(
            codigo="003",
            nome="Produto C",
            preco=15.0,
            quantidade=10,
            data_validade=datetime(2025, 12, 31),
            estoque_minimo=1,
            max_estoque=100
        )
        produto.remover_estoque(3)
        self.assertEqual(produto.quantidade, 7)

        with self.assertRaises(ValueError):
            produto.remover_estoque(8)  # Tentando remover mais do que o estoque disponível

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        produto = Produto(
            codigo="004",
            nome="Produto D",
            preco=30.0,
            quantidade=2,
            data_validade=datetime(2025, 12, 31),
            estoque_minimo=3,
            max_estoque=100
        )
        self.assertTrue(produto.verificar_estoque_baixo())

        produto.quantidade = 5
        self.assertFalse(produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        produto = Produto(
            codigo="005",
            nome="Produto E",
            preco=25.0,
            quantidade=4,
            data_validade=datetime(2025, 12, 31),
            estoque_minimo=1,
            max_estoque=100
        )
        self.assertEqual(produto.calcular_valor_total(), 100.0)  # 25 * 4

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        produto_valido = Produto(
            codigo="006",
            nome="Produto F",
            preco=20.0,
            quantidade=5,
            data_validade=datetime(2025, 12, 31),
            estoque_minimo=1,
            max_estoque=100
        )
        produto_vencido = Produto(
            codigo="007",
            nome="Produto G",
            preco=20.0,
            quantidade=5,
            data_validade=datetime(2023, 12, 31),
            estoque_minimo=1,
            max_estoque=100
        )
        self.assertTrue(produto_valido.verificar_validade())
        self.assertFalse(produto_vencido.verificar_validade())

    def test_verificar_validade_sem_data(self):
        """Verifica se produtos sem data de validade são considerados válidos."""
        produto = Produto(
            codigo="008",
            nome="Produto H",
            preco=10.0,
            quantidade=10,
            data_validade=None,
            estoque_minimo=1,
            max_estoque=100
        )
        self.assertTrue(produto.verificar_validade())

if __name__ == "__main__": # pragma: no cover
    unittest.main()
