from django.db import models
from django.urls import reverse
# Create your models here.
class Fornecedor(models.Model):
    CNPJ = models.CharField(max_length=18)
    nome = models.CharField(max_length=100)
    is_ativo = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('fornecedor:detail',kwargs ={'pk':self.pk})

    def __str__(self):
        return self.nome

class Produto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome