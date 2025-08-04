# core/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Mensagem(models.Model):
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_exibicao = models.CharField(max_length=100)

    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        # Vamos melhorar a representação do objeto no admin
        return f'Mensagem de {self.nome_exibicao} em {self.data_criacao.strftime("%d/%m/%Y")}'
    
    

    


