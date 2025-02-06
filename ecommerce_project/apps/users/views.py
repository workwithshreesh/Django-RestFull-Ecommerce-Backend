from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegister(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.validate_data['email']
            password = serializer.validate['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token


                return Response({
                    "refresh":str(refresh.token),
                    "access":str(access_token),
                    "login": "Login Successful"
                }, status=status.HTTP_200_OK);
            return Response({"message":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
