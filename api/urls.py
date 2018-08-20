from django.urls import path

from .views import (
    BadRequestView, ProductCreateView, ProductDeleteView,
    ProductDetailsView, ProductListView,
)


urlpatterns = [
    path('bad_request/', BadRequestView.as_view(), name='bad_request'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
