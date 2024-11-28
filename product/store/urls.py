from django.urls import path

from .views import getProduct

urlpatterns = [
    path('product/', getProduct, name='getProduct'),
]
