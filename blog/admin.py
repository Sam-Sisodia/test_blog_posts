from django.contrib import admin
from . models import *


# Register your models here.


@admin.register(PostHashTag)
class PostHashTagadmin(admin.ModelAdmin):
    list_display=["id","hashtag"
                  
    ]





@admin.register(InstaPassword)
class InstaPasswordadmin(admin.ModelAdmin):
    list_display=["id","name","password"
                  
    ]

@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_display=["id","title","date_time","description","summary",
                  
    ]



@admin.register(Blog_Commnet)
class Blog_Commnet_admin(admin.ModelAdmin):
    list_display=["id","blog","comment","date_time"
                  
    ]


@admin.register(Share_Blog)
class Share_Blog_admin(admin.ModelAdmin):
    list_display=["id","blog","token","email","date_time"
                  
    ]


    