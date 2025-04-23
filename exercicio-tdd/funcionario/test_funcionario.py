"""
Testes da classe Funcionario.
"""

import pytest

from funcionario import Funcionario


def test_calcular_salario_bruto():
    """Testa o cálculo do salário bruto."""
    funcionario = Funcionario(nome="Carlos", matricula=1, salario_hora=50.0, horas_trabalhadas=160)
    assert funcionario.calcular_salario_bruto() == 8000.0

def test_calcular_custo_total():
    """Testa o cálculo do custo total."""
    funcionario = Funcionario(nome="Carlos", matricula=1, salario_hora=50.0, horas_trabalhadas=160, custo_empregador=1000.0)
    assert funcionario.calcular_custo_total() == 9000.0

def test_calcular_comissao():
    """Testa o cálculo da comissão."""
    funcionario = Funcionario(nome="Carlos", matricula=1, tem_comissao=True, valor_comissao=200.0, contratos_fechados=5)
    assert funcionario.calcular_comissao() == 1000.0

def test_calcular_comissao_sem_comissao():
    """Testa o cálculo da comissão quando o funcionário não tem comissão."""
    funcionario = Funcionario(nome="Carlos", matricula=1, tem_comissao=False, valor_comissao=200.0, contratos_fechados=5)
    assert funcionario.calcular_comissao() == 0.0

def test_calcular_comissao_zero_contratos():
    """Testa o cálculo da comissão com zero contratos fechados."""
    funcionario = Funcionario(nome="Carlos", matricula=1, tem_comissao=True, valor_comissao=200.0, contratos_fechados=0)
    assert funcionario.calcular_comissao() == 0.0

def test_calcular_salario_bruto_zero_horas():
    """Testa o cálculo do salário bruto com zero horas trabalhadas."""
    funcionario = Funcionario(nome="Carlos", matricula=1, salario_hora=50.0, horas_trabalhadas=0)
    assert funcionario.calcular_salario_bruto() == 0.0

def test_calcular_salario_bruto_zero_salario():
    """Testa o cálculo do salário bruto com salário por hora zero."""
    funcionario = Funcionario(nome="Carlos", matricula=1, salario_hora=0.0, horas_trabalhadas=160)
    assert funcionario.calcular_salario_bruto() == 0.0

def test_valida_valores_negativos():
    """Testa a validação de valores negativos."""
    with pytest.raises(ValueError, match="Salário por hora não pode ser negativo."):
        Funcionario(nome="Carlos", matricula=1, salario_hora=-50.0, horas_trabalhadas=160)
    with pytest.raises(ValueError, match="Horas trabalhadas não podem ser negativas."):
        Funcionario(nome="Carlos", matricula=1, salario_hora=50.0, horas_trabalhadas=-160)

def test_valida_custo_empregador_negativo():
    """Testa a validação de custo empregador negativo."""
    with pytest.raises(ValueError, match="Custo do empregador não pode ser negativo."):
        Funcionario(nome="Carlos", matricula=1, salario_hora=50.0, horas_trabalhadas=160, custo_empregador=-1000.0)

def test_calcular_custo_total_zero_custo_empregador():
    """Testa o cálculo do custo total com custo do empregador zero."""
    funcionario = Funcionario(nome="Carlos", matricula=1, salario_hora=50.0, horas_trabalhadas=160, custo_empregador=0.0)
    assert funcionario.calcular_custo_total() == 8000.0

def test_calcular_salario_bruto_extremo():
    """Testa o cálculo do salário bruto com horas trabalhadas extremamente altas."""
    funcionario = Funcionario(nome="Carlos", matricula=1, salario_hora=50.0, horas_trabalhadas=10000)
    assert funcionario.calcular_salario_bruto() == 500000.0

def test_calcular_comissao_extremo():
    """Testa o cálculo da comissão com um número muito alto de contratos fechados."""
    funcionario = Funcionario(nome="Carlos", matricula=1, tem_comissao=True, valor_comissao=200.0, contratos_fechados=1000)
    assert funcionario.calcular_comissao() == 200000.0

def test_calcular_custo_total_extremo():
    """Testa o cálculo do custo total com um custo do empregador muito alto."""
    funcionario = Funcionario(nome="Carlos", matricula=1, salario_hora=50.0, horas_trabalhadas=160, custo_empregador=100000.0)
    assert funcionario.calcular_custo_total() == 108000.0

if __name__ == "__main__":  
    pytest.main() 