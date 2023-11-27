from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    email = models.EmailField(unique=True)
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
        
class Estoque(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    

class Reclamacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    

class Encomenda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    

class Pedido(models.Model):
    encomenda = models.ForeignKey(Encomenda, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    produto = models.CharField(max_length=100)

