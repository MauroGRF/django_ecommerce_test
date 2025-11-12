from django.shortcuts import render, get_object_or_404
from .models import Product
from categorias.models import Category
def store(request,category_slug=None):
    category = None
    products = None   
    if category_slug != None:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.all().filter(is_available=True, category=category)    
        counter_products = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)    
        counter_products = products.count()
           
    context = {
        "all_products" : products,
        "counter_products": counter_products,
        "category" : category,
    }
    return render(request, "store/tienda.html", context=context)

def details_product(request,category_slug, product_slug):
    product = get_object_or_404(Product, Category__slug=category_slug, slug=product_slug)
    context = {
        "product" : product,
    }
    return render(request, "store/product.html", context=context)