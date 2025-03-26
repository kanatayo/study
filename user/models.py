from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class CustomerUser(AbstractUser):
    img = models.ImageField(default='default.jpg', verbose_name='头像')
    video = models.ManyToManyField('video.Video', blank=True, related_name='user', verbose_name='观看过')
