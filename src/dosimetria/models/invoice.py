from django.db import models
from .client import Client
from .quarter import Quarter


class Invoice(models.Model):
    client = models.ForeignKey(verbose_name='Клиент',
                               to=Client,
                               on_delete=models.PROTECT,
                               related_name='invoices')

    issued_at = models.ForeignKey(verbose_name='Квартал',
                                  to=Quarter,
                                  on_delete=models.CASCADE,
                                  related_name='issued_invoices')

    number = models.CharField(verbose_name='Номер',
                              max_length=16,
                              unique=True)

    is_returned = models.BooleanField(default=False,
                                      verbose_name='Статус')

    returned_at = models.ForeignKey(null=True,
                                    verbose_name='Квартал возврата',
                                    to=Quarter,
                                    on_delete=models.CASCADE,
                                    related_name='returned_invoices')

    total = models.PositiveIntegerField(verbose_name='Сумма')

    class Meta:
        verbose_name = 'Счет/акт'
        verbose_name_plural = 'Счета/акты'
