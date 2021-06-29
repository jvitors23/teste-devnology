from django.shortcuts import render
from core.models import Vehicle

def home(request):
    return render(request, 'dashboard.html')


def veiculos(request):
    vehicles = Vehicle.objects.all().filter(data_venda__isnull=True)
    return render(request, 'veiculos.html', {'vehicles': vehicles})


def vendas(request):
    return render(request, 'vendas.html')
