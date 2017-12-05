from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from insurance import serializers
from insurance.models import Schema


class ReadSchemaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.SchemaSerializer
    queryset = Schema.objects.all()