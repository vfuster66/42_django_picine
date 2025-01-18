import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom, Message

class ChatConsumer(AsyncWebsocketConsumer):
    connected_users = {}  # Dictionnaire pour stocker les utilisateurs par room

    @database_sync_to_async
    def save_message(self, username, message, room_name):
        room = ChatRoom.objects.get(name=room_name)
        return Message.objects.create(room=room, username=username, content=message)

    @database_sync_to_async
    def get_recent_messages(self, room_name):
        room = ChatRoom.objects.get(name=room_name)
        messages = list(Message.objects.filter(room=room)
                   .order_by('-timestamp')[:3]
                   .values('content', 'username'))

        return messages[::-1]

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope["user"].username

        # Rejoindre la room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Récupérer les derniers messages
        recent_messages = await self.get_recent_messages(self.room_name)
        for message in recent_messages:
            await self.send(text_data=json.dumps({
                'message': message['content'],
                'username': message['username']
            }))

        # Gérer la liste des utilisateurs
        if self.room_name not in self.connected_users:
            self.connected_users[self.room_name] = set()
        self.connected_users[self.room_name].add(self.user)

        # Envoyer la liste mise à jour des utilisateurs
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_list',
                'users': list(self.connected_users[self.room_name])
            }
        )

        # Envoyer le message de connexion
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f"{self.user} has joined the chat",
                'username': 'System'
            }
        )

    async def disconnect(self, close_code):
        if self.room_name in self.connected_users and self.user in self.connected_users[self.room_name]:
            self.connected_users[self.room_name].remove(self.user)
            
            # Envoyer la liste mise à jour et le message de départ
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_list',
                    'users': list(self.connected_users[self.room_name])
                }
            )
            
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': f"{self.user} has left the chat",
                    'username': 'System'
                }
            )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        # Sauvegarder le message
        await self.save_message(username, message, self.room_name)

        # Envoyer le message au groupe
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Envoyer le message au WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def user_list(self, event):
        await self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': event['users']
        }))