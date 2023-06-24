from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db.models import Avg


from decimal import Decimal

# from centers.models import CenterReviews

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        null=False,
    )

    username = models.CharField(
        _("username"),
        max_length=255,
        unique=False,
        null=False,
    )

    first_name = models.CharField(_("first name"), max_length=150, null=True, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'.strip()
        else:
            return f'{self.first_name}'.strip()

    def is_client(self) -> bool:
        try:
            Client.objects.get(id=self.id)
            return True
        except:
            return False

    def is_center(self) -> bool:
        try:
            Center.objects.get(id=self.id)
            return True
        except:
            return False

    def is_specialist(self) -> bool:
        try:
            Specialist.objects.get(id=self.id)
            return True
        except:
            return False


class Center(User):
    excerpt = models.CharField(max_length=100, null=True, blank=True)
    description = HTMLField(null=True, blank=True)  # TextField inside
    experience = models.IntegerField(null=True, blank=True)
    image = models.ImageField(
        upload_to='images/centers/profile_images/',
        default='images/centers/default-placeholder.png',
    )
    is_subscribed = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username']

    def get_absolute_url(self):
        return reverse('center-details', args=[self.id])

    def average_rating(self):
        return int(self.reviews.aggregate(Avg('rate')).get('rate__avg') or 0)

    class Meta:
        verbose_name = 'center'


class Specialist(User):
    excerpt = models.CharField(max_length=100, null=True, blank=True)
    description = HTMLField(null=True, blank=True)  # TextField inside
    experience = models.IntegerField(null=True, blank=True, default=0)
    service_price = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal(0.00))
    image = models.ImageField(
        upload_to='images/specialists/profile_images/',
        default='images/centers/default-placeholder.png',
    )

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('specialist-details', args=[self.id])

    def has_requested_chats(self):
        requested_chats = self.rooms.filter(status='REQUESTED')
        return bool(requested_chats)

    def has_new_enabled_chats(self):
        chats = self.rooms.filter(status='ENABLED').filter(messages__sender_id=self.id)
        return not bool(chats)

    def average_rating(self):
        return int(self.reviews.aggregate(Avg('rate')).get('rate__avg') or 0)

    class Meta:
        verbose_name = 'specialist'


class Client(User):
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_requested_chats(self):
        requested_chats = self.rooms.filter(status='REQUESTED')
        return bool(requested_chats)

    def has_accepted_chats(self):
        accepted_chats = self.rooms.filter(status='ACCEPTED')
        return bool(accepted_chats)

    class Meta:
        verbose_name = 'client'

