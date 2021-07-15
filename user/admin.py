from django.contrib import admin
from .models import PostModel



# Register your models here
class PostAdmin(admin.ModelAdmin):
	list_display= ('text','created_at','updated_at','user')
	list_filter=('created_at','updated_at')
admin.site.register(PostModel,PostAdmin)