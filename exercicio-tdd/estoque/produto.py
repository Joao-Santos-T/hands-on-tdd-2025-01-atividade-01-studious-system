"""
Sistema de controle de estoque.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Produto:
    """Representação básica de um produto no estoque."""

    codigo: str
    nome: str
    preco: float
    quantidade: int = 0
    data_validade: Optional[datetime] = None
    estoque_minimo: int = 10
    perdas: int = 0

    def adicionar_estoque(self, quantidade: int) -> None:
        """Adiciona quantidade ao estoque do produto."""
        if quantidade <= 0:
            raise ValueError("Quantidade a adicionar deve ser positiva.")
        self.quantidade += quantidade

    def remover_estoque(self, quantidade: int) -> bool:
        """Remove quantidade do estoque do produto."""
        if quantidade <= 0:
            raise ValueError("Quantidade a remover deve ser positiva.")
        if quantidade > self.quantidade:
            self.perdas += quantidade - self.quantidade
            self.quantidade = 0
            return False
        self.quantidade -= quantidade
        return True

    def verificar_estoque_baixo(self) -> bool:
        """Verifica se o estoque está abaixo do mínimo."""
        return self.quantidade < self.estoque_minimo

    def calcular_valor_total(self) -> float:
        """Calcula o valor total do produto em estoque."""
        return self.preco * self.quantidade

    def verificar_validade(self) -> bool:
        """Verifica se o produto está dentro da validade."""
        if not self.data_validade:
            return True
        return self.data_validade >= datetime.now()

    def calcular_perdas(self) -> int:
        """Retorna o total de perdas registradas por tentativa de remoção além do estoque."""
        return self.perdas
