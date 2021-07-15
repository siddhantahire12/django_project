from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostModel(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now_add =True)
	updated_at = models.DateTimeField(auto_now=True)

