from django.db import models
from .client import Client
from core.models import AbstractContact


class Contact(AbstractContact):
    client = models.ForeignKey(verbose_name='Клиент',
                               to=Client,
                               on_delete=models.CASCADE,
                               related_name='contacts')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
