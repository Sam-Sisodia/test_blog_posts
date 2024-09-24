from django.contrib import admin

# Register your models here.
from . models import *


@admin.register(Bugger)
class Buggeradmin(admin.ModelAdmin):
    list_display=["id",
                  "name",
                "image",
                "cusine",
                "rating",
                "flavor"
                  
    ]
