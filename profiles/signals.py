from django.contrib.auth import get_user_model
from profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance.username, "__Created", created)
    if created:
        Profile.objects.create(user=instance)
