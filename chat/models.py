from django.db import models
from users.models import User

# Create your models here.


class Room(models.Model):
    name = models.UUIDField(primary_key=True)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    send_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['room', 'send_date']
        indexes = [
            models.Index(fields=['room', 'send_date'])
        ]

