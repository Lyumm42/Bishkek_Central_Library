from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rental, ActionHistory


@receiver(post_save, sender=Rental)
def log_rental_action(sender, instance, created, **kwargs):
    action = 'Книга арендована' if created else 'Книга возвращена'
    ActionHistory.objects.create(
        user=instance.user,
        action=f'{action}: {instance.book.title}'
    )
