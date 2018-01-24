from rest_framework import serializers
from catalogManagement.models import Category, Catalog, RelatedParty
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

    def validate(self, data):
        try:
            if data['validFor_startDateTime'] > data['validFor_endDateTime']:
                raise serializers.ValidationError("endDate must occur after startDate")
        except:
            return data
        return data

    def create(self, validated_data):
        category, created = Category.objects.get_or_create(**validated_data)
        category.save()
        return category


class RelatedPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedParty
        fields = ('__all__')

    def create(self, validated_data):
        relatedParty, created = RelatedParty.objects.get_or_create(**validated_data)
        return relatedParty


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
        catalog = Catalog.objects.get_or_create(**validated_data)

        for category_data in categories_data:
            c, created = Category.objects.get_or_create(catalog=catalog, **category_data)
            print("se ha creado nuevo? {}".format(created))
        for relatedParty_data in relatedParties_data:
            r, rcreated = RelatedParty.objects.get_or_create(catalog=catalog, **relatedParty_data)
            print("se ha creado nuevo? {}".format(rcreated))

        return catalog

# class CatalogSerializer(serializers.ModelSerializer):
#     catalog = GenericModelSerializer({Category: CategorySerializer()}, many=True)
#     relatedParty = GenericModelSerializer({RelatedParty: RelatedPartySerializer()}, many=True)

#     class Meta:
#         model = Catalog
#         fields = ('__all__')
