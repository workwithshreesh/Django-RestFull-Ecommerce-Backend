from rest_framework import serializers
from returnscustomer.models import (ReturnedRequestProduct, 
                                    ReturnProducts)
from products.serializer import ProductSellerSerializerGet

class ReturnedRequestProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnedRequestProduct
        fields = "__all__"


class ReturnProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnProducts
        fields = "__all__"


class ReturnProductSingleUser(serializers.ModelSerializer):
    class Meta:
        model = ReturnedRequestProduct
        fields = ["Return_Entry_Id","Return_Request_Id","Product_Id",
                  "Return_Status","Order_Item_Id","Product_Id",
                  "Return_Reason","Return_Status","Requested_At", "Updated_At"]



class ReturnRequestOfSingleUser(serializers.ModelSerializer):
    Return_Request_Id = ReturnedRequestProductSerializer(many=True, read_only=True)
    Product_Id = ProductSellerSerializerGet(many=True, read_only=True)
    class Meta:
        model = ReturnProducts
        fields = ["Return_Entry_Id","Return_Request_Id", "Product_Id", "RETURN_STATUS_CHOICES",
                  "Return_Status","Seller_Confirmation","Return_Quantity",
                  "Return_Remark","Confirmed_At"]
        
        