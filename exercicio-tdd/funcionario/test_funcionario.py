"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def setup(self):
        return Funcionario("Jorge", 1, 100.0, 8.0, 1000.0, True, 100.0, 2)

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        funcionario = self.setup()
        resultadoEsperado = 1000.0
        resultado = funcionario.calcular_salario_bruto()
        assert resultado == resultadoEsperado

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        funcionario = self.setup()
        resultadoEsperado = 2000.0
        resultado = funcionario.calcular_custo_total()
        assert resultado == resultadoEsperado

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        funcionario = self.setup()
        resultadoEsperado = 200.0
        resultado = funcionario.calcular_comissao()
        assert resultado == resultadoEsperado

    def test_retorna_salario_zerado_se_salario_bruto_negativo(self):
        """Testa o cálculo do salário bruto com valor negativo."""
        funcionario = Funcionario("Jorge", 1, 100.0, -10, 1000.0, True, 100.0, 2)
        resultado = funcionario.calcular_salario_bruto()
        assert resultado == 0

    def test_retorna_custo_total_zerado_se_custo_total_negativo(self):
        """Testa o cálculo do custo total com valor negativo."""
        funcionario = Funcionario("Jorge", 1, 100.0, 0, -29, False, 100.0, 2)
        resultado = funcionario.calcular_custo_total()
        assert resultado == 0

    def test_retorna_comissao_zerada_se_sem_comissao(self):
        """Testa o cálculo da comissão quando não há comissão."""
        funcionario = Funcionario("Jorge", 1, 100.0, 0, 29, False, 100.0, 2)
        resultado = funcionario.calcular_comissao()
        assert resultado == 0
