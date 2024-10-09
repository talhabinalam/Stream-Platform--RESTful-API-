from .models import *

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = StreamPlatform.objects.create(name="Netflix", about="Streaming Platform",
                                                        website="https://www.netflix.com",)

    def test_create_stream_platform(self):
        data = {
            "name": "Netflix",
            "about": "Streaming Platform",
            "website": "https://www.netflix.com"
        }
        response = self.client.post(reverse('stream-platform'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_stream_platform_list(self):
        response = self.client.get(reverse('stream-platform'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stream_platform_detail(self):
        response = self.client.get(reverse('stream-details', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchlistTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='example', password='password@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = StreamPlatform.objects.create(name="Netflix", about="Streaming Platform",
                                                        website="https://www.netflix.com")
        self.watchlist = WatchList.objects.create(platform=self.stream, title="Spider Man",
                                                  description="Movie", active=True)

    def test_create_watchlist(self):
        data = {
            "title": "Spider man",
            "description": "Movie",
            "platform": self.stream.id,
            "active": True
        }

        response = self.client.post(reverse('watchlist'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('watchlist'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_detail(self):
        response = self.client.get(reverse('watchlist-details', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
