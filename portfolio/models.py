from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    stack = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='projects/')
    github = models.URLField(max_length=300, blank=True, null=True)
    site = models.URLField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.name