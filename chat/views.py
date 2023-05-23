from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Room, Message

# Create your views here.


@login_required
def chat_room(request, room_id):
    pass
    # try:
    #     course = request.user.courses_joined.get(id=course_id)
    # except:
    #     return HttpResponseForbidden()
    #
    # chat = Chat.objects.filter(room_group_name=f'chat_{course_id}')
    # return render(request, 'chat/room.html', {
    #     'room': Room
    #     'messages': chat
    # })
