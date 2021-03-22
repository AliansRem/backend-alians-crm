from django.db import models

from .client import Client
from .abstractcontact import AbstractContact


class Contact(AbstractContact):
    organisation = models.ForeignKey(Client,
                                     models.CASCADE,
                                     related_name='legal_contacts')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
