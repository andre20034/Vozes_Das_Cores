# core/views.py
from django.shortcuts import render, redirect
from .models import Mensagem
# Garanta que estas duas linhas foram importadas:
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def pagina_principal(request):
    if request.method == 'POST':
        texto_da_mensagem = request.POST.get('mensagem')
        eh_anonimo = request.POST.get('anonimo')

        if texto_da_mensagem:
            if request.user.is_authenticated and not eh_anonimo:
                Mensagem.objects.create(
                    autor=request.user,
                    nome_exibicao=request.user.username,
                    texto=texto_da_mensagem
                )
            else:
                Mensagem.objects.create(
                    nome_exibicao="Anônimo",
                    texto=texto_da_mensagem
                )
        return redirect('pagina_principal')

    mensagens = Mensagem.objects.all().order_by('-data_criacao')
    contexto = {'mensagens': mensagens}
    return render(request, 'index.html', contexto)

# ESTA É A FUNÇÃO QUE ESTAVA FALTANDO OU ESTAVA INCORRETA
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pagina_principal')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})