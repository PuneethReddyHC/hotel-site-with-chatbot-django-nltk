from django.shortcuts import render,redirect
from .models import messageItem, Bot
from .nlp import give_response

# Create your views here.
from django.http import HttpResponse
import requests
from django.db import transaction
from HotelApp.models import Hotels
from HotelApp.models import Room
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from HotelChatbot.serializers import GetMessagesSerializer, MessagesSerializer, AddMessageSerializer
# def home(request):
#     return render(request, 'home.html')

def chatbot(request):
    all_message_items = messageItem.objects.filter(creator=request.user)
    # all_message_items = []
    
        
    all_bots = Bot.objects.all()
    return render(request, 'multichat.html',
    {'all_message_items': all_message_items,
    'all_bots' : all_bots })

def addmsg(request):
    c = request.POST['content']
    botid = request.POST['botid']
    print(c, botid)
    bot= Bot.objects.get(id=botid)
    new_item = messageItem(content = c, creator=request.user, bot=bot)
    new_item.save()
    
    bot_msg(request, c, bot=bot)
    return redirect('/chatbot/')

def bot_msg(request, msg, bot):
    msg = msg.lower()
    if "weather" in msg:
        lst = msg.split(' ')
        if(len(lst) > 1):

            bot_msg = give_response(msg)
            if isinstance(bot_msg, dict):
                c='<b>'+ bot_msg["city"] +'</b> Weather Info '
                c+='<ul class="weather nested_lu">'
                c+='<li class="input__nested-list">Current Temperature <span class="bot__command">'+ str(bot_msg["temperature"]) + '&#176; C</span> </li>'
                c+='<li class="input__nested-list"><img id="icon" class="icon" src="http://openweathermap.org/img/w/'+str(bot_msg['icon'])+'.png" width="10"> </li>'
                c+='<li class="input__nested-list">clouds|'+bot_msg['description']+'</li>'
                c+='</ul>'
            else:
                c= bot_msg
        
        else:
            c = "No city name found"
    elif "hotels" in msg  or "list" in msg:
        hotels = Hotels.objects.all()
        c = '<div class="cont">List of <b> Hotels </b>'
        c+= '<ul class="hotels nested_lu">'
        for hotel in hotels:
            rooms = Room.objects.filter(hotel=hotel)
            for room in rooms:
                price = room.Price
            c+= '<li class="input__nested-list">'+hotel.Name+' :<span class="bot__command">$'+ str(price) +' </span> </li>'
                   
        c+='</ul></div>'
    else:
        c = give_response(msg)
    new_item = messageItem(content = c, isbot = True, creator=request.user, bot=bot)
    new_item.save()
    return redirect('/chatbot/')

# class MessageItem(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):

#         request_data = request.data.copy()

#         serializer = GetMessagesSerializer(data=request_data)
#         serializer.is_valid(raise_exception=True)

#         data = serializer.validated_data
#         bot_id = data.get('bot_id', 1)
#         bot= Bot.objects.get(id=bot_id)
#         message_items = messageItem.objects.filter(creator=request.user, bot = bot)
        
#         messages_serializer = MessagesSerializer(message_items, many=True, context={"request": request})

#         return Response(messages_serializer.data, status=status.HTTP_200_OK)

   
#     def post(self, request):
#         request_data = request.data.dict()

#         serializer = AddMessageSerializer(data=request_data, context={"request": request})
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data

#         content = data.get('content')
#         print(content)
#         bot_id = data.get('bot_id',1)
#         bot= Bot.objects.get(id=bot_id)
#         c = give_response(content)
#         print(c)
#         with transaction.atomic():
#             user_msg = messageItem(content = content, creator=request.user, bot=bot)
#             user_msg.save()
#             bot_msg = messageItem(content = c, isbot = True, creator=request.user, bot=bot)
#             bot_msg.save()

#         messages_serializer = MessagesSerializer(bot_msg, context={"request": request})

#         return Response(messages_serializer.data, status=status.HTTP_200_OK)
