from rest_framework import serializers
from catalogManagement.models import Category, Catalog, RelatedParty


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

    def validate(self, data):
        try:
            if data['validFor_startDateTime'] > data['validFor_endDateTime']:
                raise serializers.ValidationError("endDate must occur after startDate")
        except KeyError:
            return data
        return data


class RelatedPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedParty
        fields = ('__all__')


class CatalogSerializer(serializers.ModelSerializer):
    relatedParty = RelatedPartySerializer(many=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = Catalog
        fields = ("__all__")
        depth = 6

    def create(self, validated_data):
        relatedParties_data = validated_data.pop('relatedParty')
        print("related parties: {}".format(relatedParties_data))
        categories_data = validated_data.pop('category')
        print("categories: {}".format(categories_data))
        catalog = Catalog.objects.create(**validated_data)

        for category_data in categories_data:
            Category.objects.create(catalog=catalog, **category_data)
        for relatedParty_data in relatedParties_data:
            RelatedParty.objects.create(catalog=catalog, **relatedParty_data)

        return catalog

# class CatalogSerializer(serializers.ModelSerializer):
#     catalog = GenericModelSerializer({Category: CategorySerializer()}, many=True)
#     relatedParty = GenericModelSerializer({RelatedParty: RelatedPartySerializer()}, many=True)

#     class Meta:
#         model = Catalog
#         fields = ('__all__')
