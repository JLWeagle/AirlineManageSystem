from django.urls import path

from . import views

app_name="main"

urlpatterns = [
    path('flightinfo/', views.flightinfo, name='flightinfo'),
    path('flightactivity/', views.flightactivity, name='flightactivity'),
    path('ticketmanage/', views.ticketmanage, name='ticketmanage'),
    path('ticketquery/', views.ticketquery, name='ticketquery'),
    path('recommendation/', views.recommendation, name='recommendation')
    
]
