from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    # to register the signals created in signals.py file
    def ready(self):
        import users.signals