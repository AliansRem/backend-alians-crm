from rest_framework import serializers

from dosimetria.models import ActualAddress


class ActualAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActualAddress
        fields = '__all__'


class ActualAddressViewSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()

    class Meta:
        model = ActualAddress
        fields = '__all__'
