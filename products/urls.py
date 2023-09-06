from django.urls import path, include
from . import views
from django.contrib import admin



urlpatterns = [
    # path('menu-product/', views.MenuProducts, name='menu_products' ) ,
    path('', views.productsByCategoryView, name='menu'),
    path('menu-product/', views.MenuProducts.as_view(), name='menu_products' ) ,  
    path('new-category/', views.CategoryCreateView.as_view(), name='new_category' ),
    path('list-product/', views.ProductsView.as_view(), name='product_list' ),
    path('new-product/', views.ProductCreateView.as_view(), name='new_product' ),
    path('update-product/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product' ),
    path('delete_product/<int:pk>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('products/', include('django.contrib.auth.urls')),
]
