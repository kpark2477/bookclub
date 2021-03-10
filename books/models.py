from django.db import models
from core.models import TimeStampedModel

# Create your models here.

class Book(TimeStampedModel):

    """ Book Model Definition """

    GENRE_FICTION = "fiction"
    GENRE_NONFICTION = "nonfiction"

    GENRE_CHOICE = (
        (GENRE_FICTION, "Fiction"),
        (GENRE_NONFICTION, "Nonfiction"),
    )

    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    totalpages = models.IntegerField()
    cover = models.ImageField()
    description = models.TextField()
    pickreason = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="books", on_delete=models.CASCADE
    )
    genre = models.CharField(
        choices=GENRE_CHOICE, max_length=10,
        )

    def __str__(self):
        return self.title