from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from keys.models import KeyValuePair
from keys.serializers import KeyValuePairSerializer
# Create your views here.

class KeyValuePairViewSet(viewsets.ModelViewSet):
    queryset = KeyValuePair.objects.all().order_by('-key')
    serializer_class = KeyValuePairSerializer
    permission_classes = [permissions.IsAuthenticated]