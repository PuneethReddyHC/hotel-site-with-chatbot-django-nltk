from django.contrib import admin
from .models import messageItem, Bot
# Register your models here.
# class MessageItemAdmin():
admin.site.register(messageItem)
admin.site.register(Bot)