from django.db import models
from categorias.models import Category
# Create your models here.

# nombre, descripcion, slug, costo, stock, categoría, img ...    
 
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank= True)
    cost = models.IntegerField()
    image = models.ImageField(upload_to="imgs/products/") #Old-school 
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True) #activar y desactivarlo del stock
    category = models.ForeignKey( 
        Category, on_delete= models.CASCADE #al eliminar la categoria se borran todos los prod.
    )
    
    date_register = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name