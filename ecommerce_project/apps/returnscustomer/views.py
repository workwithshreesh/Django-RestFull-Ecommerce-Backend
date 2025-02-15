
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from returnscustomer.models import ReturnProducts, ReturnedRequestProduct
from returnscustomer.serializer import (ReturnProductSerializer, 
                                        ReturnedRequestProductSerializer,
                                        ReturnRequestOfSingleUser)



class ReturnedRequestView(APIView):
    def post(self, request):
        serializer_class = ReturnedRequestProductSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_201_CREATED)
    
    
    def get(self, request, pk=None):
        if pk:
            try:
                return_product = ReturnedRequestProduct.objects.get(pk=pk)
            except ReturnedRequestProduct.DoesNotExist:
                return Response({"error":"return product not found"},status=status.HTTP_400_BAD_REQUEST)
            
            serializer = ReturnRequestOfSingleUser(return_product,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return_product = ReturnedRequestProduct.objects.all()
        serializer = ReturnedRequestProductSerializer(return_product,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def patch(self, request, pk):
        try:
            return_product = ReturnedRequestProduct.objects.get(pk=pk)
        except ReturnedRequestProduct.DoesNotExist:
            return Response({"message":"Data not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ReturnedRequestProductSerializer(return_product,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)






# return product
class ReturnedProduct(APIView):
    def post(self, request):
        serializer_class = ReturnProductSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            try:
                return_product = ReturnProducts.objects.get(pk=pk)
            except ReturnProducts.DoesNotExist:
                return Response({"error":"returned product"}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = ReturnProductSerializer(return_product,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        returned_product = ReturnProducts.objects.all()
        serializer = ReturnProductSerializer(returned_product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def patch(self, request, pk):
        try:
            returned_product = ReturnProducts.objects.get(pk=pk)
        except:
            return Response({"error":"Data is not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ReturnProductSerializer(returned_product,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        