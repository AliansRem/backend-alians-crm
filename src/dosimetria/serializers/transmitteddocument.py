from rest_framework import serializers

from dosimetria.models import TransmittedDocument

from .quarter import QuarterRelatedSerializer


class TransmittedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmittedDocument
        fields = '__all__'


class TransmittedDocumentViewSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    quarter = QuarterRelatedSerializer()

    class Meta:
        model = TransmittedDocument
        fields = '__all__'
