from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_room, name='chats'),
    path('room/<uuid:room_uuid>/', views.chat_room, name='chat-room'),
    path('request_chat/<int:specialist_id>/', views.chat_requisition, name='chat-requisition'),
    path('approve_chat/<uuid:room_uuid>/', views.chat_approve, name='chat-approve'),
    path('deny_chat/<uuid:room_uuid>/', views.chat_deny, name='chat-deny'),
]
