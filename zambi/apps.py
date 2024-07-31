"""
Módulo que fornece a configuração do aplicativo Zambi.

Este módulo define a configuração para o aplicativo Django `zambi`,
incluindo o campo de chave primária padrão.
"""


from django.apps import AppConfig


class ZambiConfig(AppConfig):
    """
    Configuração para o aplicativo Django `zambi`.

    Esta classe define a configuração específica para o aplicativo `zambi`,
    incluindo o campo de chave primária padrão que será usado em modelos do
    Django.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zambi'
