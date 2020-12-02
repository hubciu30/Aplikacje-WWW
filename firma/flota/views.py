from .models import Osoba
from .serializers import OsobaSerializer
from rest_framework import generics

class OsobaList(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer


class OsobaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer









