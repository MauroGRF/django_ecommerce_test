from django.urls import path
from . import views
app_name = "store"  

urlpatterns = [
    path('',views.store,name="main"), 
    path('category/<slug:category_slug>/',views.store,name="products-category"),
    path('category/<slug:category_slug>/product/<slug:product_slug>/',views.details_product, name="details-product"),
]
