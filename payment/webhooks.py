import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import Client, Specialist
from chat.models import Room


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    print(payload)
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    print(request.META)
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'payment_intent.succeeded':
        session = event.data.object
        print(event)
        print(event.data)
        print(event.data.object)

        try:
            room = Room.objects.get(name=session.client_reference_id)
        except Client.DoesNotExist:
            return HttpResponse(status=404)

        room.status = Room.Status.ENABLED
        room.save()


    return HttpResponse(status=200)
