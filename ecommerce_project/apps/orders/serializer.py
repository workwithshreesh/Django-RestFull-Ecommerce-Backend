from rest_framework import serializers
from orders.models import (
    Order,
    OrderItem
)
from products.serializer import ProductSellerSerializerGet
from users.serializer import UserRegisterSellerSerializer

class OrderProduct(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        

class OrderProductShow(serializers.ModelSerializer):
    user = UserRegisterSellerSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = [
            "user","status", "total_price", "created_at"
        ]
        

class OrderItemProductShow(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        
        
class OrderItemFullDataShow(serializers.ModelSerializer):
    order = OrderProductShow(many=True, read_only=True)
    product = ProductSellerSerializerGet(many=True, read_only=True)
    class Meta:
        model = OrderItem
        fields = [
            "order", "product", "quantity", "price"
        ]