from django.shortcuts import render
from .models import ChatRoom
from django.contrib.auth.decorators import login_required

@login_required
def chatroom_list(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chat/chatroom_list.html', {'chatrooms': chatrooms})


@login_required
def chatroom(request, room_name):
    return render(request, 'chat/chatroom.html', {'room_name': room_name})
