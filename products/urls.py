from django.urls import path

from products.views import BaseCategoryProductView, ProductDetailView, ChildCategoryView, CartView

urlpatterns = [
    path('main/', BaseCategoryProductView.as_view()),
    path('main/<int:product_id>', ProductDetailView.as_view()),
    path('main/<slug:slug>', ChildCategoryView.as_view()),
    path('main/cart/', CartView.as_view()),
]
