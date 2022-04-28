from django.shortcuts import render
from laptop.models import LaptopItem

from store.models import Item

def home(request):
    items = Item.objects.all().filter(is_available=True)
    context = {
        'items': items,
    }
    return render(request, 'home.html', context)