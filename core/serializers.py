from rest_framework import serializers

from core.models import Product, ApplicationCall


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ApplicationCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationCall
        fields = ('name', 'phone_number')