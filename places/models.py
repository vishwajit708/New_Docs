from django.db import models
from django.conf import settings
# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=20,blank=True, null=True)
    addr=models.TextField(max_length=35,blank=True, null=True)
    open_time=models.TimeField(blank=True, null=True)
    close_time=models.TimeField(blank=True, null=True)


class AddPlace(models.Model):
    name=models.CharField(max_length=20,blank=True, null=True)
    addr=models.TextField(max_length=35,blank=True, null=True)
    open_time=models.TimeField(blank=True, null=True)
    close_time=models.TimeField(blank=True, null=True)
    usr=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
