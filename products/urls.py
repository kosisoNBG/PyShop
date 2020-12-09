from django.urls import path
from . import views

#the empty string below represents the root of this app
# /products if you take away this one the rest of the dir won't work cus this is the root
# /product/1/detail
# /product/new



urlpatterns = [
    path('', views.index),
    path('new', views.new)
]