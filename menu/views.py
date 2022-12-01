from django.shortcuts import render
from django.views import View
from .models import Dish, Drink


class MenuList(View):

    def get(self, request, *args, **kwargs):
        dishes_list = Dishes.objects.filter(available=True).order_by('name')
        drinks_list = Drinks.objects.filter(available=True).order_by('name')

        return render(
            request,
            'menu.html',
            {
                'dishes_list': dishes_list,
                'drinks_list': drinks_list,
            },
            )
