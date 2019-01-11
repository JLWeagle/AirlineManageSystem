from django.shortcuts import render, redirect
from .models import Flight, Message, Book
# Create your views here.
def flightinfo(request):
    return redirect("../../admin/main/flight")


def flightactivity(request):
    return redirect("../../admin/main/message")


def ticketmanage(request):
    return redirect("../../admin/main/book")

def ticketquery(request):
    context = {}
    for flight in Flight.object.all():
    return render(request, 'main/ticketquery.html', context)

def recommendation(request):
    context = {}
    return render(request, 'main/recommendation.html', context)
