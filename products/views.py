from django.http import JsonResponse, HttpResponse

from products.models import Product, Store
from products.tasks import hello_world_task


# Create your views here.
def products_view(request, *args, **kwargs):
    products = Product.objects.filter(featured=True)

    products_list = []

    for product in products:
        products_list.append({
            'title': product.title,
            'description': product.description,
            'price': product.price,
            'summary': product.summary,
            'is_18_plus': product.is_18_plus,
        })

    return JsonResponse({'data': products_list})

def store_view(request, *args, **kwargs):
    stores = Store.objects.filter(featured=True)
    stores_list = []

    for store in stores:
        stores_list.append({
            'name': store.name,
            'country': store.country,
            'city': store.city,
            'address': store.address,
            'square': store.square,
            'employees_num': store.employees_num,
            'inventory': store.inventory,
            'notes': store.notes,
            'opened_date': store.opened_date
        })
    return JsonResponse({'data': stores_list})

def celery_view(request, *args, **kwargs):
    hello_world_task.delay()

    return HttpResponse("OK")

