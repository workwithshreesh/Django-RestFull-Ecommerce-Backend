from rest_framework import serializers
from products.models import Products, ProductCategory, WishList
from users.serializer import UserRegisterSellerSerializer

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["Category_Name",]

class ProductSellerSerializerGet(serializers.ModelSerializer):
    category_name = serializers.CharField(source="Category.Category_Name")
    Seller = UserRegisterSellerSerializer(read_only=True)
    class Meta:
        model = Products
        fields = ["Product_Id","Product_Name","Product_Description",
                  "Product_Price","Product_Stock_Quantity","Product_Image",
                  "category_name","Seller","Is_Active"]
        

class ProductSellerBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["Product_Id","Product_Name","Product_Description",
                  "Product_Price","Product_Stock_Quantity","Product_Image",
                  "Category","Seller","Is_Active"]
        
    

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ["user","product"]
