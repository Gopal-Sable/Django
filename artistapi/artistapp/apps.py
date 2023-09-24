
from django.apps import AppConfig

class ArtistappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artistapp'

    def ready(self):
        import artistapp.signals
