from rest_framework.viewsets import ModelViewSet

from dosimetria.models import Protocol
from dosimetria.serializers import \
    ProtocolSerializer, ProtocolViewSerializer


class ProtocolAPI(ModelViewSet):
    queryset = Protocol.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProtocolViewSerializer
        else:
            return ProtocolSerializer
