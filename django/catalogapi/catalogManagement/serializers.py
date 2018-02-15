from rest_framework import serializers
from catalogManagement.models import Category, Catalog, RelatedParty


def create_href(model):
    if model.href[len(model.href) - 1] == '/':
        model.href = model.href + str(model.id)
    else:
        model.href = model.href + '/' + str(model.id)

    model.save()
    return model


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('catalog',)

    def validate(self, data):
        try:
            if data['validFor_startDateTime'] > data['validFor_endDateTime']:
                raise serializers.ValidationError("endDate must occur after startDate")
        except:
            return data
        return data

    def create(self, validated_data):
        print(validated_data)
        try:
            if not validated_data.get('isRoot'):
                if 'parentId' in validated_data:
                    Category.objects.get(href=validated_data.get('parentId'))
                else:
                    raise serializers.ValidationError("parentId non present in non root category")
            else:
                if 'parentId' in validated_data:
                    raise serializers.ValidationError("parentId included in root category")
        except Category.DoesNotExist:
            raise serializers.ValidationError("parentId must be valid")
        category = Category.objects.create(**validated_data)
        return create_href(category)


class RelatedPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedParty
        exclude = ('catalog',)

    def create(self, validated_data):
        relatedParty, created = RelatedParty.objects.get_or_create(**validated_data)
        return create_href(relatedParty)


class CatalogSerializer(serializers.ModelSerializer):
    relatedParty = RelatedPartySerializer(many=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = Catalog
        fields = ("__all__")
        depth = 6

    def create(self, validated_data):
        # import ipdb; ipdb.sset_trace()
        relatedParties_data = validated_data.pop('relatedParty')
        # print("related parties: {}".format(relatedParties_data))
        categories_data = validated_data.pop('category')
        # print("categories: {}".format(categories_data))
        catalog, catalog_created = Catalog.objects.get_or_create(**validated_data)

        for category_data in categories_data:
            category_filtered = Category.objects.filter(href=dict(category_data).get('href'))
            if not category_filtered:
                raise serializers.ValidationError("There's no category with the href in request")
            else:
                category_filtered.update(catalog=catalog)
            # print("se ha creado nuevo? {}".format(created))
        for relatedParty_data in relatedParties_data:
            RelatedParty.objects.get_or_create(catalog=catalog, **relatedParty_data)
            # print("se ha creado nuevo? {}".format(rcreated))

        return create_href(catalog)

# class CatalogSerializer(serializers.ModelSerializer):
#     catalog = GenericModelSerializer({Category: CategorySerializer()}, many=True)
#     relatedParty = GenericModelSerializer({RelatedParty: RelatedPartySerializer()}, many=True)

#     class Meta:
#         model = Catalog
#         fields = ('__all__')
