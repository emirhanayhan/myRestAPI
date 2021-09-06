from rest_framework import serializers
from .models import users
from .models import users_trip

class userSerializer(serializers.Serializer):
    userId=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    mail=serializers.CharField()
    status=serializers.IntegerField()

    def create(self, validated_data):
        return users.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

class usertripSerializer(serializers.Serializer):
    tripId=serializers.IntegerField(read_only=True)
    totalDistance=serializers.IntegerField()
    beginningTime=serializers.CharField()
    userId_id=serializers.IntegerField()

    def create(self, validated_data):
        return users_trip.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.totalDistance = validated_data.get('totalDistance', instance.totalDistance)
        instance.beginningTime = validated_data.get('beginningTime', instance.beginningTime)
        instance.userId_id = validated_data.get('userId_id',instance.userId_id)
        instance.save()
        return instance