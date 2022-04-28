from django.shortcuts import render

# Create your views here.
from store.models import Item


def store(request):
    items = Item.objects.all().filter(is_available=True)
    context = {
        'items': items,
    }
    return render(request, 'store/store.html', context)
