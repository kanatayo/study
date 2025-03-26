
from django.urls import path

from .views import index, video_list, video_details, video_list_default, delete_history, Comment

urlpatterns = [
    path('index/', index),
    path('list/', video_list_default),
    path('list/<int:categoryId>', video_list),
    path('details/<int:video_id>', video_details),
    path('delete_history/<int:video_id>', delete_history),
    path('comment/<int:video_id>', Comment.as_view())
]
