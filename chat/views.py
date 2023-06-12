from django.shortcuts import render, reverse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

from .models import Room, Message
from users.models import Client, Specialist


# Create your views here.

@login_required
def chat_room(request, room_uuid=None):
    try:
        if room_uuid is not None:
            room = Room.objects.get(name=room_uuid)
        else:
            # requesting /chat/
            room = Room.objects.filter()
    except:
        raise HttpResponseNotFound

    if request.user.is_client():
        if request.user.id != room.client.id:
            return HttpResponseNotAllowed("you're not allowed to enter this chat")
        all_chats = Room.objects.filter(client=room.client)

    elif request.user.is_specialist():
        if request.user.id != room.specialist.id:
            return HttpResponseNotAllowed("you're not allowed to enter this chat")
        all_chats = Room.objects.filter(specialist=room.specialist)
    else:
        print('user is neither')
        return HttpResponseNotAllowed("you're not a client neither a specialist")

    chat = Message.objects.filter(room=room)
    for message in chat:
        print(message.sender, message.message)

    return render(request, 'chat/room2.html', {
        'all_chats': all_chats,
        'room': room,
        'messages': chat,
    })


@login_required
def chat_requisition(request, specialist_id):
    try:
        specialist = Specialist.objects.get(id=specialist_id)
    except:
        raise HttpResponseNotFound

    if request.user.is_client():
        client = Client.objects.get(id=request.user.id)

        try:
            room = Room.objects.create(client=client, specialist=specialist)
        except ValidationError:
            return HttpResponseNotAllowed("chat was already created previously!")

    else:
        return HttpResponseNotAllowed("you're not allowed to open a chat")

    return HttpResponseRedirect(reverse('chat:chat-room', args=[room.name]))
