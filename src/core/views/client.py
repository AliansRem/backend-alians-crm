from rest_framework import viewsets
from rest_framework import filters

from core.models import Client
from core.serializers import ClientBriefSerializer, ClientDetailSerializer


class ClientAPI(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    search_fields = ['name', 'taxpayer_id']
    ordering_fields = ['id', 'name']
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientBriefSerializer
        else:
            return ClientDetailSerializer
