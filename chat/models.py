import uuid
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import User, Specialist, Client

# Create your models here.


class AvailableChatsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__in=[Room.Status.ENABLED, Room.Status.DISABLED])


class ReadOnlyChatsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Room.Status.DISABLED)


class OpenChatsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Room.Status.ENABLED)


class RequestedChatsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Room.Status.REQUESTED)


class AcceptedChatsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Room.Status.ACCEPTED)


class Room(models.Model):
    class Status(models.TextChoices):
        """
        REQUESTED: client's request chat (usually step 1)
        ACCEPTED: specialist's accepted chat request (usually step 2)
        DISABLED: the chat exists but read-only
        ENABLED: chat between client and specialist is open (usually step 3 after the client pays)
        """
        REQUESTED = 'REQUESTED', 'Requested'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        DISABLED = 'DISABLED', 'Disabled'
        ENABLED = 'ENABLED', 'Enabled'

    name = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='rooms')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='rooms')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=Status.choices, default=Status.DISABLED)

    objects = models.Manager()
    requested = RequestedChatsManager()
    accepted = AcceptedChatsManager()
    disabled = ReadOnlyChatsManager()
    enabled = OpenChatsManager()

    def get_absolut_url(self):
        return reverse('chat:chat-room', args=[self.name])

    def is_new_for_specialist(self):
        if self.status == Room.Status.ENABLED and not self.messages.filter(sender_id=self.specialist.id):
            return True
        return False

    def is_new_for_client(self):
        if self.status == Room.Status.ENABLED and not self.messages.filter(sender_id=self.client.id):
            return True
        return False

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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.room.status == self.room.Status.DISABLED:
            raise ValidationError(_("this Chat room is Disabled, you can't write to it"))
        if self.room.status == self.room.Status.REQUESTED:
            raise ValidationError(_("this Chat room is requested but not open yet, you can't write to it"))
        if self.room.status == self.room.Status.ACCEPTED:
            raise ValidationError(_("this Chat room is accepted but not open yet, you can't write to it"))

        return super(Message, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
