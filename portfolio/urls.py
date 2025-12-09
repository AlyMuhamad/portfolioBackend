from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import getRoutes, getProjects, getProject

urlpatterns = [
    path('api/', getRoutes, name='getRoutes'),
    path('api/projects/', getProjects),
    path('api/project/<str:id>/', getProject),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)