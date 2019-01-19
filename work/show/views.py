from django.shortcuts import render

from rest_framework import viewsets, filters

from . import models, serializers

class TestView(viewsets.ModelViewSet):
    serializer_class = serializers.Test
    queryset = models.Test.objects.all()
    filter_backends = (filters.SearchFilter,)
