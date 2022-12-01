from django.contrib import admin
from .models import Reservation, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    list_filter = ('max_num_guest', 'Name')
    list_display = ('Name', 'max_num_guest')
    search_fields = ['Name', 'max_num_guest']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_filter = ('date_picked', 'approved')
    list_display = (
        'name', 'email', 'phone_num',
        'table', 'date_picked', 'time_picked', 'approved')
    search_fields = ['name', 'email', 'date_picked']
    actions = ['approve_reservation', 'delete_reservation']

    def approve_reservation(self, request, queryset):
        queryset.update(approved=True)

    def delete_reservation(self, request, queryset):
        queryset.delete()
