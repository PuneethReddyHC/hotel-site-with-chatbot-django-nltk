from django.db import models
from HotelApp.models import User
from django.utils import timezone
# Create your models here.
class Bot(models.Model):
    botname= models.CharField(max_length=30)
    image= models.CharField(max_length  = 245)
    created = models.DateTimeField(editable=False, db_index=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Bot, self).save(*args, **kwargs)

class messageItem(models.Model):
    content = models.TextField()
    isbot = models.BooleanField(default = False)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, related_name='bot_name', null=False)
    created = models.DateTimeField(editable=False, db_index=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='add_message', null=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(messageItem, self).save(*args, **kwargs)

