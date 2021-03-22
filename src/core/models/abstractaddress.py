from django.db import models


class AbstractAddress(models.Model):
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

    class Meta:
        abstract = True
