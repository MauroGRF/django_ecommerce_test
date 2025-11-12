from django.db import models
from django.urls import reverse

class Category(models.Model): 
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30)
    description = models.CharField( max_length=200)
    
    
    def __str__(self):
        return self.title
    def get_url(self):
        return reverse("store:products-category",args=[self.slug])
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"