from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'API'

    def ready(self):
        import API.signals
