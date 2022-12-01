from django.db import models
from cloudinary.models import CloudinaryField


class Alergen(models.Model):
    '''Model for all the allergens choices'''
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Dish(models.Model):
    '''Model for the Dishes in the menu '''
    name = models.CharField(max_length=50, unique=True)
    dish_pic = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=300)
    alergens = models.ManyToManyField(Alergen)
    calorie_amount = models.CharField(max_length=6)
    protien_amount = models.CharField(max_length=6)
    carbs_amount = models.CharField(max_length=6)
    fat_amount = models.CharField(max_length=6)
    price = models.FloatField(default=0)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Drink(models.Model):
    '''Model for the Dishes in the menu '''
    name = models.CharField(max_length=50, unique=True)
    drink_pic = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=300)
    price = models.FloatField()
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
