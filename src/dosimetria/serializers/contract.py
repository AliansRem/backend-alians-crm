from rest_framework import serializers

from dosimetria.models import Contract


class ContractViewSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()

    class Meta:
        model = Contract
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
