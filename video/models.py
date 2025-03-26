from django.contrib.auth.models import AbstractUser
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from user.models import CustomerUser


# Create your models here.


class Actor(models.Model):
    ActorName = models.CharField(max_length=20)
    # 头像
    avatar = models.ImageField(default='default.png', verbose_name='演员头像')

    def __str__(self):
        return self.ActorName


class Category(models.Model):
    categoryName = models.CharField(max_length=10)

    def __str__(self):
        return self.categoryName


class Video(models.Model):
    videoName = models.CharField(max_length=50)
    actor = models.ManyToManyField(Actor, related_name='video')
    videoDetails = CKEditor5Field(verbose_name="影视详情", config_name='extends')
    cover = models.ImageField(default='default.png', verbose_name='封面')
    category = models.ManyToManyField(Category, related_name='video')

    def __str__(self):
        return self.videoName


class Comment(models.Model):
    commentTitle = models.CharField(max_length=50, verbose_name='评论标题', null=True, blank=True)
    commentContent = CKEditor5Field(verbose_name='评论内容', config_name='extends')
    video = models.ForeignKey(Video, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, related_name='comment', on_delete=models.CASCADE)
    commentDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
