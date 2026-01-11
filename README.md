# 🏥 VITTA – Sistema de Atendimento em Saúde

O **VITTA** é um sistema web desenvolvido com **Python e Django**, voltado para a **gestão de atendimentos em saúde**, aplicável a 
**hospitais, clínicas, ambulatórios e unidades básicas de saúde (UBS)**.

O sistema tem como objetivo **centralizar e organizar informações essenciais do atendimento ao paciente**, oferecendo uma interface simples, 
funcional e de fácil manutenção, focada em rotinas administrativas e clínicas do dia a dia.

Entre as principais funcionalidades estão:

- Cadastro e gerenciamento de pacientes
- Agendamento e controle de consultas
- Registro de anotações clínicas (prontuário)
- Histórico de atendimentos
- Controle de acesso por usuários

Este projeto foi desenvolvido com fins **educacionais e demonstrativos**, servindo como **portfólio prático** para estudo de desenvolvimento web, 
modelagem de dados, automação de rotinas e manutenção de sistemas, especialmente no contexto da área da saúde.

---

## 🎯 Objetivo do Projeto

Criar uma plataforma que permita:

- Centralizar **dados clínicos e administrativos** de pacientes
- Registrar **anotações de atendimentos**
- Organizar **agendamentos de consultas**
- Facilitar a comunicação entre empresa, profissionais e pacientes
- Garantir **segurança da informação** e conformidade com a LGPD

---

## 🧠 Problema que o Sistema Resolve

Empresas de Home Care costumam enfrentar:

- Anotações descentralizadas (papel, WhatsApp, planilhas)
- Falta de histórico organizado do paciente
- Dificuldade no controle de agendas
- Risco de perda de informações sensíveis

O **Vitta** surge para **organizar, registrar e proteger** esses dados em um único sistema.

---

## 🏗️ Arquitetura do Sistema

O sistema será estruturado seguindo boas práticas do Django:

- Arquitetura **MVC (Model–View–Template)**
- Separação por apps
- Uso de autenticação e permissões
- Banco de dados relacional

### Apps planejados:

- `consultas` – Agendamentos e remarcações
- `pacientes` – Cadastro e histórico do paciente
- `prontuarios` – Profissionais da saúde

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **Django**
- **HTML5**
- **CSS3**
- **Bootstrap** (frontend)
- **SQLite** (desenvolvimento)
- **PostgreSQL** (produção – planejado)
- **Git / GitHub**

---

## 🧑‍⚕️ Funcionalidades Planejadas

### Institucional

- Página inicial
- Serviços oferecidos
- Sobre a empresa
- Contato

### Sistema

- Cadastro de pacientes
- Cadastro de profissionais
- Agendamento de atendimentos
- Registro de evolução clínica
- Histórico completo do paciente
- Controle de usuários e permissões

---

## 🔐 Segurança e LGPD

- Autenticação por usuário
- Controle de permissões por perfil
- Proteção de dados sensíveis
- Acesso restrito a informações clínicas
- Planejamento de adequação à **LGPD**

---

## Como configurar o projeto localmente (Linux Ubuntu)

Siga os passos abaixo para replicar corretamente o ambiente de desenvolvimento.

---

### 1️⃣ Pré-requisitos

Certifique-se de ter instalado:

- Python 3.10+
- pip
- virtualenv (opcional, mas recomendado)
- Git

Verifique:

```bash
python3 --version
pip --version
git --version

```

---

### 2️⃣ Criando e ativando o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate

```

---

### 3️⃣ Instalando o Django

Como o projeto é criado do zero, instale o Django antes:

```bash
pip install django
django-admin --version

```

---

### 4️⃣ Criando o projeto Django

```bash
django-admin startproject vitta
cd vitta

```

Estrutura inicial:

```
vitta/
├── manage.py
├── vitta/

```

---

### 5️⃣ Criando os aplicativos do sistema

```bash
python manage.py startapp pacientes
python manage.py startapp consultas
python manage.py startapp prontuarios

```

---

### 6️⃣ Registrando os aplicativos no settings.py

Arquivo:

```
vitta/settings.py

```

Adicionar:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pacientes',
    'consultas',
    'prontuarios',
]

```

---

### 7️⃣ Configurando arquivos estáticos (CSS, JS, imagens)

Criar a pasta na raiz (nível do `manage.py`):

```bash
mkdir static
mkdir static/css static/js static/img

```

No `settings.py`:

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

```

⚠️ Não é necessário configurar `STATICFILES_FINDERS`.

---

### 8️⃣ Configurando templates (HTML)

Criar pasta:

```bash
mkdir templates

```

No `settings.py`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

---

### 9️⃣ Configurando URLs do projeto

Arquivo:

```
vitta/urls.py

```

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),
]

```

---

### 🔟 Configurando URLs e Views do app (exemplo: pacientes)

### Criar o arquivo:

```
pacientes/urls.py

```

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pacientes_index'),
]

```

### Criar a view:

```
pacientes/views.py

```

```python
from django.shortcuts import render

def index(request):
    return render(request, 'pacientes/index.html')

```

---

### 1️⃣1️⃣ Criando templates do app

```bash
mkdir -p templates/pacientes

```

Arquivo:

```
templates/pacientes/index.html

```

```html
{% extends 'base.html' %}

{% block content %}
<h1>Pacientes</h1>
<p>Gerenciamento de pacientes.</p>
{% endblock %}

```

---

### 1️⃣2️⃣ Criando o template base

```
templates/base.html

```

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>VITTA</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<header>
    <h1>VITTA – Sistema de Atendimento em Saúde</h1>
</header>

<main>
    {% block content %}{% endblock %}
</main>

</body>
</html>

```

---

## 🗄️ Banco de dados e migrações

### 1️⃣3️⃣ Migrações iniciais do Django

⚠️ **Neste momento ainda NÃO existem models próprios.**

Execute apenas:

```bash
python manage.py migrate

```

Isso irá:

- criar o arquivo `db.sqlite3`
- criar tabelas internas do Django
- preparar o admin

---

### 1️⃣4️⃣ Criando superusuário

```bash
python manage.py createsuperuser

```

---

### 1️⃣5️⃣ Criando models (exemplo)

```
pacientes/models.py

```

```python
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome

```

---

### 1️⃣6️⃣ Migrações dos models

⚠️ **Este é o momento correto de usar `makemigrations`.**

```bash
python manage.py makemigrations
python manage.py migrate

```

---

### 1️⃣7️⃣ Registrando models no admin

```
pacientes/admin.py

```

```python
from django.contrib import admin
from .models import Paciente

admin.site.register(Paciente)

```

Acesse:

```
http://127.0.0.1:8000/admin/

```

---

### 1️⃣8️⃣ Executando o servidor

```bash
python manage.py runserver

```

Acesse:

```
http://127.0.0.1:8000/

```

---

## Observações importantes

- O arquivo `db.sqlite3` **não deve ser versionado**
- Adicione ao `.gitignore`:

```
db.sqlite3
venv/

```

- Projeto voltado para fins educacionais

---

## ✅ Conclusão

Este README reflete **exatamente a ordem correta de criação de um projeto Django do zero**, evitando erros comuns com migrações, banco de dados, settings e estrutura do sistema. Pode ser evoluído futuramente com:

- PostgreSQL
- Controle de permissões
- Relatórios
- Auditoria

---

## 👤 Autor

**Robinson Dias**

Desenvolvedor em formação

Projeto que integra **saúde, cuidado e tecnologia**

---
