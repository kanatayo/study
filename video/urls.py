
from django.urls import path

from .views import index, video_list, video_details

urlpatterns = [
    path('index/', index),
    path('list/<str:categoryName>', video_list),
        path('details/<int:video_id>', video_details)
]
