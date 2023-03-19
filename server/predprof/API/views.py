from django.shortcuts import render
from API.models import Day, Waypoint, Resources
from API.serializers import DaySerializer
from rest_framework import generics
from django.http import JsonResponse
import requests


class get_init_waypoints(generics.GenericAPIView):

    def get(self, request):
        Waypoint.objects.all().delete()
        headers = {'X-Auth-Token': '7vt3qmhc'}
        response = requests.get('https://dt.miet.ru/ppo_it_final', headers=headers)
        for i in response.json()['message'][0]['points']:
            Waypoint.objects.create(distance=i['distance'], SH=i['SH'])
        # for i in response.json()['message']:
        #     for j in i['points'][]:
        #         print(i['points'])
        #         Waypoint.objects.create(distance=j['distance'], SH=j['SH'])
        #     pass
        return JsonResponse(response.json(), safe=False)


class get_days(generics.ListAPIView):
    serializer_class = DaySerializer
    queryset = Day.objects.all()


class get_waypoints(generics.GenericAPIView):

    def get(self, request):
        waypoints = Waypoint.objects.all().values('SH', 'distance')
        return JsonResponse(list(waypoints), safe=False)


class get_consumptions(generics.GenericAPIView):


    def get(self, request):
        resources = list(Resources.objects.all().values())
        days = list(Day.objects.all().values())
        res = {
            'resources': resources,
            'days': days
        }
        return JsonResponse(res, safe=False)


class get_cals(generics.GenericAPIView):


    def get(self, request):
        pass
