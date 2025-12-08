from django.urls import path
from .views import getRoutes, getProjects

urlpatterns = [
    path('api/', getRoutes, name='getRoutes'),
    path('api/projects/', getProjects, name='getProjects'),
]