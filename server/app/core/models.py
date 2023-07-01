from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=5000, blank=True)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo