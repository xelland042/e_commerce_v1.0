from rest_framework import serializers

from products.models import Product, Category, Image, Specification


class BaseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class BaseSpecificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specification
        fields = ('price',)


class MainProductSerializer(serializers.ModelSerializer):
    specifications = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'specifications')

    def get_specifications(self, instance):
        specification = instance.specifications.all().order_by('price').first()
        return BaseSpecificationSerializer(specification).data


class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
