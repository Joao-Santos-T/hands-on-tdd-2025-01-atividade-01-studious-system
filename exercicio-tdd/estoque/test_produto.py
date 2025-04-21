import unittest
from datetime import datetime, timedelta
from produto import Produto

class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        # Criando uma instância do produto para os testes
        self.produto = Produto(
            codigo="P001", nome="Produto Teste", preco=10.0, quantidade=20
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.codigo, "P001")
        self.assertEqual(self.produto.nome, "Produto Teste")
        self.assertEqual(self.produto.preco, 10.0)
        self.assertEqual(self.produto.quantidade, 20)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.quantidade, 30)

        # Teste de quantidade negativa (deve lançar erro)
        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-10)
        
        # Teste de quantidade zero (deve lançar erro)
        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(0)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        resultado = self.produto.remover_estoque(10)
        self.assertTrue(resultado)
        self.assertEqual(self.produto.quantidade, 10)

        # Testando tentar remover mais do que a quantidade disponível
        resultado = self.produto.remover_estoque(20)
        self.assertFalse(resultado)
        self.assertEqual(self.produto.quantidade, 10)

        # Testando remover quantidade zero (deve falhar)
        resultado = self.produto.remover_estoque(0)
        self.assertFalse(resultado)
        self.assertEqual(self.produto.quantidade, 10)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.produto.quantidade = 5
        self.assertTrue(self.produto.verificar_estoque_baixo())

        self.produto.quantidade = 15
        self.assertFalse(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        self.assertEqual(self.produto.calcular_valor_total(), 200.0)

        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.calcular_valor_total(), 300.0)

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""

        # Caso onde data_validade é None (o método deve retornar False)
        produto_sem_validade = Produto(
            codigo="P004", nome="Produto Sem Validade", preco=20.0, quantidade=10,
            data_validade=None
        )
        self.assertFalse(produto_sem_validade.verificar_validade())

        produto_expirado = Produto(
            codigo="P002", nome="Produto Expirado", preco=15.0, quantidade=10,
            data_validade=datetime.now() - timedelta(days=1)
        )

        produto_valido = Produto(
            codigo="P003", nome="Produto Valido", preco=15.0, quantidade=10,
            data_validade=datetime.now() + timedelta(days=1)
        )

        self.assertFalse(produto_expirado.verificar_validade())
        self.assertTrue(produto_valido.verificar_validade())

if __name__ == "__main__": # pragma: no cover
    unittest.main()
