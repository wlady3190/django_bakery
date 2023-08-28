from django.urls import path
from .views import about, contact, home, menu, service, team, testimonial



urlpatterns = [
    path('', home, name='home_core'),
    path('about/', about, name='about_core'),
    path('contact/', contact, name='contact_core'),
    path('menu/', menu, name='menu_core'),
    path('service/', service, name='service_core'),
    path('team/', team, name='team_core'),
    path('testimonial/', testimonial, name='testimonial_core'),
    

    
    
]
