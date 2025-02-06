from rest_framework import serializers
from .models import UserRegister


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserRegister
        fields = ["email","first_name","last_name","phone_number","address","role","password"]

    
    def create(self, validated_data):
        user = UserRegister.objects.create(
            email = validated_data["email"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            phone_number = validated_data["phone_number"],
            address = validated_data["address"],
            role = validated_data["role"],
            password = validated_data["password"]
        )
        return user
    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)