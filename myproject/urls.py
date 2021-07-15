
from django.contrib import admin
from django.urls import path
from user.views import ulogin,ulogout,home,register,create,update_post,edit,delete,profile
from products.views import products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ulogin/',ulogin,name="ulogin"),
    path('ulogout/',ulogout,name="ulogout"),
    path('register/',register,name="register"),
    path('',home,name="home"),
    path('create/',create,name="create"),
    path("edit/<int:id>",edit,name="edit"),
    path("update_post/",update_post,name="update_post"),
    path("delete/<int:id>",delete,name="delete"),
    path("products/",products,name="products"),
    path("profile/",profile,name="profile"),
]
