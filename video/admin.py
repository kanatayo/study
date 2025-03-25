from django.contrib import admin

from .models import Actor, Video, Category


# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass