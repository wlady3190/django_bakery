from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Comment (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author
    
    class Meta:
        ordering = ['-created']
    