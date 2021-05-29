from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from ManageHotels import views
from ManageHotels.views import ChartData,ChartView
from django.urls import path,include
app_name = 'ManageHotels'

# Specifying all the urls for the Manage Hotels app which the partners will see .
# Allows for Creating Hotels , Editing them and photos , and adding rooms etc.

urlpatterns = [
     path('', views.home, name='home'),
     path('newhotel', views.HotelCreateView.as_view(), name='createhotel'),
     path('yourhotels', views.showhotels, name='showhotel'),
     path('yourhotels/<int:pk>/edit', views.HotelUpdateView.as_view(), name='editHotel'),
     path('yourhotels/<int:pk>/bookings', views.showreservations, name='hotelreservations'),
     path('yourhotels/<int:pk>/delete', views.HotelDeleteView.as_view(), name='deleteHotel'),
     path('yourhotels/bookings/<int:pk>/delete', views.cancelbooking, name='removebooking'),
     path('yourhotels/<int:pk>/dashboard', views.showdashboard, name='hoteldash'),
     path('yourhotels/<int:pk>/manage', views.managehotel, name='managehotel'),
     path('yourhotels/<int:pk>/rooms', views.showRoomsDash, name='showRoomsDash'),
     path('yourhotels/<int:pk>/rooms/add', views.RoomCreateView.as_view(), name='addRoom'),
     path('yourhotels/<int:pk>/rooms/edit', views.RoomUpdateView.as_view(), name='editRoom'),
     path('yourhotels/<int:pk>/rooms/delete', views.RoomDeleteView.as_view(), name='deleteRoom'),
     path('yourhotels/<int:id>/upload', views.BasicUploadView.as_view(), name='basicupload'),
     path('yourhotels/<int:id>/photodash', views.showphotodash, name='photodash'),
     path('yourhotels/<int:id>/thumbnail', views.editThumbnail, name='editThumb'),
     path('yourhotels/<int:id>/deletephoto', views.deletePhoto, name='deletephoto'),
     path('yourhotels/<int:id>/charts', ChartView.as_view(), name = 'partnercharts'),
     path('yourhotels/<int:id>/chart/data', ChartData.as_view()),

]
