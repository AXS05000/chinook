from django.db import models


class Informacao(models.Model):
    nome = models.CharField(max_length=100)
    persona = models.CharField(max_length=100)
    data_resposta = models.DateField()
    unidade = models.CharField(max_length=100)
    questao = models.TextField()
    resposta = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.persona}): {self.questao[:50]}"


class APIKey(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

    def __str__(self):
        return self.name


########################################################################################################


class Beneficio(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Informações sobre Benefícios"


class FolhaPonto(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Informações sobre Folha de Ponto"


class Salario(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Informações sobre Salário"


class Ferias(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Informações sobre Férias"
