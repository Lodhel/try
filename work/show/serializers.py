from rest_framework import serializers
from . import models


class Test(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = ('id', 'test')

        extra_kwargs = {
            'test': {'write_only': True}
        }

    def create(self, validated_data):

        request = models.Test(
            test=validated_data['test']
        )

        return request

class AutoServicesSer(serializers.ModelSerializer):
    class Meta:
        model = models.AutoServices
        fields = ('id', 'SERVICES_CHOICES', 'services')

    def create(self, validated_data, **kwargs):

        request = models.AutoServices(kwargs)

        return request
    """
    остальная серилизация
    """