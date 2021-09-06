from rest_framework.test import APITestCase
from .models import users
from .models import users_trip
import json
from django.urls import reverse
from rest_framework import status

class testUser(APITestCase):

    url = '/api/user/'

    def setUp(self):
        users.objects.create(name='ali', mail='ali@gmail.com', status=1)
        users.objects.create(userId=35,name='veli', mail='veli@gmail.com', status=1)

    def test_get_userlist(self):
        response= self.client.get(self.url)
        result = response.json()
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]['name'], 'ali')
        self.assertEqual(result[0]['mail'], 'ali@gmail.com')
        self.assertEqual(result[0]['status'], 1)

    def test_get_userbyid(self):
        response = self.client.get(reverse('user-detail',kwargs={'pk':35}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'],'veli')

    def test_post_user(self):
        data = {
            'name':'yeniali',
            'mail':'yeniali@gmail.com',
            'status':0
        }
        response=self.client.post(self.url,data=data)
        result=response.json()
        self.assertEqual(response.status_code,201)
        self.assertEqual(result['name'], 'yeniali')
        self.assertEqual(result['mail'], 'yeniali@gmail.com')
        self.assertEqual(result['status'], 0)

    def test_update_user(self):
        pk=35
        data2={
            'name':'ali2',
            'mail':'ali2@gmail.com',
            'status':0
        }
        response = self.client.put(reverse('user-detail', kwargs={'pk': pk}),
            data = json.dumps(data2),
            content_type='application/json'
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        pk=1
        response=self.client.delete(reverse('user-detail', kwargs={'pk': pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class testUserTrip(APITestCase):
    url = '/api/trip/'

    def setUp(self):
        users.objects.create(userId=1,name='ali', mail='ali@gmail.com', status=1)
        users.objects.create(userId=4, name='ali3', mail='ali3@gmail.com', status=1)
        users.objects.create(userId=33, name='ali2', mail='ali2@gmail.com', status=1)
        users_trip.objects.create(userId_id=1, totalDistance=35, beginningTime='03:53pm')
        users_trip.objects.create(userId_id=1, totalDistance=45, beginningTime='04:53pm')
    def test_get_triplist(self):
        response= self.client.get(self.url)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['totalDistance'], 35)
        self.assertEqual(result[0]['beginningTime'], '03:53pm')

    def test_post_trip(self):
        data = {
            'userId_id': 33,
            'totalDistance': 55,
            'beginningTime': '07:53pm'
        }
        response = self.client.post(self.url, data=data)
        result = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['totalDistance'], 55)
        self.assertEqual(result['beginningTime'], '07:53pm')

    def test_update_trip(self):
        pk = 1
        data2 = {
            'userId_id': 33,
            'totalDistance': 65,
            'beginningTime': '05:25am'
        }
        response = self.client.put(reverse('trip-detail', kwargs={'pk': pk}),
                                   data=json.dumps(data2),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_trip(self):
        pk = 1
        response = self.client.delete(reverse('trip-detail', kwargs={'pk': pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_tripbyuserid(self):
        response = self.client.get(reverse('trip-detailwithuserid', kwargs={'userid': '1'}))
        result=response.json()
        print(response.data)
        self.assertEqual(result[0]['totalDistance'], 35)
        self.assertEqual(result[0]['beginningTime'], '03:53pm')
        self.assertEqual(result[1]['totalDistance'], 45)
        self.assertEqual(result[1]['beginningTime'], '04:53pm')



























