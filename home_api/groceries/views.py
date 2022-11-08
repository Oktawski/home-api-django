from typing import List
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request: HttpRequest):
    user_id = request.user.id

    categories = Category.objects.all()
    products = Product.objects.all()

    categories_serialized = CategorySerializer(categories, many=True)
    products_serialized = ProductSerializer(products, many=True)

    message = categories_serialized.data + products_serialized.data

    return Response(message)


