from django.db import models

ALLERGY_ICONS = (
    ('0', 'none'),
    ('1', 'cereal'),
    ('2', 'gluten'),
    ('3', 'milk'),
    ('4', 'eggs'),
    ('5', 'peanuts'),
    ('6', 'nuts'),
    ('7', 'crustaceans'),
    ('8', 'mustard'),
    ('9', 'fish'),
    ('11', 'lupin'),
    ('12', 'sesame'),
    ('13', 'celery'),
    ('14', 'soya'),
    ('15', 'molluscs'),
)


class Dishes(models.Model):
    '''Model for the Dishes in the menu '''
    name = models.CharField(max_length=50, unique=True)
    dish_pic = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=300)
    allergy_icon = models.CharField(max_length=12, choices=ALLERGY_ICONS, default='0')
    calorie_amount = models.CharField(max_length=6)
    protien_amount = models.CharField(max_length=6)
    carbs_amount = models.CharField(max_length=6)
    fat_amount = models.CharField(max_length=6)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
