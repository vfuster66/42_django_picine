from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatroom_list, name='chatroom_list'),
    path('<str:room_name>/', views.chatroom, name='chatroom'),
]
