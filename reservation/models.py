from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GUEST_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)


class Table(models.Model):
    '''Model for the reservation table '''
    Name = models.CharField(max_length=50, unique=True)
    max_num_guest = models.PositiveIntegerField()

    class Meta:
        ordering = ['Name']

    def __str__(self):
        return self.Name


class Reservation(models.Model):
    '''Model for the reservation'''
    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=80,)
    phone_num = models.CharField(max_length=12,)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservation_client')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE,
        related_name='reservation_table', null=True)
    num_of_guest = models.CharField(
        max_length=6, choices=GUEST_CHOICES, default='2')
    date_picked = models.DateField()
    time_picked = models.TimeField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_picked']

    def __str__(self):
        return self.name
