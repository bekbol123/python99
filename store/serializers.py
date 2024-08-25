from rest_framework import serializers
from .models import *

class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'car_name', 'description', 'price', 'color', 'volume', )


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = '__all__'
