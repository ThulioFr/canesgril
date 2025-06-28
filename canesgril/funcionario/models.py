from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __srt__(self):
        return self.nome