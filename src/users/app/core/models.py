from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("User must have an phone_number")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            phone_number=phone_number
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_employee = False
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("User must have an phone_number")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            phone_number=phone_number
        )
        user.set_password(password)
        user.is_admin = True
        user.is_employee = False
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(db_index=True, blank=False, null=True, unique=True)
    first_name = models.CharField(
        db_index=True, blank=False, null=False, max_length=100
    )
    middle_name = models.CharField(db_index=True, blank=True, null=True, max_length=100)
    last_name = models.CharField(db_index=True, blank=True, null=True, max_length=100)
    phone_number = models.CharField(
        db_index=True, blank=True, null=True, max_length=100, unique=True
    )
    password = models.CharField(max_length=255)
    is_employee = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    username = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
