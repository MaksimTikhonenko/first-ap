from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
import os
from warehouse.models import Product

@csrf_exempt
def healthcheck(request):
    return HttpResponse("OK", status=200)

@csrf_exempt
def create_product(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        name = data['name']
        country = data['country']
        category = data['category']
        price = data['price']
        expire_date = data['expire_date']

        product = Product(
            name=name, country=country, category=category,
            price=price, expire_date=expire_date
        )

        product.save()
        return JsonResponse({'id': product.product_id}, status=201)
    else:
        return HttpResponseBadRequest("Invalid request method")


@csrf_exempt
def get_product(request):
    if request.method == 'GET':

        json.loads(request.body)

        product = Product.objects.all().values()

        return JsonResponse(list(product), safe=False)


@csrf_exempt
def del_product(request):
    if request.method == 'DELETE':
        json.loads(request.body)
        product = Product.objects.filter(id=id).delete()
        return JsonResponse({'id': product.product_id}, ': DELETED')
    else:
        return HttpResponseBadRequest("Invalid request method")
