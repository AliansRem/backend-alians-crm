from rest_framework import serializers

from dosimetria.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactViewSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()

    class Meta:
        model = Contact
        fields = '__all__'
