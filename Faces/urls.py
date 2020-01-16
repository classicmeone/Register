from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    
    path("", views.index, name="home"),
    path("formpage", views.loadform, name="formpage"),
    path("search", views.search, name="search"), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}) 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)