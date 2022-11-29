from . import views
from django.urls import path

urlpatterns = [
    path('reservations', views.ReservationList.as_view(), name='reservations'),
    path('create_reservation', views.create_reservation, name='create_reservation'),
    path('edit_reservation/<int:reservation_id>', views.edit_reservation, name='edit_reservation'),
    path('delete_task/<int:reservation_id>', views.delete_reservation, name='delete_reservation')
]