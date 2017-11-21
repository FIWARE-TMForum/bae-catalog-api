from rest_framework import serializers
from catalogManagement.models import Category, ValidFor

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    href = serializers.CharField()
    version = serializers.CharField()
    lastUpdate = serializers.DateTimeField()
    lifecycleStatus = serializers.CharField()
    validFor = serializers.ForeignKey(ValidFor)
    parentId = serializers.CharField()
    isRoot = serializers.CharField()
    name = serializers.TextField()
    description = serializers.TextField()
    
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.href = validated_data.get('href', instance.href)
        instance.version = validated_data.get('version', instance.version)
        instance.lastUpdate = validated_data.get('lastUpdate', instance.lastUpdate)
        instance.lifecycleStatus = validated_data.get('lifecycleStatus', instance.lifecycleStatus)
        instance.validFor = validated_data.get('validFor', instance. validFor)
        instance.parentId = validated_data.get('parentId', instance.parentId)
        instance.isRoot = validated_data.get('isRoot', instance.isRoot)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        
        return instance



        
