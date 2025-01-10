from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from app.organizations.models import Organization
from app.tasks.models import Tasks


@receiver(pre_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    Tasks.objects.filter(user=instance).delete()
    Organization.objects.filter(owner=instance).delete()
