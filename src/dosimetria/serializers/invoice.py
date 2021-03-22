from rest_framework import serializers

from dosimetria.models import Invoice

from .quarter import QuarterRelatedSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceViewSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    quarter = QuarterRelatedSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'
