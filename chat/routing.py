from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/room/(?P<room_uuid>[A-Za-z0-9_-]+)/$',
            consumers.ChatConsumer.as_asgi()),
]
