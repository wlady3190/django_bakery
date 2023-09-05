from django.urls import path, include
from .views import SignUpView


urlpatterns = [
    path('signup', 'django.contrib.auth.urls'), 
    path('signup/', SignUpView.as_view(), name='signup'),
]

