from django.shortcuts import render, get_object_or_404
from store.models import Item, ItemType, LaptopItem


def store(request, item_type_slug=None):
    item_type = None
    items = None

    if item_type_slug != None:
        item_type = get_object_or_404(ItemType, slug=item_type_slug)
        items = Item.objects.filter(item_type=item_type, is_available=True)
        item_count = items.count()
    else:
        items = Item.objects.all().filter(is_available=True)
        item_count = items.count()

    context = {
        'items': items,
        'item_count': item_count,
    }
    return render(request, 'store/store.html', context)


def item_detail(request, item_type_slug, item_slug):
    try:
        single_item = Item.objects.get(item_type__slug=item_type_slug, slug=item_slug)
    except Exception as e:
        raise e

    context = {
        'single_item': single_item,
    }
    return render(request, 'store/item_detail.html', context)