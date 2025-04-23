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
    max_estoque: int = 100

    def adicionar_estoque(self, quantidade: int) -> None:
        """Adiciona quantidade ao estoque do produto."""
        if self.quantidade + quantidade > self.max_estoque:
            raise ValueError("Não é possível adicionar mais do que o estoque máximo permitido.")
        self.quantidade += quantidade

    def remover_estoque(self, quantidade: int) -> bool:
        """Remove quantidade do estoque do produto."""
        if self.quantidade < quantidade:
            raise ValueError("Estoque insuficiente para remoção.")
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
        if self.data_validade is None:
            return True  # Caso o produto não tenha data de validade, consideramos válido
        return self.data_validade >= datetime.now()
