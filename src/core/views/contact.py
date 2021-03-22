from rest_framework import viewsets

from core.models import Contact
from core.serializers import \
    ContactSerializer, ContactViewSerializer


class ContactAPI(viewsets.ModelViewSet):
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ContactViewSerializer
        else:
            return ContactSerializer
