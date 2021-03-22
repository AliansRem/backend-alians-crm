from django.db import models


class Quarter(models.Model):
    year = models.PositiveSmallIntegerField(verbose_name='Год')
    number = models.PositiveSmallIntegerField(verbose_name='Номер')
    begin = models.DateField(verbose_name='Начало')
    end = models.DateField(verbose_name='Конец')

    def __str__(self):
        return f'{self.year}/{self.number}'

    class Meta:
        verbose_name = 'Квартал'
        verbose_name_plural = 'Кварталы'
        unique_together = ['year', 'number']
        ordering = get_latest_by = ['year', 'number']
