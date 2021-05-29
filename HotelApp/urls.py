from django.conf.urls import url
from HotelApp import views
from django.urls import path,include

app_name = 'HotelApp'

urlpatterns = [
     path('', views.hotelIndex.as_view(), name='hotelindex'),
     path('hotels/<int:pk>/', views.hoteldetails, name='hoteldetails'),
     path('<int:id>/reviews/create', views.reviewCreateView.as_view(), name='createreview'),
     path('<int:pk>/reviews/edit', views.reviewUpdateView.as_view(), name='editreview'),
     path('<int:pk>/reviews/delete', views.reviewDeleteView.as_view(), name='deletereview'),
     path('partner/apply', views.partnerCreateView.as_view(), name='newproposal'),
]