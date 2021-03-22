from django.db import models
from core.models import Client as BaseClient


class Client(models.Model):
    organisation = models.OneToOneField(to=BaseClient,
                                        on_delete=models.CASCADE,
                                        related_name='organisation_info')

    def __str__(self):
        return self.organisation.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
