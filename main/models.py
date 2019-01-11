from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flight(models.Model):
    flight_company = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=255)
    transfer_city = models.CharField(max_length=255, null=True, blank=True)
    arrival_city = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    total_price = models.IntegerField()
    total_tickets = models.IntegerField()
    
    def __str__(self):
        return self.flight_number


class Message(models.Model):
    affected_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    delay_time = models.TimeField(null=True, blank=True)
    message = models.TextField()
    cancel_state = models.BooleanField(default=False)

    def __str__(self):
        return self.affected_flight.flight_number


class Book(models.Model):
    book_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    book_user = models.ForeignKey(User, on_delete=models.CASCADE)
    direct_purchase = models.BooleanField(default=True)

    def __str__(self):
        return self.book_user.username+' '+self.book_flight.flight_number
