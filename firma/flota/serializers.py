from rest_framework import serializers
from .models import Osoba, Samochod
from django.contrib.auth.models import User

class OsobaSerializer(serializers.HyperlinkedModelSerializer):
    samochody= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='samochod-detail')
    class Meta:
        model = Osoba
        fields=['id', 'url', 'email', 'imie', 'nazwisko', 'data_urodzenia', 'zarobki', 'samochody']


class SamochodSerializer(serializers.HyperlinkedModelSerializer):
    wlasciciel = OsobaSerializer()
    wlasciciel_uzytkownik = serializers.ReadOnlyField(source='wlasciciel_uzytkownik.username')
    class Meta:
        model = Samochod
        fields = ['id', 'url', 'marka', 'model', 'pojemnosc', 'rok_produkcji', 'wlasciciel', 'wlasciciel_uzytkownik']


class UserSamochodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Samochod
        fields = ['url', 'marka', 'model']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    samochody = UserSamochodSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'samochody']