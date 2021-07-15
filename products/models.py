from django.db import models

# Create your models here.

class ProductModel(models.Model):
	name = models.CharField(max_length=50)
	weight = models.CharField(max_length=5)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	