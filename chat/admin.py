from django.contrib import admin
from .models import Room, Message

# Register your models here.


admin.site.register(Message)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'client', 'specialist']

