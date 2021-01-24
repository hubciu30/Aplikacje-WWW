from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Client
from rest_framework import status

class ClientTest(APITestCase):
    def post_client(self, sn):
        url = reverse(views.ClientList.name)
        dane = {'surname': sn}
        response = self.client.post(url, dane, format='json')
        return response

    def test_post_adn_get_osoba(self):
        new_surname = 'Kowalski'
        response = self.post_client(new_surname)
        assert response.status_code == status.HTTP_201_CREATED
        assert Client.objects.count() == 1
        assert Client.objects.get().surname == new_surname