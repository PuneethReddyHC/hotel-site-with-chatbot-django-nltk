from django.urls import path

from . import views

app_name = 'HotelChatbot'
urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
    path('addmsg/',views.addmsg, name='addmsg'),
    ]
