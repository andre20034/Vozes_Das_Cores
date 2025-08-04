# core/admin.py
from django.contrib import admin
from .models import Mensagem # Importa o modelo Mensagem

# Esta classe customiza como as mensagens são exibidas no painel de admin
class MensagemAdmin(admin.ModelAdmin):
    # Mostra estas colunas na lista de mensagens
    list_display = ('nome_exibicao', 'autor', 'texto', 'data_criacao')
    # Adiciona um filtro por data na lateral direita
    list_filter = ('data_criacao',)
    # Adiciona uma barra de busca que procura nos campos de texto e nome
    search_fields = ('texto', 'nome_exibicao')
    # Define uma ordem padrão
    ordering = ('-data_criacao',)

# Registra o modelo Mensagem para que ele apareça no admin, usando a customização acima
admin.site.register(Mensagem, MensagemAdmin)