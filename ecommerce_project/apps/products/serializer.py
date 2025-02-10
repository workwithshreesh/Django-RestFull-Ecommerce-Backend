from rest_framework import serializers
from .models import Products

class ProductSerializerGet(serializers.ModelSerializer):
    Seller = serializers.CharField("Seller.email")
    class Meta:
        model = Products
        fields = ["Product_Id","Product_Name","Product_Description",
                  "Product_Price","Product_Stock_Quantity","Product_Image",
                  "Category","Seller","Is_Active"]
        

class ProductSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["Product_Id","Product_Name","Product_Description",
                  "Product_Price","Product_Stock_Quantity","Product_Image",
                  "Category","Seller","Is_Active"]