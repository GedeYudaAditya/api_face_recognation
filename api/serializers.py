from rest_framework import serializers
from base.models import Test, Face, Image

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'