from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from .models import Category, Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


class CategoryCreateView(LoginRequiredMixin,  CreateView,  ):
    model = Category
    template_name = 'products/category_new.html'
    fields = ['categoryName']
    success_url = '/products/menu-product/'
    


class ProductCreateView(LoginRequiredMixin,  CreateView, ):
    model = Product
    template_name = 'products/product_new.html'
    fields = ['productName', 'description', 'price', 'image', 'category']
    # success_url = '/products/menu-product/'
    success_url = '/products/list-product/'


class MenuProducts(LoginRequiredMixin, LoginView, ):
    template_name = 'products/menu_products.html'

class ProductsView (ListView):
    template_name = 'products/products_view.html'
    model = Product
    context_object_name = 'products'
    
    