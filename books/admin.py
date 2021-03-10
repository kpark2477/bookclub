from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    """ Book Admin Definition """

    list_display = (
        "title",
        "author",
        "totalpages",
        "user",
        "genre",
    )