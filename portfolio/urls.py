from django.urls import path
from .views import index

urlpatterns = [
    path('api/projects', index, name='home'),
]