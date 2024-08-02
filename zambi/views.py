"""
Módulo que fornece visualizações para o aplicativo Django.

Este módulo define as funções de visualização para o aplicativo Django
"""


from django.shortcuts import render


def home(request):
    """
    Exibe a página inicial do site.

    Esta função processa uma solicitação HTTP e retorna a resposta com
    o conteúdo do template 'home.html'.
    """
    return render(request, 'zambi/pages/home.html')

