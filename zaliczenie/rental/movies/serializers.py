from rest_framework import serializers
from .models import Client, Video
from django.contrib.auth.models import User

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    videos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='video-detail')
    #videos = Video
    class Meta:
        model = Client
        fields=['id', 'url', 'mail', 'firstname', 'surname', 'birthday', 'videos']


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    owner = Client
    class Meta:
        model = Video
        fields = ['id', 'url', 'title', 'year', 'director', 'type', 'owner']
