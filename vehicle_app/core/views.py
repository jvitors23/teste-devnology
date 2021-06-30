from django.shortcuts import render
from django.db.models import Sum
import datetime
from datetime import timedelta

from core.models import Vehicle
from api.serializers import VehicleSerializer


PORCENTAGEM_COMISSAO = 0.1


def home(request):
    last_month = request.GET.get('last_month', 0)
    last_month_date = datetime.datetime.today() - timedelta(days=30)
    if int(last_month) == 1:
        compras = Vehicle.objects.all().filter(
            data_compra__gte=last_month_date)
        vendas = Vehicle.objects.all().filter(
            data_venda__isnull=False).filter(
            data_venda__gte=last_month_date)
    else:
        compras = Vehicle.objects.all()
        vendas = Vehicle.objects.all().filter(data_venda__isnull=False)

    total_compras = compras.aggregate(Sum('valor_compra'))[
        'valor_compra__sum']
    if total_compras is None:
        total_compras = 0
    total_compras = float(total_compras)

    total_vendas = vendas.aggregate(Sum('valor_venda'))[
        'valor_venda__sum']
    if total_vendas is None:
        total_vendas = 0
    total_vendas = float(total_vendas)

    lucro_prejuizo_total = float(total_vendas - total_compras)

    serializer = VehicleSerializer(vendas, many=True)
    vendas = serializer.data
    total_comissoes = 0
    lucro_prejuizo_venda = 0
    for vehicle in vendas:
        lucro_prejuizo_venda += float(vehicle['valor_venda']) - \
                                 float(vehicle['valor_compra'])
        if lucro_prejuizo_venda > 0:
            total_comissoes += lucro_prejuizo_venda * PORCENTAGEM_COMISSAO

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
        if float(vehicle['lucro_prejuizo']) > 0:
            vehicle['comissao'] = float(vehicle['lucro_prejuizo']) * \
                                  PORCENTAGEM_COMISSAO
        else:
            vehicle['comissao'] = 0
    return render(request, 'vendas.html', {'vehicles': vehicles,
                                           'year_options': year_options})
