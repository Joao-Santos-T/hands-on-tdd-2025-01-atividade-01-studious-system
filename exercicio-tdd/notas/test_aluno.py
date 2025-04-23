"""
Testes da classe Aluno.
"""
import pytest
from aluno import Aluno

def test_adicionar_nota():
    aluno = Aluno(nome="Daniel", matricula="123")
    aluno.adicionar_nota("Matemática", 8.0)
    assert aluno.notas["Matemática"] == [8.0]

def test_calcular_media():
    aluno = Aluno(nome="Daniel", matricula="123", notas={"Matemática": [8.0, 9.0]})
    media = aluno.calcular_media("Matemática")
    assert media == 8.5

def test_verificar_aprovacao():
    aluno = Aluno(nome="Daniel", matricula="123", notas={"Matemática": [8.0, 9.0]})
    assert aluno.verificar_aprovacao("Matemática") is True

def test_registrar_falta():
    aluno = Aluno(nome="Daniel", matricula="123")
    aluno.registrar_falta("Matemática")
    assert aluno.faltas["Matemática"] == 1

def test_calcular_frequencia():
    aluno = Aluno(nome="Daniel", matricula="123", faltas={"Matemática": 2})
    frequencia = aluno.calcular_frequencia("Matemática", 10)
    assert frequencia == 80.0

def test_calcular_media_sem_notas():
    aluno = Aluno(nome="Daniel", matricula="123", notas={})
    media = aluno.calcular_media("Matemática")
    assert media == 0.0

if __name__ == "__main__":
    pytest.main() 