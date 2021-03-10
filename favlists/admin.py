from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Favlist)
class FavlistAdmin(admin.ModelAdmin):

    """ Favlist Admin Definition """

    list_display = (
        "user",
    )