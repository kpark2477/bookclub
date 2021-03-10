from django.db import models
from core import models as core_models

# Create your models here.

class Comment(core_models.TimeStampedModel):

    """ Comment Model Definition """

    comment = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="comments", on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        "books.Book", related_name="comments", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)
