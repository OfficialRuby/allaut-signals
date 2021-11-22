from django.apps import AppConfig


class ActionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'action'

    def ready(self):
        import action.signals
