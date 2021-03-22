from rest_framework.viewsets import ModelViewSet

from dosimetria.models import TransmittedDocument
from dosimetria.serializers import \
    TransmittedDocumentSerializer, TransmittedDocumentViewSerializer


class TransmittedDocumentAPI(ModelViewSet):
    queryset = TransmittedDocument.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TransmittedDocumentViewSerializer
        else:
            return TransmittedDocumentSerializer
