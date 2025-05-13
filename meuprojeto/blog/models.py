from django.db import models

class Post(models.Model):
    titulo= models.CharField(max_length=200)
    descricao = models.TextField()
    capa = models.ImageField(upload_to='capas/',blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo