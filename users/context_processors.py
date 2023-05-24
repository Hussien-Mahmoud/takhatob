from . import models


def users(request):
    return {
        'clients': models.User.objects.filter(id__in=models.Client.objects.all()),
        'centers': models.User.objects.filter(id__in=models.Center.objects.all()),
        'specialists': models.User.objects.filter(id__in=models.Specialist.objects.all()),
    }

#
# def current_user_type(request):
#     if request.user.
#
#     return {'user_type': type}
