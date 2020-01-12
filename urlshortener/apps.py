from django.apps import AppConfig


class UrlshortenerConfig(AppConfig):
    name = 'urlshortener'

    def ready(self):
        from . import signals


