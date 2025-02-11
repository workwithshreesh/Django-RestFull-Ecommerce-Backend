from django.urls import path
from products.views import (ProductApiView, ProductUpdateApiView, 
                            ProductCategoryApiView)

urlpatterns = [
    path("show-products/",ProductApiView.as_view(),name="showProducts"),
    path("show-products/<int:pk>/",ProductUpdateApiView.as_view(),name="showProducts"),
    path("product-category/",ProductCategoryApiView.as_view(),name="product-category")
]
