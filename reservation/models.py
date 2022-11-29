from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, 'Not approved'), (1, 'Approved'))


class Table(models.Model):
    '''Model for the reservation table '''
    Name = models.CharField(max_length=20, unique=True)
    max_num_guest = models.IntegerField()
