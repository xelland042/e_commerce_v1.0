from django.urls import path

from products.views import BaseCategoryProductView, ProductDetailView, ChildCategoryProductView

urlpatterns = [
    path('main/', BaseCategoryProductView.as_view()),
    path('main/<int:product_id>', ProductDetailView.as_view()),
    path('main/<slug:slug>', ChildCategoryProductView.as_view()),
]
