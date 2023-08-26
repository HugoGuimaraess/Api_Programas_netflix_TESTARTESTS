from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class ValidaUsuarioAPITestCase(APITestCase):

    def setUp(self):
        self.list_url=reverse('programas-list')
        self.user=User.objects.create_user(username='EDINALDO',password='123456')


    def validalogin(self):
        user = authenticate(username='EDINALDO',password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)



    def test_req_get_naoauto(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_credenciais_erradas(self):
        user = authenticate(username='EDIN',password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_get_autenticauser(self):
        self.client.force_authenticate(self.user)
        response=self.client.get(self.list_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)