from django.contrib import admin
from .models import Categoria, CLiente, Orden, Producto
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(CLiente)
admin.site.register(Orden)