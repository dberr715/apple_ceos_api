from .models import AppleCeo
from rest_framework import serializers


class AppleCeoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppleCeo
        fields = ["name", "year_started"]
