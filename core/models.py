from django.db import models

# Create your models here.


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField("nome", max_length=50)
    nota = models.DecimalField("nota", max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'tb_aluno'

    def _str_(self):
        return self.nome
    

class Professor(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField("nome", max_length=50)

    class Meta:
        managed = True
        db_table = 'tb_professor'

    def _str_(self):
        return self.nome


class Disciplina(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField("nome", max_length=50)

    class Meta:
        managed = True
        db_table = 'tb_disciplina'

    def _str_(self):
        return self.nome


class Turma(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField("nome", max_length=50)
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    descricao = models.CharField("descricao", max_length=200)

    class Meta:
        managed = True
        db_table = 'tb_turma'