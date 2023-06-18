from . import models


def users(request):
    current_user = None
    if not request.user.is_anonymous:
        if request.user.is_client():
            current_user = models.Client.objects.get(id=request.user.id)
        elif request.user.is_center():
            current_user = models.Center.objects.get(id=request.user.id)
        elif request.user.is_specialist():
            current_user = models.Specialist.objects.get(id=request.user.id)

    return {
        'clients': models.User.objects.filter(id__in=models.Client.objects.all()),
        'centers': models.User.objects.filter(id__in=models.Center.objects.all()),
        'specialists': models.User.objects.filter(id__in=models.Specialist.objects.all()),

        'current_user': current_user
    }


def user_chats(request):
    room = None
    if not request.user.is_anonymous:
        if request.user.is_specialist():
            specialist = models.Specialist.objects.get(id=request.user.id)
            room = specialist.rooms.all() or None
            if room:
                room = room[0].get_absolut_url()
        elif request.user.is_client():
            client = models.Client.objects.get(id=request.user.id)
            room = client.rooms.all() or None
            if room:
                room = room[0].get_absolut_url()

    return {
        'chats': room,
    }
