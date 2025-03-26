from django.urls import path

from .views import login, logout, register, my

urlpatterns = [
    path('login/', login.as_view(), name='login'),
    path('logout/', logout),
    path('register/', register.as_view(), name='register'),
    path('my/', my)
]
