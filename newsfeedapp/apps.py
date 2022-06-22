from django.apps import AppConfig


class NewsfeedappConfig(AppConfig):
    name = 'newsfeedapp'

    def ready(self): 
        import newsfeed.celery