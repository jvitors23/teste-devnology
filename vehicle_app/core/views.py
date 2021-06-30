import datetime

from api.serializers import VehicleSerializer
from api.views import get_profits_info
from core.models import Vehicle
from django.shortcuts import render

PORCENTAGEM_COMISSAO = 0.1


def dashboard(request):
    """Render 'Dashboard' page"""
    last_month = int(request.GET.get('last_month', 0)) == 1
    profits_info = get_profits_info(last_month)

    all_vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(all_vehicles, many=True)
    all_vehicles = serializer.data
    for vehicle in all_vehicles:
        if vehicle['data_venda'] is not None:
            vehicle['status'] = 'Vendido'
        else:
            vehicle['status'] = 'Disponível'

    ultimas_vendas = Vehicle.objects.all().filter(
        data_venda__isnull=False).order_by('data_venda')

    serializer = VehicleSerializer(ultimas_vendas, many=True)
    ultimas_vendas = serializer.data
    for vehicle in ultimas_vendas:
        vehicle['lucro_prejuizo'] = "{:.2f}".format(
            float(vehicle['valor_venda']) - float(vehicle['valor_compra']))
        if float(vehicle['lucro_prejuizo']) > 0:
            vehicle['comissao'] = "{:.2f}".format(PORCENTAGEM_COMISSAO * float(
                vehicle['lucro_prejuizo']))
        else:
            vehicle['comissao'] = "{:.2f}".format(0)
    if len(ultimas_vendas) > 5:
        ultimas_vendas = ultimas_vendas[0:5]

    return_object = profits_info
    return_object['all_vehicles'] = all_vehicles
    return_object['ultimas_vendas'] = ultimas_vendas
    return render(request, 'dashboard.html', return_object)


def veiculos(request):
    """Render 'Veículos' page"""
    year_options = list(range(datetime.date.today().year, 1940, -1))
    available_vehicles = Vehicle.objects.all().filter(data_venda__isnull=True)
    serializer = VehicleSerializer(available_vehicles, many=True)
    available_vehicles = serializer.data

    return render(request, 'veiculos.html', {
        'available_vehicles': available_vehicles,
        'year_options': year_options})


def vendas(request):
    """Render 'Vendas' page"""
    year_options = list(range(datetime.date.today().year, 1940, -1))
    vehicles = Vehicle.objects.all().filter(data_venda__isnull=False)
    serializer = VehicleSerializer(vehicles, many=True)
    vehicles = serializer.data
    for vehicle in vehicles:
        vehicle['lucro_prejuizo'] = "{:.2f}".format(
            float(vehicle['valor_venda']) - float(vehicle['valor_compra']))
        if float(vehicle['lucro_prejuizo']) > 0:
            vehicle['comissao'] = float(vehicle['lucro_prejuizo']) * \
                                  PORCENTAGEM_COMISSAO
        else:
            vehicle['comissao'] = 0
    return render(request, 'vendas.html', {'vehicles': vehicles,
                                           'year_options': year_options})
