from . import models


def users(request):
    return {
        'clients': models.Client.objects.all(),
        'centers': models.Center.objects.all(),
        'specialists': models.Specialist.objects.all(),
    }

#
# def current_user_type(request):
#     if request.user.
#
#     return {'user_type': type}
