from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Bem(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    data_aquisicao = models.DateField()
    status = models.CharField(max_length=50, choices=[('Em uso', 'Em uso'), ('Manutenção', 'Manutenção'), ('Baixado', 'Baixado')])
    usuario_responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Adicionando valor do bem
    
    def __str__(self):
        return self.nome

class Movimentacao(models.Model):
    bem = models.ForeignKey(Bem, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    destino = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descricao = models.TextField()
    
    def __str__(self):
        return f'{self.bem} - {self.destino} ({self.data})'