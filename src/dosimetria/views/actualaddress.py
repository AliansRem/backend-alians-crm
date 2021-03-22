from rest_framework import viewsets

from dosimetria.models import ActualAddress
from dosimetria.serializers import \
    ActualAddressSerializer, ActualAddressViewSerializer


class ActualAddressAPI(viewsets.ModelViewSet):
    queryset = ActualAddress.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ActualAddressViewSerializer
        else:
            return ActualAddressSerializer
