from django.db import models
from .client import Client


class Contract(models.Model):
    client = models.ForeignKey(verbose_name='Клиент',
                               to=Client,
                               on_delete=models.PROTECT,
                               related_name='contracts')
    category = models.CharField(verbose_name='Тип',
                                max_length=8,
                                choices=[
                                    ('CON', 'Контракт'),
                                    ('AGR', 'Договор'),
                                ])
    number = models.CharField(verbose_name='Номер',
                              max_length=32)
    begin = models.DateField(verbose_name='Заключен')
    end = models.DateField(verbose_name='Истекает')

    class Meta:
        ordering = get_latest_by = ['end']
        verbose_name = 'Контракт/договор'
        verbose_name_plural = 'Контракты/договора'
        unique_together = ['category', 'number']
