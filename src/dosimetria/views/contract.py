from rest_framework import viewsets

from dosimetria.models import Contract
from dosimetria.serializers import \
    ContractSerializer, ContractViewSerializer


class ContractAPI(viewsets.ModelViewSet):
    queryset = Contract.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ContractViewSerializer
        else:
            return ContractSerializer
