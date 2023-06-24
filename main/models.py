from django.db import models

# Create your models here.


class ContactMessageModel(models.Model):
    name = models.CharField(max_length=50)
