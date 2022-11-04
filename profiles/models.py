from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    picture = models.ImageField(
        blank=True, null=True, upload_to='Profile_Picture/%Y/%m/')
    # height_field = None, width_field = None, max_length = None

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profiles'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:
            img = Image.open(self.picture.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.picture.path)


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_massage = models.CharField(max_length=240)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_profile)

    class Meta:
        verbose_name_plural = "ProfileStatus'"
