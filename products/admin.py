from django.contrib import admin
from products.models import Product, Image, Specification, Category


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, SpecificationInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Specification)
admin.site.register(Category)
