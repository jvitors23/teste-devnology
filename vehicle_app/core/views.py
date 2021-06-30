from django.shortcuts import render
from django.db.models import Sum
import datetime

from core.models import Vehicle
from api.serializers import VehicleSerializer


PORCENTAGEM_COMISSAO = 0.1


def home(request):
    ultimas_vendas = Vehicle.objects.all().filter(
        data_venda__isnull=False).order_by('data_venda')

    total_compras = float(Vehicle.objects.all().aggregate(Sum('valor_compra'))[
        'valor_compra__sum'])
    total_vendas = float(Vehicle.objects.all().aggregate(Sum('valor_venda'))[
        'valor_venda__sum'])
    lucro_prejuizo_total = float(total_vendas - total_compras)
    total_comissoes = total_vendas * PORCENTAGEM_COMISSAO

    serializer = VehicleSerializer(ultimas_vendas, many=True)
    ultimas_vendas = serializer.data
    for vehicle in ultimas_vendas:
        vehicle['lucro_prejuizo'] = "{:.2f}".format(
            float(vehicle['valor_venda']) - float(vehicle['valor_compra']))
        vehicle['comissao'] = "{:.2f}".format(PORCENTAGEM_COMISSAO * float(
            vehicle['valor_venda']))
    if len(ultimas_vendas) > 5:
        ultimas_vendas = ultimas_vendas[0:5]
    total_compras = "{:.2f}".format(total_compras)
    total_vendas = "{:.2f}".format(total_vendas)
    lucro_prejuizo_total = "{:.2f}".format(lucro_prejuizo_total)
    total_comissoes = "{:.2f}".format(total_comissoes)
    return render(request, 'dashboard.html', {'ultimas_vendas':
                                                  ultimas_vendas,
                                              'total_compras': total_compras,
                                              'total_vendas': total_vendas,
                                              'lucro_prejuizo_total':
                                                  lucro_prejuizo_total,
                                              'total_comissoes':
                                                   total_comissoes,
                                              })


def veiculos(request):
    year_options = list(range(datetime.date.today().year, 1940, -1))
    vehicles = Vehicle.objects.all().filter(data_venda__isnull=True)
    serializer = VehicleSerializer(vehicles, many=True)
    vehicles = serializer.data
    return render(request, 'veiculos.html', {'vehicles': vehicles,
                                             'year_options': year_options})


def vendas(request):
    year_options = list(range(datetime.date.today().year, 1940, -1))
    vehicles = Vehicle.objects.all().filter(data_venda__isnull=False)
    serializer = VehicleSerializer(vehicles, many=True)
    vehicles = serializer.data
    for vehicle in vehicles:
        vehicle['lucro_prejuizo'] = "{:.2f}".format(
            float(vehicle['valor_venda']) - float(vehicle['valor_compra']))
    return render(request, 'vendas.html', {'vehicles': vehicles,
                                           'year_options': year_options})
