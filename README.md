Markdown


# Projeto Janeiro Branco


Este projeto é uma aplicação web completa desenvolvida em apoio à campanha **Janeiro Branco**, Um mês para refletir, cuidar da mente e promover o bem-estar emocional, construindo uma sociedade mais saudável e feliz. A plataforma busca ser um canal de informação e, ao mesmo tempo, um espaço seguro e acolhedor para que pessoas possam deixar mensagens de apoio e solidariedade de forma anônima.

## 📜 Sobre a Campanha

A campanha "Janeiro Branco" é um movimento dedicado à conscientização sobre a importância da saúde mental e emocional. Ela busca prevenir doenças como ansiedade, depressão e pânico, que podem ser causadas pelo estresse, além de abordar outros transtornos de humor como esquizofrenia e transtorno bipolar.**Atendimento psicológico do HUB (Hospital Universitário de Brasília): Contato: (61) 3340-2314.** ou **Centro Universitário UDF: Oferece atendimento psicológico. Agendamento: (61) 3225-7724 / 99983-7555.**

## ✨ Funcionalidades

O projeto conta com as seguintes funcionalidades:

* **Página Informativa:** Uma página inicial que apresenta a campanha, explica a importância da saúde Mental, mostrar a força da mente sobre o corpo.
* **Diario anônimo de progresso:** Compartilhe anonimamente seu progresso na luta contra os aspectos negativos da vida e incentive outras pessoas.
* **Formulário de Envio:** Um formulário simples e seguro para que qualquer pessoa possa ver sem saber quem é vc.

## 💻 Tecnologias Utilizadas

A aplicação foi construída utilizando um conjunto de tecnologias modernas, separando as responsabilidades entre o front-end, o back-end e o banco de dados.

* **Front-end (Interface do Usuário):**
    * `HTML5`: Para a estruturação semântica do conteúdo.
    * `CSS3`: Para a estilização, layout e design responsivo, seguindo a identidade visual do Agosto Lilás.
    * `JavaScript`: Para a interatividade e o carregamento dinâmico das mensagens no mural, consumindo a API do back-end.

* **Back-end (Lógica do Servidor):**
    * `Python 3`: Linguagem principal para toda a lógica da aplicação.
    * `Flask`: Um micro-framework leve e poderoso para criar o servidor web, gerenciar as rotas e a API.
    * `Django`:...

* **Banco de Dados:**
    * `SQLite 3`: Um banco de dados relacional baseado em arquivo, ideal para projetos de pequeno e médio porte pela sua simplicidade e por não necessitar de um servidor dedicado.

## 🚀 Como Executar o Projeto Localmente
Guia Completo: Transformando seu Site HTML, CSS e JavaScript em um Projeto Django
Olá! Este guia foi criado para ajudar você a migrar seu projeto web estático (HTML, CSS e JavaScript) para o framework Django. Django é uma ferramenta poderosa e segura, escrita em Python, ideal para construir aplicações web complexas, especialmente aquelas que interagem com um banco de dados, como o seu "Diário da Comunidade".

Vamos seguir passo a passo. Explicarei cada comando e o porquê de cada etapa para garantir que você compreenda todo o processo.

Passo 1: Preparando o Ambiente
Antes de tudo, precisamos garantir que você tenha o Python e o Django instalados. Também vamos criar um ambiente virtual, que é uma boa prática para isolar as dependências do nosso projeto, evitando conflitos com outras instalações de Python.

Instale o Python: Se você ainda não tem o Python, baixe e instale a versão mais recente em python.org.

Crie a Pasta do Projeto:
No seu computador, crie uma pasta para o projeto. Vamos chamá-la de vozesdascores_project.

Crie e Ative o Ambiente Virtual:
Abra seu terminal ou prompt de comando, navegue até a pasta que você criou (vozesdascores_project) e execute os seguintes comandos:

Bash

# Cria um ambiente virtual chamado 'venv'
python -m venv venv

# Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

# Ativa o ambiente virtual (macOS/Linux)
source venv/bin/activate
Você saberá que funcionou porque o nome (venv) aparecerá no início da linha do seu terminal.

Instale o Django:
Com o ambiente virtual ativo, instale o Django com este comando:
```
Bash: pip install django
```

Passo 2: Criando o Projeto Django
Agora, vamos criar a estrutura básica do projeto Django.

Crie o Projeto:
Ainda no terminal, dentro da pasta vozesdascores_project e com o (venv) ativo, execute:
```
Bash : django-admin startproject config . 
```
startproject é o comando para criar um projeto.

config será o nome da nossa pasta de configurações.

O  ( . ponto) no final significa para criar o projeto na pasta atual, evitando uma subpasta desnecessária.

Sua estrutura de pastas agora deve ser:
```
vozesdascores_project/
├── venv/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py  <-- Configurações do projeto
│   ├── urls.py      <-- Rotas principais do projeto
│   └── wsgi.py
└── manage.py        <-- Seu assistente para comandos Django
```
Passo 3: Criando a "App" do Diário
No Django, um projeto é dividido em "apps". Cada app cuida de uma funcionalidade específica. Vamos criar um app para cuidar do nosso site principal e do diário.

Crie o App:
Execute o comando:
```
Bash: python manage.py startapp core
```

Isso criará uma nova pasta core com vários arquivos para a lógica da nossa aplicação.

Registre o App:
Agora, precisamos dizer ao Django que ele deve usar nosso novo app. Abra o arquivo config/settings.py e adicione 'core' à lista INSTALLED_APPS:

Python

# config/settings.py
```
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$wgg2dvw0egpli)&1!c1ed8f9kinb)0(+p_zxleb)lraignt(&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ... no final do arquivo ...

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Para onde redirecionar após o login
LOGIN_REDIRECT_URL = '/'

# Para onde redirecionar se o usuário não estiver logado
# (essa é a URL da nossa página de login)
LOGIN_URL = '/accounts/login/'

# Para onde redirecionar após o logout
LOGOUT_REDIRECT_URL = '/accounts/login/'
```
Passo 4: Definindo o Modelo de Dados (O Diário)
Vamos definir como uma mensagem do diário será salva no banco de dados.

Edite o models.py:
Abra o arquivo core/models.py e adicione o seguinte código:

Python
```
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
```
Crie e Aplique as Migrações:
Agora, vamos traduzir esse modelo Python para uma tabela no banco de dados.

# Cria o arquivo de migração
```
python manage.py makemigrations
```
# Aplica a migração ao banco de dados
```
python manage.py migrate
```
Passo 5: Criando a Lógica (Views)
A "view" é a função que é executada quando um usuário acessa uma URL. Ela busca dados, processa informações de formulários e renderiza o HTML.

Edite o views.py:
Abra o arquivo core/views.py e substitua o conteúdo por:

Python

# core/views.py
```
# core/views.py
from django.shortcuts import render, redirect
from .models import Mensagem
# Garanta que estas duas linhas foram importadas:
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

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
```
Passo 6: Configurando as Rotas (URLs)
Precisamos mapear uma URL (como www.meusite.com/) para a view que acabamos de criar.

Crie um arquivo urls.py no app core:
Dentro da pasta core, crie um novo arquivo chamado urls.py e adicione:

Python
```
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('signup/', views.signup, name='signup'), 
]
```
Inclua as URLs do App no Projeto Principal:
Agora, modifique o arquivo config/urls.py para que ele "enxergue" as URLs do nosso app core.

Python

# config/urls.py
```
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ADICIONE ESTA LINHA:
    # Ela ativa as URLs de autenticação do Django.
    # Todas começarão com 'contas/' (ex: /contas/login/, /contas/logout/)
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
]
```
Passo 7: Configurando os Arquivos Estáticos (CSS, Imagens, Vídeos) e Templates (HTML)
Esta é a etapa crucial para garantir que seus arquivos CSS, imagens e vídeos sejam carregados corretamente.

Crie a Estrutura de Pastas Correta:
Na raiz do seu projeto (vozesdascores_project), crie a pasta static. Dentro dela, crie subpastas para cada tipo de arquivo: css, images, videos.
Crie também a pasta templates na raiz do projeto.
```
vozesdascores_project/
├── static/
│   ├── css/
│   │   └── style.css        <-- SEU ARQUIVO CSS AQUI
|        └── stylelogin.css <-- CSS do login e singup
├── templates/         <-- SEU ARQUIVO HTML AQUI
│   └── index.html
├── registretion
|     └── login.html
|     └── singup.html           
└── ... (outras pastas do projeto Django)
```
Ação: Mova seus arquivos style.css, imagem.png e video.mp4 para as pastas correspondentes acima. Mova também seu arquivo HTML (index.html) para a pasta templates.

Configure o settings.py:
Abra config/settings.py e informe ao Django onde encontrar essas pastas. Garanta que import os esteja no topo do arquivo. Em seguida, adicione/modifique estas linhas:

Python

# config/settings.py
import os # Garanta que 'os' está importado no topo do arquivo

# ... (outras configurações) ...
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Informa onde estão os templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
# ... (no final do arquivo add estas linhas) ...
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # Informa onde está a pasta 'static'
]
```
Atualize o Template HTML (index.html):
Agora vamos corrigir o HTML para que ele use a tag {% static %} para todos os arquivos. Isso permite que o Django encontre o caminho correto para eles.

HTML
```
{% load static %} <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vozes das Cores - Janeiro Branco</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

    <section id="novo-topico-1" class="new-topic">
        <h2>Caso 1</h2>
        <div class="images-wrapper">
            <div class="video-item">
                <video width="100%" height="auto" controls>
                    <source src="{% static 'videos/mulher_curada.mp4' %}" type="video/mp4">
                    Seu navegador não suporta a tag de vídeo.
                </video>
                </div>
        </div>
    </section>

    <section id="novo-topico-2" class="new-topic">
        <h2>Caso 2</h2>
        <div class="images-wrapper">
            <div class="image-item">
                <img src="{% static 'images/levanta-carro.png' %}" alt="Mãe levantando carro para salvar filho">
                </div>
        </div>
    </section>

    <section id="diario">
        <h2>Diário da Comunidade</h2>
        <p>Compartilhe seus pensamentos, sentimentos ou uma mensagem de apoio. Este é um espaço seguro para todos.</p>

        <form method="POST" action="{% url 'pagina_principal' %}">
            {% csrf_token %}
            <textarea name="mensagem" placeholder="Escreva sua mensagem aqui..." required rows="4"></textarea>
            <button type="submit">Enviar Mensagem</button>
        </form>

        <h3>Mensagens:</h3>
        <div id="mensagens-container">
            {% for mensagem in mensagens %}
                <div class="mensagem-item">
                    <p>{{ mensagem.texto }}</p>
                    <small style="color: #777; font-size: 0.8em;">Em {{ mensagem.data_criacao|date:"d/m/Y H:i" }}</small>
                </div>
            {% empty %}
                <p>Nenhuma mensagem ainda. Seja o primeiro a compartilhar!</p>
            {% endfor %}
        </div>
    </section>

    </body>
</html>
```
Principais mudanças:

Baixe a extençao "Djangle" e "Django Template" nos apps do vscode

Adicionamos {% load static %} no início do arquivo.

Substituímos o <iframe> por uma tag <video>, que é a forma correta de exibir um arquivo de vídeo local. O src agora usa {% static 'pasta_do_video/video.mp4' %}.

A tag <img> para a imagem do carro agora usa src="{% static 'pasta_de_images/imagem.png' %}".

Implementamos o formulário do diário usando a tag {% csrf_token %} (essencial para segurança no Django) e {% url 'pagina_principal' %} para a ação do formulário.

Adicionamos a lógica para exibir as mensagens do diário usando um loop {% for ... %} e {% empty %} para quando não houver mensagens.

Passo 8: Rodando o Servidor
Agora que tudo está configurado corretamente, vamos rodar o servidor. O erro "Conexão recusada" geralmente significa que o servidor não está rodando ou você está tentando acessar o endereço errado.

Inicie o Servidor de Desenvolvimento:
No terminal (com o ambiente virtual (venv) ativo), execute:
```
Bash: python manage.py runserver
```

Se houver algum erro no seu código, ele aparecerá no terminal agora. Se tudo estiver certo, você verá algo como Starting development server at http://127.0.0.1:8000/.

Acesse o Site:
Abra seu navegador e acesse http://127.0.0.1:8000/.  adicione "admin" (para entrar na pagina de adimministrador); "login" (pagina de logins)


```
+------------------+                   +------------------+
|                  |                   |                  |
|       VIEW       |<------------------|     CONTROLLER   |
| (Templates HTML, |  3. Renderiza     | (app.py: Rotas,  |
|  CSS,)           |     View          |  Lógica de Fluxo) |
|                  |                   |                  |
+------------------+                   +--------^---------+
         ^                                      |
         |                                      | 1. Requisição do Usuário
         |                                      | (e.g., Clicar em botão,
         |                                      | Enviar formulário)
         |                                      |
         |                                      | 2. Interage com
         |                                      |
+------------------+                   +--------+---------+
|                  |                   |                  |
|   Usuário/Cliente|<----------------->|      MODEL       |
| (Navegador Web)  |                   | (models.py: Dados,|
|                  |                   |  Lógica de Negócios) |
+------------------+                   |                  |
                                       +------------------+
                                                ^
                                                |
                                                | 4. Persistência
                                                |    (Leitura/Escrita)
                                                |
                                       +------------------+
                                       |                  |
                                       |   BANCO DE DADOS |
                                       |    (mensagens.db)  |
                                       |                  |
                                       +------------------+

```


Passo 9: Atualizando o Modelo de Dados para Associar Mensagens a Usuários
Nosso primeiro objetivo é modificar a estrutura da tabela Mensagem no banco de dados para que ela possa "lembrar" qual usuário escreveu cada postagem, ou se foi uma postagem anônima.

Abra o arquivo core/models.py:
Este arquivo define a estrutura de todas as "tabelas" da sua aplicação core.

Importe o modelo User:
O Django já vem com um sistema de usuários completo. Precisamos apenas importar o modelo User para podermos nos referir a ele. Adicione a linha from django.contrib.auth.models import User no topo do arquivo.

Modifique a classe Mensagem:

autor: Adicionaremos um campo chamado autor. Ele será uma ForeignKey (chave estrangeira), que é a forma como o Django cria uma relação entre dois modelos. Ele ligará cada Mensagem a um User.

on_delete=models.CASCADE: Isso diz ao banco de dados: "Se um usuário for excluído, exclua também todas as mensagens que ele escreveu".

null=True, blank=True: Estas duas opções são cruciais. Elas permitem que o campo autor no banco de dados fique vazio. É assim que representaremos uma mensagem anônima.

nome_exibicao: Adicionaremos um campo de texto simples para guardar o nome que será exibido na postagem. Se o usuário estiver logado, guardaremos seu nome de usuário aqui. Se for anônimo, guardaremos a palavra "Anônimo".

Seu arquivo core/models.py deve ficar exatamente assim:

Python
```
# core/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # <-- ADICIONE ESTA LINHA

class Mensagem(models.Model):
    # --- INÍCIO DAS MODIFICAÇÕES ---
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_exibicao = models.CharField(max_length=100)
    # --- FIM DAS MODIFICAÇÕES ---

    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # Vamos melhorar a representação do objeto no admin
        return f'Mensagem de {self.nome_exibicao} em {self.data_criacao.strftime("%d/%m/%Y")}'
```

Crie e Aplique as Migrações:
Agora que descrevemos as mudanças no código Python, precisamos traduzir isso em comandos para o banco de dados.
Abra seu terminal (com o ambiente (venv) ativo) e execute os seguintes comandos, um após o outro:

# Este comando lê o seu models.py e cria um novo arquivo de migração com as alterações
```
Bash: python manage.py makemigrations
```
# Este comando aplica o arquivo de migração, alterando de fato o seu banco de dados
```
Bash: python manage.py migrate
```

Resultado: Seu banco de dados agora tem a tabela de mensagens com os novos campos autor_id e nome_exibicao.

Passo 10: Configurando as Páginas de Login, Logout e Cadastro
O Django é incrível porque já nos dá a maior parte da lógica de autenticação pronta. Nós só precisamos criar os arquivos HTML e dizer ao Django onde encontrá-los.

Configure as URLs de Autenticação:
Primeiro, vamos dizer ao nosso projeto principal para usar as URLs de autenticação que o Django oferece (para login, logout, troca de senha, etc.).
Abra o arquivo config/urls.py e modifique-o:

Python
```
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ADICIONE ESTA LINHA:
    # Ela ativa as URLs de autenticação do Django.
    # Todas começarão com 'contas/' (ex: /contas/login/, /contas/logout/)
    path('contas/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
]
```
Crie o Template de Login:
Por padrão, a URL /contas/login/ que acabamos de ativar vai procurar por um template em templates/registration/login.html. Vamos criá-lo.

Dentro da pasta templates, crie uma nova pasta chamada registration.

Dentro de templates/registration, crie um arquivo chamado login.html.

A estrutura de pastas ficará assim:
```
vozesdascores_project/
|-- templates/
|   |-- registration/
|   |   `-- login.html      <-- CRIE ESTE ARQUIVO
|   `-- index.html
`-- ...
```
Adicione o seguinte código ao arquivo templates/registration/login.html:

HTML
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    </head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %} {{ form.as_p }}  <button type="submit">Entrar</button>
    </form>
    <p>Ainda não tem uma conta? <a href="{% url 'signup' %}">Cadastre-se aqui!</a></p>
</body>
</html>
```
Crie a Página de Cadastro (Sign Up):
Para o cadastro, precisamos de 3 coisas: uma URL, uma View (lógica) e um Template (HTML).

a) Crie a View de Cadastro:
A "view" é a função Python que vai processar o formulário de cadastro.
Abra core/views.py e adicione o seguinte código:

Python
```
# core/views.py
from django.shortcuts import render, redirect
from .models import Mensagem
# Importe o formulário de criação de usuário e a função de login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# ...sua view 'pagina_principal' continua aqui...

# ADICIONE ESTA NOVA FUNÇÃO (VIEW)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário no banco de dados
            login(request, user)  # Loga o usuário automaticamente
            return redirect('pagina_principal')  # Redireciona para a página inicial
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
```
b) Crie a URL para o Cadastro:
Abra core/urls.py e adicione o caminho para a nova view signup:

Python
```
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('signup/', views.signup, name='signup'), # <-- ADICIONE ESTA LINHA
]
```
c) Crie o Template de Cadastro:
Dentro da pasta templates/registration, crie um novo arquivo chamado signup.html.
Adicione o seguinte código a templates/registration/signup.html:

HTML
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastro</title>
</head>
<body>
    <h2>Crie sua Conta</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }} <button type="submit">Cadastrar</button>
    </form>
</body>
</html>
```
Passo 11: Integrando a Autenticação na Página Principal
Agora vamos fazer a mágica acontecer na página inicial: mostrar links de login/logout, permitir postagens anônimas e exibir o autor de cada mensagem.

Atualize a View pagina_principal:
Vamos alterar a lógica de salvamento de mensagens.
Abra core/views.py e substitua TODA a função pagina_principal pela versão abaixo:

Python
```
# core/views.py
def pagina_principal(request):
    if request.method == 'POST':
        texto_da_mensagem = request.POST.get('mensagem')
        # Verifica se a caixa "Postar como anônimo" foi marcada
        eh_anonimo = request.POST.get('anonimo')

        if texto_da_mensagem:
            # Se o usuário está logado E a caixa de anônimo NÃO foi marcada
            if request.user.is_authenticated and not eh_anonimo:
                Mensagem.objects.create(
                    autor=request.user,
                    nome_exibicao=request.user.username,
                    texto=texto_da_mensagem
                )
            # Para todos os outros casos (usuário deslogado OU marcou anônimo)
            else:
                Mensagem.objects.create(
                    nome_exibicao="Anônimo",
                    texto=texto_da_mensagem
                )
        return redirect('pagina_principal')

    mensagens = Mensagem.objects.all().order_by('-data_criacao')
    contexto = {'mensagens': mensagens}
    return render(request, 'index.html', contexto)
```
Atualize o Template index.html:
Esta é a mudança mais visível para o usuário.
Abra o arquivo templates/index.html e faça as seguintes modificações:

a) Adicione os links de Login/Logout no cabeçalho:
Encontre sua tag <header> ou <nav> e adicione o bloco de código abaixo. Ele usa a variável user (que o Django sempre disponibiliza) para verificar se o usuário está logado.

HTML
```
<nav>
    {% if user.is_authenticated %}
        <span>Olá, {{ user.username }}!</span>
        <a href="{% url 'logout' %}">Sair</a>
    {% else %}
        <a href="{% url 'login' %}">Entrar</a>
        <a href="{% url 'signup' %}">Cadastre-se</a>
    {% endif %}
</nav>
```
b) Modifique o Formulário de Mensagens:
Vamos adicionar uma caixa de seleção (checkbox) para a postagem anônima.
Encontre a seção <section id="diario"> e substitua o <form> pelo seguinte:

HTML
```
<form method="POST" action="{% url 'pagina_principal' %}">
    {% csrf_token %}
    <textarea name="mensagem" placeholder="Escreva sua mensagem aqui..." required rows="4"></textarea>

    {% if user.is_authenticated %}
    <div>
        <input type="checkbox" name="anonimo" id="anonimo">
        <label for="anonimo">Postar como anônimo</label>
    </div>
    {% endif %}
    <button type="submit">Enviar Mensagem</button>
</form>
```
c) Modifique a Exibição das Mensagens:
Agora, vamos mostrar o nome_exibicao que salvamos.
Encontre o loop {% for mensagem in mensagens %} e modifique-o para ficar assim:

HTML
```
<div id="mensagens-container">
    {% for mensagem in mensagens %}
        <div class="mensagem-item">
            <p><strong>{{ mensagem.nome_exibicao }}:</strong> {{ mensagem.texto }}</p>
            <small style="color: #777; font-size: 0.8em;">Em {{ mensagem.data_criacao|date:"d/m/Y H:i" }}</small>
        </div>
    {% empty %}
        <p>Nenhuma mensagem ainda. Seja o primeiro a compartilhar!</p>
    {% endfor %}
</div>
```
Passo 12: Configurando o Painel de Administrador (Sua Ferramenta de Moderação)
Esta é a etapa final e mais gratificante. Vamos ativar a interface de administração do Django para que você possa excluir comentários indesejados.

Crie uma Conta de Administrador (Superusuário):
No seu terminal (com o (venv) ativo), execute o comando:
```
Bash: python manage.py createsuperuser
```

O terminal pedirá para você criar um nome de usuário, um e-mail e uma senha. Preencha com atenção, pois estes serão seus dados de acesso ao painel de controle.(Caso apareça opções 1 ou 2 escolha a 1 e digide ('Anonimo') com aspas simples).


Registre o Modelo Mensagem no Painel de Admin:
Precisamos dizer ao Django: "Ei, eu quero gerenciar o modelo Mensagem através do painel de admin".
Abra o arquivo core/admin.py e substitua seu conteúdo por este:

Python
```
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
```
pagina de adm: http://127.0.0.1:8000/admin/


extra - caso de erro no singup faça cole o codigo abaixo : 
```
# core/views.py
from django.shortcuts import render, redirect
from .models import Mensagem
# Garanta que estas duas linhas foram importadas:
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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
```
*Caso esqueça a senha 
```
bash:python manage.py createsuperuser
```
e siga as intruçoes do terminal

# Registra o modelo Mensagem para que ele apareça no admin, usando a customização acima
admin.site.register(Mensagem, MensagemAdmin)

---
## 💻 Banco de dados

1) Mensagens de apoio: Que já existem.

2) Usuários: Pessoas que se cadastram e podem, por exemplo, postar suas próprias mensagens e ter um perfil.

Para isso, precisaríamos de duas tabelas principais: uma para Usuários e outra para Mensagens.
```
+---------------------+       +---------------------------+
|      usuarios       |       |        mensagens          |
+---------------------+       +---------------------------+
| id (PK)             |<----->| id (PK)                   |
| nome_usuario (UNIQUE)|       | texto                     |
| email (UNIQUE)      |       | data_criacao              |
| senha (HASHED)      |       | autor_id (FK -> usuarios) |
| data_cadastro       |       +---------------------------+
| ultimo_login        |
+---------------------+
```
Com essa estrutura, você pode:

1 - Registrar novos usuários.

2 - Permitir que usuários façam login.

3- Associar cada mensagem postada a um usuário específico.

4 -Consultar todas as mensagens de um usuário, ou todas as mensagens e saber quem as postou.

---

Um pequeno Projeto com um grande objetivo para apoiar uma causa importante.

Aluno do TDS (Tecnico Desenvolvimento de Sistema)

Autor: André Rodrigues

GitHub: http://github.com/andre20034

E-mail de contato: andre67192@estudante.ifb.edu.br
