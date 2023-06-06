from django.db import models


class Grupo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.BooleanField(default=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome