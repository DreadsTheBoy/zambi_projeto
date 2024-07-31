"""
Configuração de URL para o projeto_zambi.

A lista urlpatterns mapeia URLs para as visualizações. Para mais informações,
consulte: https://docs.djangoproject.com/en/5.0/topics/http/urls/
Exemplos:
Visualizações baseadas em funções
1. Adicione um import: from my_app import views
2. Adicione uma URL aos urlpatterns: path('', views.home, name='home')
Visualizações baseadas em classes
1. Adicione um import: from other_app.views import Home
2. Adicione uma URL aos urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
1. Importe a função include(): from django.urls import include, path
2. Adicione uma URL aos urlpatterns: path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


# Http Request
def home(request):
    """Function printing python version."""
    request = 'Home'
    return HttpResponse(request)
    # return http Response


# Http Request
def sobre(request):
    """Function printing python version."""
    request = 'Sobre'
    return HttpResponse(request)
    # return http Response


# Http Request
def contato(request):
    """Function printing python version."""
    request = 'Contato'
    return HttpResponse(request)
    # return http Response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre
    path('contato/', contato),  # /contato
]
