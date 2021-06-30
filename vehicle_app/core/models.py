from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def max_value_current_year(value):
    return MaxValueValidator(datetime.date.today().year)(value)


def year_choices():
    return [(r, r) for r in range(1940, datetime.date.today().year+1)]


class Vehicle(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    placa = models.CharField(max_length=20)
    cor = models.CharField(max_length=10)
    chassi = models.CharField(max_length=255)
    ano_fabricacao = models.IntegerField('ano_fabricacao', validators=[
        MinValueValidator(1940), max_value_current_year])
    valor_compra = models.DecimalField(decimal_places=2, max_digits=8)
    valor_venda = models.DecimalField(decimal_places=2, max_digits=8,
                                      blank=True, null=True)
    data_compra = models.DateField()
    data_venda = models.DateField(blank=True, null=True)

