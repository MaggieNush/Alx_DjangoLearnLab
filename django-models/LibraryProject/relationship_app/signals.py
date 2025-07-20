from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Check if profile already exists
        if not UserProfile.objects.filter(user=instance).exists():
            UserProfile.objects.create(user=instance, role='Member')