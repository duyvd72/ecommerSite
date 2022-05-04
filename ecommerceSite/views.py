from django.shortcuts import render

from store.models import Item

def home(request):
    items = Item.objects.all().filter(is_available=True)
    context = {
        'items': items,
    }
    return render(request, 'home.html', context)

def Login(request):
    return render(request,"store/user_login.html")

def Register(request):
    return render(request,"store/user_register.html")