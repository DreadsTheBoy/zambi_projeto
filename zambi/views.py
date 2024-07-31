"""
Módulo que fornece visualizações para o aplicativo Django.

Este módulo define as funções de visualização para o aplicativo Django
"""


# from django.shortcuts import render
from django.http import HttpResponse


# Http Request
def home(request):
    """Function printing python version."""
    request = 'Home'
    return HttpResponse(request)
    # return http Response


# Http Request
def contato(request):
    """Function printing python version."""
    request = 'Contato'
    return HttpResponse(request)
    # return http Response


# Http Request
def sobre(request):
    """Function printing python version."""
    request = 'Sobre'
    return HttpResponse(request)
    # return http Response
