import uuid
from django.db import models
from users.models import User, Specialist, Client
from django.urls import reverse

# Create your models here.


class Room(models.Model):
    name = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='rooms')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='rooms')
    date_created = models.DateTimeField(auto_now_add=True)

    def get_absolut_url(self):
        return reverse('chat:chat-room', args=[self.name])

    class Meta:
        ordering = ['-date_created']
        unique_together = [('specialist', 'client')]


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    send_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    class Meta:
        ordering = ['-room', 'send_date']
        indexes = [
            models.Index(fields=['-room', 'send_date'])
        ]

