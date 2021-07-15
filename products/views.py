from django.shortcuts import render,redirect
from .models import ProductModel

# Create your views here.
def products(request):
	if request.user.is_authenticated:
		data = ProductModel.objects.all()
		return render (request,"products.html",{'data':data})
	else:
		return redirect("ulogin")