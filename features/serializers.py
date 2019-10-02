from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from features.models import Client, Project, FeatureRequest


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'contact', 'street', 'city', 'state', 'zip', 'phone']


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class FeatureRequestSerializer(ModelSerializer):
    client = PrimaryKeyRelatedField(queryset=Client.objects.all())
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = FeatureRequest
        fields = ['id',
                  'title',
                  'description',
                  'create_date',
                  'target_date',
                  'priority',
                  'client',
                  'project']
