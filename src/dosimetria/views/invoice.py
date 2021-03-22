from rest_framework.viewsets import ModelViewSet

from dosimetria.models import Invoice
from dosimetria.serializers import \
    InvoiceSerializer, InvoiceViewSerializer


class InvoiceAPI(ModelViewSet):
    queryset = Invoice.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return InvoiceViewSerializer
        else:
            return InvoiceSerializer
