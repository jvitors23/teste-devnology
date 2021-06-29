from django.shortcuts import render

from core.models import Vehicle
from api.serializers import VehicleSerializer


PORCENTAGEM_COMISSAO = 0.1


def home(request):
    ultimas_vendas = Vehicle.objects.all().filter(
        data_venda__isnull=False).order_by('data_venda')
    serializer = VehicleSerializer(ultimas_vendas, many=True)
    ultimas_vendas = serializer.data
    for vehicle in ultimas_vendas:
        vehicle['lucro_prejuizo'] = float(vehicle['valor_venda']) - float(
            vehicle[
            'valor_compra'])
        vehicle['comissao'] = PORCENTAGEM_COMISSAO * float(vehicle['valor_venda'])
    if len(ultimas_vendas) > 5:
        ultimas_vendas = ultimas_vendas[0:5]
    return render(request, 'dashboard.html', {'ultimas_vendas':
                                                  ultimas_vendas})


def veiculos(request):
    vehicles = Vehicle.objects.all().filter(data_venda__isnull=True)
    serializer = VehicleSerializer(vehicles, many=True)
    vehicles = serializer.data
    return render(request, 'veiculos.html', {'vehicles': vehicles})


def vendas(request):
    vehicles = Vehicle.objects.all().filter(data_venda__isnull=False)
    serializer = VehicleSerializer(vehicles, many=True)
    vehicles = serializer.data
    for vehicle in vehicles:
        vehicle['lucro_prejuizo'] = float(vehicle['valor_venda']) - float(
            vehicle[
            'valor_compra'])
    return render(request, 'vendas.html', {'vehicles': vehicles})
