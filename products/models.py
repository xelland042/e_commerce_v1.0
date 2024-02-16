from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from products.manager import CategoryManager, ProductManager


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    base_specifications = models.JSONField(blank=True, null=True)

    objects = CategoryManager()

    def __str__(self):
        return f'{self.id} - {self.name} - {self.parent_category is not None}'


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    about_product = models.TextField()
    in_discount = models.BooleanField(default=False)
    discount_percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    objects = ProductManager()

    def __str__(self):
        return f'{self.name}'


class Image(BaseModel):
    place = models.IntegerField()
    main_image = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.place} - {self.main_image}'


class Specification(BaseModel):
    specification = models.JSONField()
    quantity = models.BigIntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=3)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')

    def __str__(self):
        return f'{self.product.name} - {self.price} - {self.quantity}'
