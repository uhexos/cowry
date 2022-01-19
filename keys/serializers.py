from django.contrib.auth.models import User, Group
from rest_framework import serializers

from keys.models import KeyValuePair


class KeyValuePairSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyValuePair;
        fields = ['key', 'value']

    def to_representation(self, instance):
        return {instance.key.strftime("%Y-%m-%d %H:%M:%S.%f") : instance.value}