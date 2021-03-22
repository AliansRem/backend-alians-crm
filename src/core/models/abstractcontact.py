from django.db import models


class AbstractContact(models.Model):
    surname = models.CharField(null=True,
                               max_length=64,
                               verbose_name='Фамилия')
    firstname = models.CharField(max_length=64,
                                 verbose_name='Имя')
    patronymic = models.CharField(null=True,
                                  max_length=64,
                                  verbose_name='Отчество')

    email = models.EmailField(null=True,
                              verbose_name='Электронная почта')
    phone = models.CharField(null=True,
                             max_length=10,
                             verbose_name='Номер телефона')

    class Meta:
        abstract = True
