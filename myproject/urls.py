"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from .views import (
    CategoryCreateView, ProductCreateView,
    CategoryListView, ProductListView,
    CategoryDetailView, ProductDetailView,
    CategoryUpdateView, ProductUpdateView,
    CategoryDeleteView, ProductDeleteView,
    CategoryViewSet, ProductViewSet
)

# router = DefaultRouter()
# router.register(r'category', CategoryViewSet)
# router.register(r'products', ProductViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('category/', TemplateView.as_view(template_name='category.html'),
    #      name='category'),
    # path('product/', TemplateView.as_view(template_name='product.html'), name='product'),

    # Create
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),

    # Read
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('product/', ProductListView.as_view(), name='product-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Update
    path('category/<int:pk>/update/',
         CategoryUpdateView.as_view(), name='category-update'),
    path('product/<int:pk>/update/',
         ProductUpdateView.as_view(), name='product-update'),

    # Delete
    path('category/<int:pk>/delete/',
         CategoryDeleteView.as_view(), name='category-delete'),
    path('product/<int:pk>/delete/',
         ProductDeleteView.as_view(), name='product-delete'),
]
