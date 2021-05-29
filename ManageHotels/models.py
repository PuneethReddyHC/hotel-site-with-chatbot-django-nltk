from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from HotelApp.models import Hotels
# Stating the Photo model , and giving it a file field to allow photo uploads.
class Photo(models.Model):

    path = models.FileField()
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Photo'

    def __str__(self):
         return self.hotel.Name
