"""
Configuração de URLs para o aplicativo Django `zambi`.

Este módulo define as rotas de URL para o aplicativo `zambi`,
mapeando URLs para suas respectivas visualizações.
"""

from django.urls import path
from zambi.views import home

urlpatterns = [
    path('', home),  # Página inicial
]
