from django.http.response import HttpResponse
from rest_framework import serializers, status
from rest_framework.response import Response
from product.models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ProductList(ListCreateAPIView):
    queryset = Product.objects.using('postgres').all()
    serializer_class = ProductSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)                 
        if serializer.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)   # successfully CREATED
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # invalid data
    
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.using('postgres').all()
    serializer_class = ProductSerializer
    lookup_field        = 'id'                                      # set the lookup field to id

    def retrieve(self, request, *args, **kwargs):
        try:                                                        # try to get the product
            product = Product.objects.using('postgres').get(id=id)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)   # if not found, return 404
        
        serializer = ProductSerializer(product)                     # serialize the product
        return Response(serializer.data)                            # return the serialized product
    
    
    def update(self, request, *args, **kwargs):
        try:                                                        # try to get the product
            product = Product.objects.using('postgres').get(id=id)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data)  # convert complex data by passing into serializer 
        
        if serializer.is_valid():                                   # check for validation of data
            serializer.save()
            return Response(serializer.data)                        # return updated the JSON response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # return error for invalid data


    def delete(self, request, *args, **kwargs):
        try:
            product = Product.objects.using('postgres').get(id=id)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)  # return 404 if not found
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)         # return 204 if deleted