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

    def tipo_resposta(self):
        if (
            self.questao
            == "Em uma escala de 0 a 10, o quanto você recomendaria a escola para um amigo ou familiar?"
        ):
            if self.resposta >= 1 and self.resposta <= 6:
                return "Detrator"
            elif self.resposta >= 7 and self.resposta <= 8:
                return "Neutro"
            elif self.resposta >= 9 and self.resposta <= 10:
                return "Promotor"
        else:
            if self.resposta >= 1 and self.resposta <= 2:
                return "Negativo"
            elif self.resposta == 3:
                return "Neutro"
            elif self.resposta >= 4 and self.resposta <= 5:
                return "Positivo"
        return "N/A"
