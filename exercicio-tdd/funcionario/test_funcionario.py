"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        funcionario = Funcionario(
            nome="João",
            matricula=123,
            salario_hora=50.0,
            horas_trabalhadas=160
        )
        self.assertEqual(funcionario.calcular_salario_bruto(), 8000.0)

    def test_calcular_comissao_com_comissao(self):
        """Testa o cálculo da comissão quando o funcionário tem comissão."""
        funcionario = Funcionario(
            nome="Maria",
            matricula=456,
            tem_comissao=True,
            valor_comissao=200.0,
            contratos_fechados=5
        )
        self.assertEqual(funcionario.calcular_comissao(), 1000.0)

    def test_calcular_comissao_sem_comissao(self):
        """Testa o cálculo da comissão quando o funcionário não tem comissão."""
        funcionario = Funcionario(
            nome="Carlos",
            matricula=789,
            tem_comissao=False,
            valor_comissao=150.0,
            contratos_fechados=3
        )
        self.assertEqual(funcionario.calcular_comissao(), 0.0)

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        funcionario = Funcionario(
            nome="Ana",
            matricula=101,
            salario_hora=60.0,
            horas_trabalhadas=150,
            custo_empregador=1200.0,
            tem_comissao=True,
            valor_comissao=100.0,
            contratos_fechados=4
        )
        salario = 60.0 * 150  # 9000
        comissao = 100.0 * 4  # 400
        custo = 1200.0
        total_esperado = salario + comissao + custo
        self.assertEqual(funcionario.calcular_custo_total(), total_esperado)


if __name__ == "__main__":
    unittest.main()
