from django.shortcuts import render
from django.http import request
from store.models import Product


def home(request):
    #obteniendo todos los productos disponibles de la BD 
    products = Product.objects.all().filter(is_available=True) 
    context = {"products": products}
    return render(request, "home/home.html",context)