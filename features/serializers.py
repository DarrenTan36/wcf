from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField
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
    client = HyperlinkedRelatedField(queryset=Client.objects.all(), view_name='client-detail')
    project = HyperlinkedRelatedField(queryset=Project.objects.all(), view_name='project-detail')

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
