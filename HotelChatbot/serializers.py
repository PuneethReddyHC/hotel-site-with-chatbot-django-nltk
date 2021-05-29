from rest_framework import serializers
from django.conf import settings
from HotelChatbot.models import messageItem, Bot

class GetMessagesSerializer(serializers.Serializer):
    bot_id = serializers.IntegerField(
        required=False,
    )

class AddMessageSerializer(serializers.Serializer):
    bot_id = serializers.IntegerField(
        required=False,
    )
    content = serializers.CharField(
        required=True,
        max_length=100
    ) 

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = (
            'id',
            'botname',
            'image',
            'created'
        )

class MessagesSerializer(serializers.ModelSerializer):
    bot = BotSerializer(many = False)
    class Meta:
        model = messageItem
        fields = (
            'id',
            'content',
            'isbot',
            'bot',
            'creator',
            'created'

        )