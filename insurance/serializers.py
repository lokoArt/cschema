from rest_framework import serializers

from insurance.models import Schema


class SchemaSerializer(serializers.ModelSerializer):
    schema = serializers.JSONField()

    class Meta:
        model = Schema
        fields = '__all__'
