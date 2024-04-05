import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hillelDjango3.settings')


app = Celery('hillelDjango3')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
