from rest_framework import serializers
import datetime
from core.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    """Serializer for vehicles objects"""

    modelo = serializers.CharField(max_length=255)
    marca = serializers.CharField(max_length=255)
    placa = serializers.CharField(max_length=10)
    cor = serializers.CharField(max_length=255)
    chassi = serializers.CharField(max_length=255)
    ano_fabricacao = serializers.ChoiceField(choices=list(range(1940,
                                             datetime.date.today().year)))
    valor_compra = serializers.DecimalField(max_digits=8, decimal_places=2)
    valor_venda = serializers.DecimalField(max_digits=8, decimal_places=2,
                                           required=False)
    data_compra = serializers.DateField()
    data_venda = serializers.DateField(required=False)

    class Meta:
        model = Vehicle
        fields = ('id', 'modelo', 'marca', 'placa', 'cor', 'chassi',
                  'ano_fabricacao', 'valor_compra', 'valor_venda',
                  'data_compra', 'data_venda')
        read_only_fields = ('id',)

    def create(self, validated_data):
        validated_data['data_compra'] = validated_data[
            'data_compra'].strftime('%Y-%m-%d')
        validated_data['placa'] = validated_data['placa'].upper()
        return Vehicle.objects.create(**validated_data)

