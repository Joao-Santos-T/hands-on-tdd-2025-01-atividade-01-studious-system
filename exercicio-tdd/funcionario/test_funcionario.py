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
            matricula=1,
            salario_hora=50.0,
            horas_trabalhadas=160
        )
        self.assertEqual(funcionario.calcular_salario_bruto(), 8000.0)

        funcionario.horas_trabalhadas = -5
        with self.assertRaises(ValueError):
            funcionario.calcular_salario_bruto()

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        funcionario = Funcionario(
            nome="Maria",
            matricula=2,
            tem_comissao=True,
            valor_comissao=200.0,
            contratos_fechados=3
        )
        self.assertEqual(funcionario.calcular_comissao(), 600.0)

        funcionario.tem_comissao = False
        self.assertEqual(funcionario.calcular_comissao(), 0.0)

        funcionario.tem_comissao = True
        funcionario.contratos_fechados = -1
        with self.assertRaises(ValueError):
            funcionario.calcular_comissao()

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        funcionario = Funcionario(
            nome="Ana",
            matricula=3,
            salario_hora=100.0,
            horas_trabalhadas=100,
            custo_empregador=500.0,
            tem_comissao=True,
            valor_comissao=50.0,
            contratos_fechados=2
        )
        salario = 100.0 * 100  # 10.000
        comissao = 50.0 * 2    #    100
        custo_total = salario + comissao + 500.0
        self.assertEqual(funcionario.calcular_custo_total(), custo_total)

        funcionario.custo_empregador = -100
        with self.assertRaises(ValueError):
            funcionario.calcular_custo_total()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
