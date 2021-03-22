from rest_framework.serializers import \
    StringRelatedField, ModelSerializer

from core.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactViewSerializer(ModelSerializer):
    organisation = StringRelatedField(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
