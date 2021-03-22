from django.db import models
from .client import Client
from .quarter import Quarter


class Protocol(models.Model):
    client = models.ForeignKey(verbose_name='Клиент',
                               to=Client,
                               on_delete=models.PROTECT,
                               related_name='protocols')

    quarter = models.ForeignKey(verbose_name='Квартал',
                                to=Quarter,
                                on_delete=models.CASCADE)

    number = models.CharField(verbose_name='Номер',
                              max_length=16,
                              unique=True)

    class Meta:
        verbose_name = 'Протокол'
        verbose_name_plural = 'Протоколы'
