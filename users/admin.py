from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, Center, Specialist

# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Center)
admin.site.register(Specialist)
