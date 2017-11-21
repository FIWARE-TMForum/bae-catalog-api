from rest_framework import serializers
from catalogManagement.models import Category, ValidFor

class ValidForSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidFor
        fields = ('startDateTime', 'endDateTime')

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'href', 'version', 'lastUpdate', 'lifecycleStatus', 'validFor',
                  'parentId', 'isRoot', 'name', 'description')

            

    id = serializers.IntegerField(read_only=True)
    href = serializers.CharField()
    version = serializers.CharField()
    lastUpdate = serializers.DateTimeField(required=False)
    lifecycleStatus = serializers.CharField()
    validFor = ValidForSerializer(required=False)
    parentId = serializers.CharField(required=False)
    isRoot = serializers.BooleanField()
    name = serializers.CharField()
    description = serializers.CharField()
    
    def create(self, validated_data):
        try:
            v = validated_data.pop('validFor')
        #validfor = ValidFor(v['startDateTime'], v['endDateTime'])

            validfor = ValidFor.create(v['startDateTime'], v['endDateTime'])
            validfor.save()
        
            return Category.objects.create(validFor=validfor, **validated_data)
        except:
            return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.href = validated_data.get('href', instance.href)
        instance.version = validated_data.get('version', instance.version)
        instance.lastUpdate = validated_data.get('lastUpdate', instance.lastUpdate)
        instance.lifecycleStatus = validated_data.get('lifecycleStatus', instance.lifecycleStatus)
        instance.validFor = validated_data.get('validFor', instance.validFor)
        instance.parentId = validated_data.get('parentId', instance.parentId)
        instance.isRoot = validated_data.get('isRoot', instance.isRoot)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        
        return instance
