from django.db import models
from .client import Client
from .quarter import Quarter


class TransmittedDocument(models.Model):
    client = models.ForeignKey(verbose_name='Клиент',
                               to=Client,
                               on_delete=models.PROTECT,
                               related_name='transmitted_documents')

    quarter = models.ForeignKey(verbose_name='Квартал',
                                to=Quarter,
                                on_delete=models.CASCADE)

    name = models.CharField(verbose_name='Наименование',
                            max_length=128)

    is_returned = models.BooleanField(verbose_name='Статус')

    class Meta:
        verbose_name = 'Переданный документ'
        verbose_name_plural = 'Переданные документы'
