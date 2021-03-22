from rest_framework import serializers

from dosimetria.models import Protocol

from .quarter import QuarterRelatedSerializer


class ProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocol
        fields = '__all__'


class ProtocolViewSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    quarter = QuarterRelatedSerializer()

    class Meta:
        model = Protocol
        fields = '__all__'
