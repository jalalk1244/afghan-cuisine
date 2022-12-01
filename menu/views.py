from django.shortcuts import render
from django.views import View
from .models import Dish, Drink


class MenuList(View):

    def get(self, request, *args, **kwargs):
        dishes_list = Dish.objects.filter(available=True).order_by('name')
        drinks_list = Drink.objects.filter(available=True).order_by('name')

        return render(
            request,
            'menu.html',
            {
                'dishes_list': dishes_list,
                'drinks_list': drinks_list,
            },
            )
