from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from core.managers import UserManager


class Job(models.Model):
    title = models.CharField(max_length=100)
    min_salary = models.FloatField()
    max_salary = models.FloatField()


class Language(models.Model):
    language = models.CharField(max_length=100)


class User(AbstractBaseUser):
    email = models.EmailField(db_index=True, blank=False, null=True, unique=True)
    first_name = models.CharField(
        db_index=True, blank=False, null=False, max_length=100
    )
    middle_name = models.CharField(db_index=True, blank=True, null=True, max_length=100)
    last_name = models.CharField(db_index=True, blank=True, null=True, max_length=100)
    phone_number = models.CharField(
        db_index=True, blank=True, null=True, max_length=100, unique=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    def __str__(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin




