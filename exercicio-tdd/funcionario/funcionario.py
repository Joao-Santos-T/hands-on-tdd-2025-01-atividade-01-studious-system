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

    def calcular_salario_bruto(self) -> float:
        """Calcula o salário bruto do funcionário.
        
        Returns:
            float: Salário bruto calculado baseado nas horas trabalhadas
        """
        if self.horas_trabalhadas < 0 or self.salario_hora < 0:
            raise ValueError("Horas trabalhadas e salário por hora devem ser não negativos.")
        return self.salario_hora * self.horas_trabalhadas

    def calcular_comissao(self) -> float:
        """Calcula o valor total da comissão do funcionário.
        
        Returns:
            float: Valor total da comissão baseado nos contratos fechados
        """
        if not self.tem_comissao:
            return 0.0
        if self.valor_comissao < 0 or self.contratos_fechados < 0:
            raise ValueError("Valor de comissão e contratos fechados devem ser não negativos.")
        return self.valor_comissao * self.contratos_fechados

    def calcular_custo_total(self) -> float:
        """Calcula o custo total do funcionário para a empresa.
        
        Returns:
            float: Custo total (salário + custos do empregador)
        """
        salario = self.calcular_salario_bruto()
        comissao = self.calcular_comissao()
        if self.custo_empregador < 0:
            raise ValueError("Custo do empregador deve ser não negativo.")
        return salario + self.custo_empregador + comissao
