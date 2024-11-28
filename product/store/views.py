from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from store.models import Product
from store.serializer import ProductSerializer

#Product view
@api_view(['GET'])
def getProduct(request):
    product = Product.objects.all()
    pdata = ProductSerializer(product, many=True).data
    return Response(pdata)
    
