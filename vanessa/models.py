from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.EmailField()
    genero = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return('{}\n{}\n{}\n{}'.format(self.nome, self.email, self.genero, self.idade))