from rest_framework import serializers

from core.serializers import \
    ClientBriefSerializer as OrganisationBriefSerializer
from core.serializers import \
    ClientDetailSerializer as OrganisationDetailSerializer

from dosimetria.models import Client

from .contract import ContractSerializer
from .contact import ContactSerializer
from .actualaddress import ActualAddressSerializer
from .invoice import InvoiceSerializer
from .protocol import ProtocolSerializer
from .transmitteddocument import TransmittedDocumentSerializer


class ClientBriefSerializer(serializers.ModelSerializer):
    organisation = OrganisationBriefSerializer(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailSerializer(serializers.ModelSerializer):
    organisation = \
        OrganisationDetailSerializer(read_only=True)

    contacts = \
        ContactSerializer(many=True, read_only=True)
    actual_addresses = \
        ActualAddressSerializer(many=True, read_only=True)

    contracts = \
        ContractSerializer(many=True, read_only=True)

    invoices = \
        InvoiceSerializer(many=True, read_only=True)
    protocols = \
        ProtocolSerializer(many=True, read_only=True)
    transmitted_documents = \
        TransmittedDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
