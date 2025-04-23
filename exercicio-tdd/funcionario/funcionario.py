"""
Sistema de gerenciamento de funcionários.
"""
from dataclasses import dataclass


@dataclass
class Funcionario:
    """Representação de um funcionário com foco em custos trabalhistas e comissões.
    
    Attributes:
        nome: Nome do funcionário
        matricula: Número de matrícula do funcionário
        salario_hora: Valor do salário por hora trabalhada
        horas_trabalhadas: Quantidade de horas trabalhadas no mês
        custo_empregador: Custo fixo mensal do empregador (INSS, FGTS, etc)
        tem_comissao: Indica se o funcionário recebe comissão
        valor_comissao: Valor da comissão por contrato fechado
        contratos_fechados: Número de contratos fechados no mês
    """

    nome: str
    matricula: int
    salario_hora: float = 100.0
    horas_trabalhadas: float = 0.0
    custo_empregador: float = 1000.0
    tem_comissao: bool = True
    valor_comissao: float = 100.0
    contratos_fechados: int = 0

    def __post_init__(self):
        if self.salario_hora < 0:
            raise ValueError("Salário por hora não pode ser negativo.")
        if self.horas_trabalhadas < 0:
            raise ValueError("Horas trabalhadas não podem ser negativas.")
        if self.custo_empregador < 0:
            raise ValueError("Custo do empregador não pode ser negativo.")

    def calcular_salario_bruto(self) -> float:
        return self.salario_hora * self.horas_trabalhadas

    def calcular_custo_total(self) -> float:
        return self.calcular_salario_bruto() + self.custo_empregador

    def calcular_comissao(self) -> float:
        if self.tem_comissao:
            return self.valor_comissao * self.contratos_fechados
        return 0.0