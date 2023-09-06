from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Chef
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CreateChefView(LoginRequiredMixin,CreateView):
    model = Chef
    template_name = 'chefs/create_chef_view.html'
    fields = ['name', 'designation', 'facebook_url', 'twitter_url','linkedin_url', 'image']
    success_url = '/products/menu-product/'
    
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class ListChefsView(ListView):
    model = Chef
    template_name= 'chefs/team.html'
    fields = ['name', 'designation', 'facebook_url', 'twitter_url','linkedin_url', 'image']
    