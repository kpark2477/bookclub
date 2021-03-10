from django.db import models
from core.models import TimeStampedModel

# Create your models here.

class Favlist(TimeStampedModel):

    """ Favlist Model Definition """

    name = models.CharField(max_length=50)
    user = models.OneToOneField(
        "users.User", related_name="favlist", on_delete=models.CASCADE
    )
    books = models.ManyToManyField("books.Book", related_name="favlists",)