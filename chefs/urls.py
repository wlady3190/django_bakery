from django.urls import path
from .views import CreateChefView, ListChefsView

urlpatterns = [
    path('', ListChefsView.as_view(), name='team' ), 
    path('create/', CreateChefView.as_view(), name='create_chef' ),
    
]
