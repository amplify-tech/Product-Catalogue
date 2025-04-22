from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


@api_view(['POST'])
def product_search(request):
    data = request.data
    price = data.get("price")
    location = data.get("location")
    bedroomCount = data.get("bedroomCount")
    
    productObjects = Product.objects.filter(price=price, 
                            location=location,
                            bedroomCount=bedroomCount
                            ).all()
    productList = ProductSerializer(productObjects, many=True)
    return Response(productList.data, status=status.HTTP_200_OK)
   
@api_view(['POST'])
def product_create(request):
    newProduct = ProductSerializer(data=request.data)
    if newProduct.is_valid():
        newProduct.save()
        return Response(newProduct.data, status=status.HTTP_201_CREATED)
    return Response(newProduct.errors, status=status.HTTP_400_BAD_REQUEST)
   