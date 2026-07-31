from rest_framework import serializers
from .models import Person
# serializer class is used here
""" class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length = 150) 


    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.city = validated_data.get("city", instance.city)
        instance.save()
        return instance """

# ModelSerializer is used here -> in this create()and update() will run automatically 

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"