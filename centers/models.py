from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Client, Center

# Create your models here.


class CenterReviews(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='center_reviews')
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='reviews')
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    text = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = [('client', 'center')]


class CenterSubscription(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='subscriptions')
    start_date = models.DateField(auto_now_add=True)
    duration_in_days = models.IntegerField()
    price_paid = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = [('center', 'start_date')]


class CenterTransactions(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE, related_name='transactions')
    transaction_date = models.DateTimeField(auto_now_add=True)
    paid = models.DecimalField(max_digits=8, decimal_places=2)
    our_profit = models.DecimalField(max_digits=8, decimal_places=2)

