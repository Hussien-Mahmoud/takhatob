from . import models


def users(request):
    return {
        'clients': models.User.objects.filter(id__in=models.Client.objects.all()),
        'centers': models.User.objects.filter(id__in=models.Center.objects.all()),
        'specialists': models.User.objects.filter(id__in=models.Specialist.objects.all()),
    }


def user_chats(request):
    if request.user.is_specialist():
        specialist = models.Specialist.objects.get(id=request.user.id)
        room = specialist.rooms.all()[0] or None
        if room:
            room = room.get_absolut_url()
    elif request.user.is_client():
        client = models.Client.objects.get(id=request.user.id)
        room = client.rooms.all()[0] or None
        if room:
            room = room.get_absolut_url()
    else:
        room = None

    return {
        'chats': room,
    }
