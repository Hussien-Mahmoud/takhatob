import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Message, Room


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.uuid = self.scope['url_route']['kwargs']['room_uuid']
        self.room = f'{self.uuid}'

        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room,
            self.channel_name
        )

        # accept connection
        self.accept()

    def disconnect(self, code):
        # leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room,
            self.channel_name
        )

    # receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        db_massage = Message(
            sender=self.user,
            room=Room.objects.get(name=self.room),
            message=message,
        )
        db_massage.save()

        # Chat.objects.create(
        #     sender=self.user,
        #     room_group_name=self.room_group_name,
        #     message=message,
        # )

        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.user.id,
                'username': f'{self.user.first_name}'
                            f'{" " + self.user.last_name if self.user.last_name else ""}',
                'datetime': db_massage.send_date.isoformat(),
            }
        )

        # # send message to WebSocket
        # self.send(text_data=json.dumps({'message': message}))

    # receive message from room group
    def chat_message(self, event):
        # send message to WebSocket
        self.send(text_data=json.dumps(event))
