from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework import routers
from shop.views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('products/', getAllProducts),
    path('product/<str:pk>', getProduct),
    path('category/', getAllCategory),
    path('category/<str:pk>', getCategory),
    path('subcategory/all/', getAllSubCategory),
    path('products/popular/', getPopularProducts),
    path('orders/', getAllOrders),
    path('orders/new/', OrderSet.as_view()),
    path('cart/<str:pk>', getCart),
    path('carts/', CartSet.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]