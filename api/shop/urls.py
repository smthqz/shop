from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework import routers
from shop.views import *
from .views import LoginAPI
from knox import views as knox_views
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('products/', getAllProducts),
    path('product/<str:pk>', getProduct),
    path('category/', getAllCategory),
    path('category/<str:pk>', getCategory),
    path('subcategory/all/', getAllSubCategory),
    path('products/popular/', getPopularProducts),
    path('products/category/<str:pk>', getProductBySubcategory),
    path('orders/', getAllOrders),
    path('products/sort/<str:s>', getProductsBySort),
    path('products/sort/down/<str:s>', getProductsBySortDown),
    path('orders/new/', OrderSet.as_view()),
    path('cart/<str:pk>', getCart),
    path('order/<str:pk>', getOrder),
    path('carts/', CartSet.as_view()),
    path('auth/', include('djoser.urls')),
    path('search/', ProductList.as_view()),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    #path('register/', RegisterAPI.as_view(), name='register'),
    #path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('users/', getAllUsers),
    path('users/<str:pk>', getUser),
    path('login/', SignInAPI.as_view()),
    path('register/', SignUpAPI.as_view()),

]