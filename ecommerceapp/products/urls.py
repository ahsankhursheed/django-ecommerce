from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage , name="homepage"),
    path('products-listings/', views.products_listings , name="products_listings"),
    path('<int:product_id>/', views.product_details , name="product_details"),
]