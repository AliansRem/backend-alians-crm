from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Наименование организации')
    taxpayer_id = models.CharField(max_length=12,
                                   verbose_name='ИНН')

    #  Юридический адрес
    postcode = models.PositiveSmallIntegerField(verbose_name='Почтовый индекс')

    region = models.CharField(max_length=64,
                              verbose_name='Регион/край')
    area = models.CharField(max_length=64,
                            verbose_name='Район')
    city = models.CharField(max_length=64,
                            verbose_name='Населенный пункт')

    street = models.CharField(max_length=64,
                              verbose_name='Улица')
    building = models.CharField(max_length=16,
                                verbose_name='Строение/дом')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['id']
