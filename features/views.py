# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from features.serializers import ClientSerializer, ProjectSerializer, FeatureRequestSerializer
from features.models import Client, FeatureRequest, Project


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class FeatureRequestViewSet(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer
