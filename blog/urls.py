from django.urls import path
from .views import CreateBlogView

urlpatterns = [
    path('new-comment/', CreateBlogView.as_view(), name='new_comment')
]
