from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
import os
from warehouse.models import Product, Personnel


@csrf_exempt
def healthcheck(request):
    return HttpResponse("OK", status=200)


# ---------Class_Product----------
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

        product = Product.objects.all().values()

        return JsonResponse(list(product), safe=False)


@csrf_exempt
def del_product(request):
    if request.method == 'DELETE':

        product = Product.objects.get(product_id=id)
        product.delete()

        return JsonResponse({'id': product.product_id}, ': DELETED')
    else:
        return HttpResponseBadRequest("Invalid request method")


#  --------- Class_Personnel -------------
@csrf_exempt
def create_person(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        name = data['name']
        age = data['age']
        position = data['position']
        start_of_work = data['start_of_work']

        person = Personnel(
            name=name, age=age, position=position,
            start_of_work=start_of_work
        )

        person.save()
        return JsonResponse({'id': person.person_id}, status=201)
    else:
        return HttpResponseBadRequest("Invalid request method")


@csrf_exempt
def get_person(request):
    if request.method == 'GET':

        person = Personnel.objects.all().values()

        return JsonResponse(list(person), safe=False)
