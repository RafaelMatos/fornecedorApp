from django.contrib import admin

# Register your models here.
from .models import Fornecedor,Produto

admin.site.register(Fornecedor)
admin.site.register(Produto)