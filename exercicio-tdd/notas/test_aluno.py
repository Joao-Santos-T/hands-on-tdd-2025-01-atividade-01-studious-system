"""
Testes da classe Aluno.
"""
import unittest

from aluno import Aluno


class TestAluno(unittest.TestCase):
    """Testes da classe Aluno."""

    def setUp(self):
        return Aluno("Pedro", "2030001", {"Matemática": []}, {"Matemática": 0})

    def test_aluno_criado_sem_nota_sem_falta(self):
        aluno = Aluno("Pedro", "2030001", None, None)
        assert aluno.notas == {}
        assert aluno.faltas == {}

    def test_adicionar_nota(self):
        """Testa se adiciona nota a uma disciplina específica"""
        aluno = self.setUp()
        aluno.adicionar_nota("Matemática", 60)
        assert aluno.notas == {"Matemática": [60]}

    def test_calcular_media(self):
        """Testa se calcula a média por disciplina"""
        aluno = self.setUp()
        aluno.adicionar_nota("Matemática", 60)
        media = aluno.calcular_media("Matemática")
        assert media == 60

    def test_verificar_aprovacao(self):
        """Testa se verifica aprovação por disciplina"""
        aluno = self.setUp()
        aluno.adicionar_nota("Matemática", 60)
        aprovado = aluno.verificar_aprovacao("Matemática")
        assert aprovado == True

    def test_registrar_falta(self):
        """Testa se registra falta por disciplina"""
        aluno = self.setUp()
        aluno.registrar_falta("Matemática")
        assert aluno.faltas["Matemática"] == 1

    def test_calcular_frequencia(self):
        """Testa calcula frequência por disciplina"""
        aluno = self.setUp()
        aluno.registrar_falta("Matemática")
        frequencia = aluno.calcular_frequencia("Matemática", 10)
        assert frequencia == 90.0
    