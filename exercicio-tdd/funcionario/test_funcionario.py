"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""
    def setUp(self):
        self.func = Funcionario(
            nome="Ruan",
            matricula=1234,
            salario_hora=100.0,
            horas_trabalhadas=12.0,
            custo_empregador=1000.0,
            tem_comissao=True,
            valor_comissao=100.0,
            contratos_fechados=10
        )

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        self.assertEqual(self.func.calcular_salario_bruto(), 1200.0)

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        self.assertEqual(self.func.calcular_custo_total(), 2200.0)

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        self.assertEqual(self.func.calcular_comissao(), 1000.0)

    def test_salario_com_horas_zero(self):
        """Salário deve ser 0 se não houver horas trabalhadas."""
        self.func.horas_trabalhadas = 0
        self.assertEqual(self.func.calcular_salario_bruto(), 0.0)

    def test_funcionario_sem_comissao(self):
        """Comissão deve ser 0 se não recebe comissão."""
        self.func.tem_comissao = False
        self.assertEqual(self.func.calcular_comissao(), 0.0)

if __name__ == "__main__":
    unittest.main() 