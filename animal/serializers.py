from rest_framework import serializers


from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = '__all__'

    def create(self, validated_data):
        animal = Animal.objects.create(**validated_data)
        return animal

