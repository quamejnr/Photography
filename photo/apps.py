from django.apps import AppConfig


class PhotoConfig(AppConfig):
    name = 'photo'

    def ready(self):
        import user.signals
