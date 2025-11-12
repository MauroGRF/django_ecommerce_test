from .models import Category
""" 
Es una funcion que agrega el contexto de las categorias a todas las vistas
"""
def menu_links(request):
    #obteniendo las distintas categorias de la bd
    links = Category.objects.all() 
    return dict(links=links)

