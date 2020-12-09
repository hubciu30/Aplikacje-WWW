from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Osoba, Samochod
from .serializers import OsobaSerializer, SamochodSerializer
from rest_framework import generics
from django_filters import DateTimeFilter, NumberFilter, FilterSet


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

class SamochodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
    name = 'samochod-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'osoby': reverse(OsobaList.name, request=request),
                         'samochody':reverse(SamochodList.name, request=request),
                         })









