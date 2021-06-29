from django.urls import path


from . import views

urlpatterns = [
    path('', views.home),
    path('veiculos', views.veiculos),
    path('vendas', views.vendas),

]

