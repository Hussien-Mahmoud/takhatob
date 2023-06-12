from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Client, Specialist

# Create your models here.


class SpecialistReviews(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='specialist_reviews')
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='reviews')
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    text = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = [('client', 'specialist')]
#
#
# class ClientSubscription(models.Model):
#     specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='subscriptions')
#     start_date = models.DateField(auto_now_add=True)
#     duration_in_days = models.IntegerField()
#     price_paid = models.DecimalField(max_digits=8, decimal_places=2)
#
#     class Meta:
#         unique_together = [('specialist', 'start_date')]
#
#
# class SpecialistTransactions(models.Model):
#     specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='transactions')
#     transaction_date = models.DateTimeField(auto_now_add=True)
#     paid = models.DecimalField(max_digits=8, decimal_places=2)
#     our_profit = models.DecimalField(max_digits=8, decimal_places=2)

