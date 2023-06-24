from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden

from decimal import Decimal
import stripe

from users.models import Specialist, Client
from chat.models import Room

# create the Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def client_payment(request, specialist_id):
    if not request.user.is_client():
        return HttpResponseForbidden()
    client = Client.objects.get(id=request.user.id)
    specialist = get_object_or_404(Specialist, id=specialist_id)

    success_url = request.build_absolute_uri(reverse('payment:completed'))
    cancel_url = request.build_absolute_uri(reverse('payment:canceled'))

    # stripe.Product.create(name="Basic subscription")
    # stripe.Price.create(
    #     product='{{PRODUCT_ID}}',
    #     unit_amount=1000,
    #     currency="egp",
    #     recurring={"interval": "month"},
    # )
    #
    # stripe.Subscription.create(
    #     customer='{{CUSTOMER_ID}}',
    #     items=[{"price": "{{RECURRING_PRICE_ID}}"}],
    # )
    #
    # stripe.Subscription.create(
    #     customer="cus_O676UEpQiY9uB2",
    #     items=[
    #         {
    #             "price_data": {
    #                 'currency': 'egp',
    #                 'product': '',
    #                 'recurring': {
    #                     'interval': 'month',
    #                     'interval_count': 1,
    #                 },
    #                 'unit_amount_decimal': Decimal(150.00)
    #             }
    #         },
    #     ],
    # )

    # stripe checkout session data
    session_data = {
        'mode': 'subscription',
        'client_reference_id': Room.objects.get(specialist=specialist, client=client).name,
        'currency': 'egp',
        'success_url': success_url,
        'cancel_url': cancel_url,
        'customer_email': request.user.email,
        'line_items': [{
            'price_data': {
                'unit_amount': int(specialist.service_price * Decimal('100')),
                'currency': 'egp',
                'product_data': {
                    'name': '1 month chat'
                },
                'recurring': {
                    'interval': 'month',
                    'interval_count': 1,
                },
            },
            'quantity': 1
        }],
    }

    # # add order items to the Stripe checkout session
    # for item in order.items.all():
    #     session_data['line_items'].append({
    #         'price_data': {
    #             'unit_amount': int(item.price * Decimal('100')),
    #             'currency': 'usd',
    #             'product_data': {
    #                 'name': item.product.name
    #             }
    #         },
    #         'quantity': item.quantity
    #     })

    # change chat state to ENABLED
    room = Room.objects.get(specialist=specialist, client=client)
    room.status = Room.Status.ENABLED
    room.save()

    # create Stripe checkout session
    session = stripe.checkout.Session.create(**session_data)
    # redirect to Stripe payment form
    return redirect(session.url)


def payment_completed(request):
    return render(request, 'payment/completed.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
