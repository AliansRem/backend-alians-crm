from rest_framework import serializers

from core.models import Client
from .contact import ContactSerializer


class ClientBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'taxpayer_id')


class ClientDetailSerializer(serializers.ModelSerializer):
    legal_contacts = ContactSerializer(many=True,
                                       read_only=False,
                                       required=False)

    class Meta:
        model = Client
        fields = '__all__'
