"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def setUp(self):
        """Configura uma instância padrão para os testes."""
        self.func = Funcionario(
            nome="Teste",
            matricula=1,
            salario_hora=100.0,
            horas_trabalhadas=10.0,
            custo_empregador=1000.0,
            tem_comissao=True,
            valor_comissao=50.0,
            contratos_fechados=2
        )

    # ===== calcular_salario_bruto =====

    def test_calcular_salario_bruto_normal(self):
        """Salário bruto calculado corretamente em condições normais."""
        self.func.salario_hora = 80.0
        self.func.horas_trabalhadas = 20.0
        self.assertEqual(self.func.calcular_salario_bruto(), 1600.0)

    def test_calcular_salario_bruto_horas_negativas(self):
        """Erro ao calcular salário bruto com horas negativas."""
        self.func.horas_trabalhadas = -5.0
        with self.assertRaises(ValueError):
            self.func.calcular_salario_bruto()

    def test_calcular_salario_bruto_salario_negativo(self):
        """Erro ao calcular salário bruto com salário por hora negativo."""
        self.func.salario_hora = -10.0
        with self.assertRaises(ValueError):
            self.func.calcular_salario_bruto()

    # ===== calcular_comissao =====

    def test_calcular_comissao_normal(self):
        """Comissão calculada corretamente em condições normais."""
        self.func.valor_comissao = 75.0
        self.func.contratos_fechados = 3
        self.assertEqual(self.func.calcular_comissao(), 225.0)

    def test_calcular_comissao_sem_comissao(self):
        """Retorna zero quando o funcionário não recebe comissão."""
        self.func.tem_comissao = False
        self.func.valor_comissao = 100.0
        self.func.contratos_fechados = 5
        self.assertEqual(self.func.calcular_comissao(), 0.0)

    def test_calcular_comissao_valor_negativo(self):
        """Erro quando o valor de comissão é negativo."""
        self.func.valor_comissao = -1.0
        self.func.contratos_fechados = 1
        with self.assertRaises(ValueError):
            self.func.calcular_comissao()

    def test_calcular_comissao_contratos_negativos(self):
        """Erro quando o número de contratos fechados é negativo."""
        self.func.valor_comissao = 10.0
        self.func.contratos_fechados = -2
        with self.assertRaises(ValueError):
            self.func.calcular_comissao()

    # ===== calcular_custo_total =====

    def test_calcular_custo_total_normal(self):
        """Cálculo do custo total em condições normais."""
        # salário: 100.0 * 10.0 = 1000.0
        # comissão: 50.0 * 2 = 100.0
        # custo empregador: 1000.0
        esperado = 1000.0 + 100.0 + 1000.0
        self.assertEqual(self.func.calcular_custo_total(), esperado)

    def test_calcular_custo_total_sem_comissao(self):
        """Custo total quando não há comissão."""
        self.func.tem_comissao = False
        # salário: 100.0 * 10.0 = 1000.0
        # comissão: 0.0
        # custo empregador: 1000.0
        esperado = 1000.0 + 0.0 + 1000.0
        self.assertEqual(self.func.calcular_custo_total(), esperado)

    def test_calcular_custo_total_custo_negativo(self):
        """Erro quando o custo do empregador é negativo."""
        self.func.custo_empregador = -500.0
        with self.assertRaises(ValueError):
            self.func.calcular_custo_total()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
