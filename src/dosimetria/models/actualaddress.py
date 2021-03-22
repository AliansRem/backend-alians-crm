from django.db import models
from .client import Client
from core.models import AbstractAddress


class ActualAddress(AbstractAddress):
    client = models.ForeignKey(verbose_name='Клиент',
                               to=Client,
                               on_delete=models.CASCADE,
                               related_name='actual_addresses')

    class Meta:
        verbose_name = 'Физический адрес'
        verbose_name_plural = 'Физические адреса'
