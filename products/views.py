from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product, Category, Image, Specification
from products.serializers import BaseCategorySerializer, MainProductSerializer, DetailProductSerializer


class BaseCategoryProductView(APIView):
    def get(self, request, format=None):
        parent_categories = Category.objects.parent_category()
        parent_serializer = BaseCategorySerializer(parent_categories, many=True)
        top_products = Product.objects.all()
        product_serializer = MainProductSerializer(top_products, many=True)
        data = {'categories': parent_serializer.data, 'products': product_serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    def get(self, request, product_id, format=None):
        product = Product.objects.get(id=product_id)
        serializer = DetailProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ChildCategoryProductView(APIView):
    def get(self, request, slug, format=None):
        child_categories = Category.objects.child_categories(slug)
        parent_category = Category.objects.get(slug=slug)
        main_categories_serializer = BaseCategorySerializer(parent_category)
        categories_serializer = BaseCategorySerializer(child_categories, many=True)
        data = {'main_category': main_categories_serializer.data['name'], 'categories': categories_serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)
