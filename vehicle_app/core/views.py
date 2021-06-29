from django.shortcuts import render


def home(request):
    return render(request, 'dashboard.html')


def veiculos(request):
    return render(request, 'veiculos.html')


def vendas(request):
    return render(request, 'vendas.html')
