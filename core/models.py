from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    profile_pic = ResizedImageField(size=[1080, 1080], quality=95, crop=['middle', 'center'],
                                    upload_to="customer_images/", default='default.webp')
    locaiton = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username


class OrganizationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=100)
    website = models.URLField(null=True, blank=True)
    locaiton = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username
