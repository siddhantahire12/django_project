from django.contrib import admin
from .models import ProductModel
from .forms import ProductForm

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	form = ProductForm
	list_display = ('name','weight','created_at','updated_at')
	list_filter= ('created_at','updated_at') 

	
admin.site.register(ProductModel,ProductAdmin)