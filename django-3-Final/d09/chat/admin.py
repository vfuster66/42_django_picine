# Dans chat/admin.py, ajoutez :
from django.contrib import admin
from .models import ChatRoom

admin.site.register(ChatRoom)