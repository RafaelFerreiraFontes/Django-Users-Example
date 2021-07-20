from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('<str:_id>/user/', views.user, name='user')
]