from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls.static import static
from vehicle_app import settings

from . import views

urlpatterns = [
    path('', views.home),
    path('veiculos', views.veiculos),
    path('login', views.login),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
