from django.urls import path

from shop.views import *

urlpatterns = [
    path('products/', getAllProducts),
    path('product/<str:pk>', getProduct),
    path('category/', getAllCategory),
    path('category/<str:pk>', getCategory),
    path('subcategory/all/', getAllSubCategory),
  #  path('products/', views.ProductsAPIList.as_view(), name='products'),
   # path('products/<str:pk>/', views.ProductsAPIDetailView.as_view(), name='product'),
   # path('info/', views.AdminAPIDetail.as_view(), name='info'),
    #path('category/', views.SubCategoryAPIList.as_view(), name='category'),
   # path('category/<str:pk>/', views.SubCategoryAPIDetail.as_view(), name='category_detail'),
   # path('cart/', views.CartAPIList.as_view(), name='cart'),
   # path('cart/<str:pk>/', views.CartAPIDetail.as_view(), name='cart_detail'),
   # path('order/', views.OrderAPIList.as_view(), name='order'),
  #  path('name/', views.CategoryAPIList.as_view(), name='name'),

]