from rest_framework import serializers

from products.models import Product, Category, Image, Specification, Order


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class BaseSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ('price',)


class DetailProductSpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ('id', 'specification', 'quantity', 'price')


class MainProductSerializer(serializers.ModelSerializer):
    specifications = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'specifications')

    def get_specifications(self, instance):
        specification = instance.specifications.all().order_by('price').first()
        return BaseSpecificationSerializer(specification).data


class DetailProductSerializer(serializers.ModelSerializer):
    specifications = DetailProductSpecificationsSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['quantity', 'products_specification', 'address']
