import datetime
from datetime import timedelta

from api.serializers import VehicleSerializer
from core.models import Vehicle
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

PORCENTAGEM_COMISSAO = 0.1


class VehicleViewset(viewsets.ModelViewSet):
    """Vehicle objects API"""
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


def get_profits_info(interval='begin'):

    if interval == 'month':
        begin_date = datetime.datetime.today() - timedelta(days=30)
    elif interval == 'week':
        begin_date = datetime.datetime.today() - timedelta(days=7)
    elif interval == 'semester':
        begin_date = datetime.datetime.today() - timedelta(days=180)
    else:
        interval = 'begin'

    if interval != 'begin':
        compras = Vehicle.objects.all().filter(
            data_compra__gte=begin_date)
        vendas = Vehicle.objects.all().filter(
            data_venda__isnull=False).filter(
            data_venda__gte=begin_date)
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

    total_compras = "{:.2f}".format(total_compras)
    total_vendas = "{:.2f}".format(total_vendas)
    lucro_prejuizo_total = "{:.2f}".format(lucro_prejuizo_total)
    total_comissoes = "{:.2f}".format(total_comissoes)

    return {
        'total_compras': total_compras,
        'total_vendas': total_vendas,
        'lucro_prejuizo_total':
            lucro_prejuizo_total,
        'total_comissoes':
            total_comissoes,
    }


class ProfitsInfo(APIView):
    """Profits Info data API"""

    def get(self, request):
        """Return the profits info (sales, profits, purchases)"""
        interval = request.query_params.get('interval', 'begin')
        profits_info = get_profits_info(interval)
        return Response(profits_info)
