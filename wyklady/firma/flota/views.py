from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Osoba, Samochod
from .serializers import OsobaSerializer, SamochodSerializer, UserSerializer
from rest_framework import generics
from django_filters import DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User


class OsobaFilter(FilterSet):
    od_data_urodzenia = DateTimeFilter( field_name='data_urodzenia', lookup_expr='gte')
    do_data_urodzenia = DateTimeFilter( field_name='data_urodzenia', lookup_expr='lte')
    od_zarobki = NumberFilter( field_name='zarobki', lookup_expr='gte')
    do_zarobki = NumberFilter( field_name='zarobki', lookup_expr='lte')


class OsobaList(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    filter_class = OsobaFilter
    name = 'osoba-list'
    search_fields=['imie', 'nazwisko']
    ordering_fields = ['zarobki', 'nazwisko', 'data_urodzenia']
    filter_fields = ['zarobki']


class OsobaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    name = 'osoba-detail'


class SamochodList(generics.ListCreateAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-list'
    search_fields=['marka', 'model']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(wlasciciel_uzytkownik=self.request.user)

class SamochodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'osoby': reverse(OsobaList.name, request=request),
                         'samochody': reverse(SamochodList.name, request=request),
                         'uzytkownicy': reverse(UserList.name, request=request),
                         })









