from rest_framework import serializers

from core.models import Product, ApplicationCall, Sizes


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    sizes = SizesSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'


class ApplicationCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationCall
        fields = ('name', 'phone_number')