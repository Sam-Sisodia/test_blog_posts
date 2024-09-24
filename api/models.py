from django.db import models

# Create your models here.

from django.utils.translation import gettext_lazy as _


# Create your models here.

from django.contrib.auth.models import AbstractUser


class  User(AbstractUser):
    address = models.CharField(_("addredss"),max_length=200,null=True,blank="True")
class Bugger(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='staic/media')
    cusine = models.CharField(max_length=200)
    rating  = models.CharField(max_length=200)
    flavor  = models.CharField(max_length=200)