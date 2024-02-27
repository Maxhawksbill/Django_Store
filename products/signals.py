from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import order_send_telegram_message, order_daily_statistics

from .models import Order
from django_celery_results.models import TaskResult

@receiver(post_save, sender=Order)
def send_order_telegram_message(sender, instance: Order, created, **kwargs):
    if created:
        order_send_telegram_message.apply_async((instance.uuid,), countdown=10)
        print('Sending telegram message')

# @receiver(post_save, sender=TaskResult)
# def send_order_daily_statistics(sender, instance: TaskResult, created, **kwargs):
#     if instance.periodic_task_name == 'daily_statistics' and created:
#         # order_daily_statistics.apply_async((instance.periodic_task_name,), countdown=10)
#         order_daily_statistics.delay(instance)
#         print('Sending daily statistics')
