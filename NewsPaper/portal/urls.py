from django.urls import path
from .views import (
    ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete, ProductSearch
)

urlpatterns = [
    path('', ProductsList.as_view(), name='product_list'),
    path('news/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('news/create/', ProductCreate.as_view(), name='product_create'),
    path('news/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('news/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('articles/create/', ProductCreate.as_view(), name='product_create'),
    path('articles/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('articles/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('search', ProductSearch.as_view(), name='product_search'),
]