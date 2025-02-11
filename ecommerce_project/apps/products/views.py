from rest_framework import generics
from products.models import Products, ProductCategory
from products.serializer import (ProductSellerSerializerGet, 
                                 ProductSellerBuyerSerializer, 
                                 ProductCategorySerializer)

class ProductApiView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    

    def get_serializer_class(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "role") and (self.request.user.role == "SELLER"):
            if (self.request.method == "GET"):
                return ProductSellerSerializerGet
            if (self.request.method == "POST"):
                    return ProductSellerBuyerSerializer
            else:
                return ProductSellerBuyerSerializer

        return ProductSellerBuyerSerializer


class ProductUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSellerBuyerSerializer
    lookup_field = "pk"


class ProductCategoryApiView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer