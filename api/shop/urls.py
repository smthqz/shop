from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
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
    path('', include(router.urls)),
]