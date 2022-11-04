from django.contrib.auth import get_user_model
from profiles.models import Profile, ProfileStatus
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance.username, "__Created", created)
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_first_profile_message(sender, instance, created, **kwargs):
    if created:
        ProfileStatus.objects.create(
            user_profile=instance,
            status_massage=f"{instance.user.username} joined the club"
        )
