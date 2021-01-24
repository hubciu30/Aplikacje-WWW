from rest_framework import serializers
from .models import Client, Video
from django.contrib.auth.models import User

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    samochody= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='samochod-detail')
    class Meta:
        model = Client
        fields=['id', 'url', 'mail', 'firstname', 'surname', 'birthday', 'videos']


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    wlasciciel = ClientSerializer()
    wlasciciel_uzytkownik = serializers.ReadOnlyField(source='wlasciciel_uzytkownik.username')
    class Meta:
        model = Video
        fields = ['id', 'url', 'title', 'year', 'director', 'type', 'owner']
