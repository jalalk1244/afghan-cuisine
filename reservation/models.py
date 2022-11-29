from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GUEST_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)

class Table(models.Model):
    '''Model for the reservation table '''
    Name = models.CharField(max_length=20, unique=True)
    max_num_guest = models.IntegerField()


class Reservation(models.Model):
    '''Model for the reservation'''
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservation_client')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservation_table')
    num_of_guest = models.IntegerField(choices=GUEST_CHOICES, default='2')
    date_picked = models.DateField()
    time_picked = models.TimeField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_picked']

    def __str__(self):
        return self.title
