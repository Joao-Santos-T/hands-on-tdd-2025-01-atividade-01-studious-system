"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""
    def setUp(self):
        nome: 'Ruan'
        matricula: 1234
        salario_hora: 100.0
        horas_trabalhadas: 12.0
        custo_empregador: 1000.0
        tem_comissao: True
        valor_comissao: 100.0
        contratos_fechados: 10

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        raise NotImplementedError()

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        raise NotImplementedError()

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        raise NotImplementedError()


if __name__ == "__main__":
    unittest.main() 