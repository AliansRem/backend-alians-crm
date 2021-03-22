from django.db.models import Sum, Q

from rest_framework import viewsets

from dosimetria.models import Quarter
from dosimetria.serializers import \
    QuarterBriefSerializer, QuarterDetailSerializer


class QuarterAPI(viewsets.ModelViewSet):
    queryset = Quarter.objects.annotate(
        total=Sum('issued_invoices__total'),

        proceeds=Sum('returned_invoices__total',
                     filter=Q(returned_invoices__is_returned=True)),

        total_returned=Sum('issued_invoices__total',
                           filter=Q(issued_invoices__is_returned=True)),

        total_not_returned=Sum('issued_invoices__total',
                               filter=Q(issued_invoices__is_returned=False))
    )

    def get_serializer_class(self):
        if self.action == 'list':
            return QuarterBriefSerializer
        else:
            return QuarterDetailSerializer
