from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Client, Video
from rest_framework import status
from django.utils.http import urlencode

class ClientTest(APITestCase):
    def post_client(self, sn):
        url = reverse(views.ClientList.name)
        dane = {'surname': sn}
        response = self.client.post(url, dane, format='json')
        return response

    def post_video(self, name):
        url = reverse(views.VideoList.name)
        dane = {'title': name}
        response = self.client.post(url, dane, format='json')
        return response

    # dodajemy clienta
    def test_post_and_get_client(self):
        new_surname = 'Kowalski'
        response = self.post_client(new_surname)
        assert response.status_code == status.HTTP_201_CREATED
        assert Client.objects.count() == 1
        assert Client.objects.get().surname == new_surname

    # proba dodania filmu, którego nie możemy dodać bo nie jesteśmy zalogowani
    def test_post_and_get_video(self):
        new_title = "Straszny film!"
        response = self.post_video(new_title)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Video.objects.count() == 0

    # sprawdzam czy mogę pobrać viedo
    def test_get_video(self):
        url = reverse(views.VideoList.name)
        get_response = self.client.get(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK

    # Sprawdzam czy działa wyszukiwanie
    def test_post_search_client(self):
        def AddClient(name, surname):
            url = reverse(views.ClientList.name)
            dane = {'name': name, 'surname': surname}
            response = self.client.post(url, dane, format='json')
            assert response.status_code == status.HTTP_201_CREATED

        AddClient("Adam", "Nowak")
        AddClient("Ewa", "Nowak")
        AddClient("Katarzyna", "Kowalska")

        url = '{0}?{1}'.format(reverse(views.ClientList.name), urlencode({'search': "Kowalska"}))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    # Sprawdzam usuwanie clienta
    def test_post_delete_client(self):
        def AddClient(name, surname):
            url = reverse(views.ClientList.name)
            dane = {'name': name, 'surname': surname}
            response = self.client.post(url, dane, format='json')
            assert response.status_code == status.HTTP_201_CREATED

        AddClient("Adam", "Nowak")
        AddClient("Ewa", "Nowak")
        AddClient("Katarzyna", "Kowalska")
        url = reverse(views.ClientList.name) + "/3"
        response = self.client.delete(url, format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        url = reverse(views.ClientList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2