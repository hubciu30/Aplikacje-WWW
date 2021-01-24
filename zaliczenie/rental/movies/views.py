from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Client, Video
from .serializers import ClientSerializer, VideoSerializer
from rest_framework import generics
from django_filters import DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User


class ClientFilter(FilterSet):
    from_birthday = DateTimeFilter( field_name='birthday', lookup_expr='gte')
    to_birthday = DateTimeFilter( field_name='birthday', lookup_expr='lte')

class ViedoFilter(FilterSet):
    from_year = NumberFilter(field_name='year', lookup_expr='gte')
    to_year = NumberFilter(field_name='year', lookup_expr='lte')

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_class = ClientFilter
    name = 'client-list'
    search_fields=['firstname', 'surname']
    ordering_fields = ['surname', 'birthday']

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    ordering_fields = ['title', 'year', 'director', 'type']
    name = 'video-list'
    filter_class = ViedoFilter
    search_fields=['title', 'type', 'year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    name = 'video-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'clients': reverse(ClientList.name, request=request),
                         'videos': reverse(VideoList.name, request=request),
                         })