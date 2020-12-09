from rest_framework import serializers
from .models import Osoba, Samochod


class OsobaSerializer(serializers.HyperlinkedModelSerializer):
    samochody= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='samochod-detail')
    class Meta:
        model = Osoba
        fields=['id', 'url', 'email', 'imie', 'nazwisko', 'data_urodzenia', 'zarobki', 'samochody']


class SamochodSerializer(serializers.HyperlinkedModelSerializer):
    wlasciciel= OsobaSerializer()
    class Meta:
        model = Samochod
        fields = ['id', 'url', 'marka', 'model', 'pojemnosc', 'rok_produkcji', 'wlasciciel']

