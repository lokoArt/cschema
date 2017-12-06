from collections import OrderedDict
from rest_framework import serializers

from insurance.models import Schema, Field, EnumOption
from insurance import vars


class FieldSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Field
        fields = ('name',
                  'type',
                  'options')

    def get_options(self, object):
        if object.type != vars.FIELD_TYPE_ENUM:
            return None

        return EnumOption.objects.filter(field=object).values_list('value', flat=True)

    def to_representation(self, instance):
        ret = super(FieldSerializer, self).to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret


class SchemaSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Schema
        fields = ('id',
                  'name',
                  'fields')
