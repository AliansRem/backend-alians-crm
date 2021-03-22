from rest_framework import viewsets, filters

from dosimetria.models import Client
from dosimetria.serializers import \
    ClientBriefSerializer, ClientDetailSerializer


class ClientAPI(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['name', 'taxpayer_id']
    ordering_fields = ['id', 'name']

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientBriefSerializer
        else:
            return ClientDetailSerializer
