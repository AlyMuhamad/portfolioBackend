from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import getRoutes, getProjects

urlpatterns = [
    path('api/', getRoutes, name='getRoutes'),
    path('api/projects/', getProjects, name='getProjects'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)