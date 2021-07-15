from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
	class Meta:
		model = ProductModel
		fields = ["name","weight"]
		
		
		
		widgets = {'name':forms.TextInput(),
			'weight':forms.NumberInput(attrs={"step":"any","min":0})
			}