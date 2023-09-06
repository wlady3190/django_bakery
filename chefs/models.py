from django.db import models

# Create your models here.

class Chef( models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default_chef.png', upload_to='chefs')
    designation = models.CharField(max_length=100)
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    linkedin_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
        
