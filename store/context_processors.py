from store.models import ItemType


def menu_links(request):
    links = ItemType.objects.all()
    return dict(links=links)