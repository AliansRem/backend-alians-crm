from rest_framework import serializers

from dosimetria.models import Quarter


class QuarterRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarter
        fields = ('id', 'year', 'number')


class QuarterBriefSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only=True,
                                     label='Итого')
    proceeds = serializers.IntegerField(read_only=True,
                                        label='Выручка')
    total_returned = serializers.IntegerField(read_only=True,
                                              label='Итого вернулось')
    total_not_returned = serializers.IntegerField(read_only=True,
                                                  label='Итого не вернулось')

    class Meta:
        model = Quarter
        exclude = ('begin', 'end')


class QuarterDetailSerializer(QuarterBriefSerializer):
    class Meta:
        model = Quarter
        fields = '__all__'
        exclude = None
