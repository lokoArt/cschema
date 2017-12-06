from django.db import models
from insurance import vars


class Schema(models.Model):
    name = models.CharField(max_length=64)


class Field(models.Model):
    schema = models.ForeignKey(Schema, related_name='fields')
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=8, choices=vars.FIELD_TYPES)


class EnumOption(models.Model):
    field = models.ForeignKey(Field, related_name='options')
    value = models.CharField(max_length=128)

    class Meta:
        db_table = 'insurance_enum_option'