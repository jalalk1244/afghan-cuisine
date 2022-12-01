from django.contrib import admin
from .models import Dish, Drink, Alergen


admin.site.register(Drink)
admin.site.register(Alergen)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_filter = ('price', 'available')
    list_display = ('name', 'price', 'calorie_amount', 'protien_amount', 'carbs_amount', 'fat_amount', 'available')
    search_fields = ['name', 'description']
    filter_horizontal = ('alergens',)
