from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework import status
from orders.models import (
    Order,
    OrderItem
)
from orders.serializer import (
    OrderProduct,
    OrderItem,
    OrderItemFullDataShow,
    OrderItemProductShow,
    OrderProductShow
)




class Order(APIView):
    def post(self, request):
        serializer_class = OrderProduct(data=request.data)
        if serializer_class.is_valid():
            serializer_class.savve()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self,request,pk=None):
        if pk:
            try:
                ordered = Order.objects.get(pk=pk)
            except Order.DoesNotExist:
                return Response({"error":"Order is not avalable"}, status=status.HTTP_400_BAD_REQUEST)
            
            
            serializer = OrderProductShow(ordered,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        ordered = Order.objects.all()
        serializer = OrderProductShow(ordered, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    def put(self, request, pk):
        try:
            ordered = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error":"order is not avilable"},status=status.HTTP_400_BAD_REQUEST)
        
        serializer = OrderProduct(ordered,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    
    
