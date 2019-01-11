from django.contrib import admin
from .models import Flight, Message, Book

admin.site.site_header = '廉乐知系统管理'
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'flight_company', 'departure_city', 'transfer_city', 'arrival_city', 'departure_time', 'arrival_time', 'total_price', 'total_tickets')
    list_display_links = ['flight_number']
    list_filter = ('flight_company', 'departure_city', 'arrival_city')
    ordering = ['departure_time']
    search_fields = ('flight_company', 'flight_number', 'departure_city', 'arrival_city')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('affected_flight', 'delay_time', 'message', 'cancel_state')
    list_display_links = ['affected_flight']
    ordering = ['-id']
    search_fields = ['affected_flight']


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_flight', 'book_user', 'direct_purchase')
    list_display_links = ['book_flight']
    list_filter = ('book_flight', 'book_user')
    ordering = ['-id']
    search_fields = ('book_flight', 'book_user')


admin.site.register(Flight, FlightAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Book, BookAdmin)
