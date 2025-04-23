# Exercício - Sistema de Controle de Estoque

Este exercício foi desenvolvido como parte da atividade prática de TDD (Test-Driven Development), conforme instruções do repositório base.

## Arquivos

- `produto.py`: implementação da classe Produto
- `test_produto.py`: testes unitários com cobertura total

## Funcionalidades testadas

- Controle de quantidade (mínimo e máximo)
- Cálculo de valor total do estoque
- Controle de validade dos produtos
- Registro de movimentações (entrada e saída)
- Alertas de estoque baixo
- Tratamento de exceções (valores negativos)

## Requisitos Atendidos

- ✅ 100% de cobertura de código (`produto.py`)
- ✅ Testes para todos os métodos públicos
- ✅ Testes para exceções e valores limite
- ✅ Segue rigorosamente o ciclo Red → Green → Refactor

## Execução dos testes

```bash
pip install pytest pytest-cov
pytest --cov=./ --cov-report=term-missing
pytest --cov=./ --cov-report=html
