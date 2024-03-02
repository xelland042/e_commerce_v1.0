from django.core.cache import cache
from datetime import timedelta

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.response import Response

from products.models import Product, Category, Image, Specification
from products.serializers import BaseCategorySerializer, MainProductSerializer, DetailProductSerializer, \
    OrderSerializer, OrderCreateSerializer


class BaseCategoryProductView(APIView):
    def get(self, request, format=None):
        parent_categories = Category.objects.parent_category()
        parent_serializer = BaseCategorySerializer(parent_categories, many=True)
        top_products = Product.objects.all()
        product_serializer = MainProductSerializer(top_products, many=True)
        data = {'categories': parent_serializer.data, 'products': product_serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OrderCreateSerializer)
    def post(self, request, format=None):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            spec_id = int(serializer.data['products_specification'])
            prod_spec = Specification.objects.get(id=spec_id)
            prod_spec.quantity = prod_spec.quantity - int(serializer.data['quantity'])
            prod_spec.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    def get(self, request, product_id, format=None):
        product = Product.objects.get(id=product_id)
        serializer = DetailProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ChildCategoryView(APIView):
    def get(self, request, slug, format=None):
        child_categories = Category.objects.child_categories(slug)
        parent_category = Category.objects.get(slug=slug)
        main_categories_serializer = BaseCategorySerializer(parent_category)
        categories_serializer = BaseCategorySerializer(child_categories, many=True)
        data = {'main_category': main_categories_serializer.data['name'], 'categories': categories_serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)


class CartView(APIView):
    def get(self, request, format=None):
        cart_data = cache.get('cart_data')

        if cart_data is not None:
            return Response(cart_data, status=status.HTTP_200_OK)
        else:
            return Response("Cart data not found", status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_OBJECT,
                                 properties={'specification': openapi.Schema(type=openapi.TYPE_INTEGER)})
        )
    )
    def post(self, request, format=None):
        data = request.data
        cache.set('cart_data', data, timeout=60 * 60)

        return Response(request.data, status=status.HTTP_200_OK)
