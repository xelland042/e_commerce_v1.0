from django.db import models


class CategoryManager(models.Manager):
    def parent_category(self):
        return super().get_queryset().filter(parent_category=None)

    def child_categories(self, parent_slug):
        children = super().get_queryset().filter(parent_category__slug=parent_slug)
        return children


class ProductManager(models.Manager):
    def cheap_product_only(self):
        cheap = super().get_queryset().all()
        return None
