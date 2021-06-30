from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('veiculos', views.VehicleViewset)

app_name = 'api'

urlpatterns = [
    path('profits/', views.ProfitsInfo.as_view()),
    path('', include(router.urls)),
]
