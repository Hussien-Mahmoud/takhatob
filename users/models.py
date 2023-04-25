from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

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


class Client(User):
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'client'


class Center(User):
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'center'


class Specialist(User):
    class Meta:
        verbose_name = 'specialist'
