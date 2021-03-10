from django.contrib.auth.models import AbstractUser
from django.db import models
from core import managers as core_managers

# Create your models here.


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    profilepic = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICE, max_length=10, null=True, blank=True
        )
    bio = models.TextField(default="", blank=True)

    objects = core_managers.CustomUserManager()
