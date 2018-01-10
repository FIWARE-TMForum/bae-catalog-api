from rest_framework import serializers
from catalogManagement.models import Category, Catalog, RelatedParty


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

    def validate(self, data):
        if data['validFor_startDateTime'] > data['validFor_endDateTime']:
            raise serializers.ValidationError("endDate must occur after startDate")
        return data


class RelatedPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedParty
        fields = ('__all__')


class CatalogSerializer(serializers.ModelSerializer):
    relatedParty = RelatedPartySerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = ('__all__')
