from rest_framework import serializers

from core.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    """Serializer for tags objects"""

    class Meta:
        model = Vehicle
        fields = ('id', 'modelo', 'marca', 'placa', 'cor', 'chassi',
                  'ano_fabricacao', 'valor_compra', 'valor_venda',
                  'data_compra', 'data_venda')
        read_only_fields = ('id',)

    modelo = serializers.CharField(max_length=255)
    marca = serializers.CharField(max_length=255)
    placa = serializers.CharField(max_length=10)
    cor = serializers.CharField(max_length=255)
    chassi = serializers.CharField(max_length=255)
    ano_fabricacao = serializers.ChoiceField(choices=list(range(1940, 2021)))
    valor_compra = serializers.DecimalField(max_digits=8, decimal_places=2)
    valor_venda = serializers.DecimalField(max_digits=8, decimal_places=2)
    data_compra = serializers.DateTimeField()
    data_venda = serializers.DateTimeField()

