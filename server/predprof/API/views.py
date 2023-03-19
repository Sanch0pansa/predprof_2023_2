from django.shortcuts import render
from API.models import Day, Waypoint, Resources
from API.serializers import DaySerializer
from rest_framework import generics
from django.http import JsonResponse
import requests
from django.db import connection
from math import *

class get_init_waypoints(generics.GenericAPIView):

    def get(self, request):
        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE "API_waypoint" RESTART IDENTITY CASCADE')
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


class get_calcs(generics.GenericAPIView):


    def get(self, request):
        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE "API_day" RESTART IDENTITY CASCADE')
        waypoints = list(Waypoint.objects.all().values('SH', 'distance'))
        points = []
        for i in waypoints:
            points.append([i['distance'], i['SH']])
        days = 0
        credits = 0
        raspisanie = [{'SH_end': 8}]
        n = 0
        for s, c in points:
            n += 1
            for w in [80, 30, 5]:
                t = s * (200 + c) / (5 * w)
                if t >= log(1 + (c / 8), 2):
                    break
            t = ceil(t)
            days += t

            credits += 10 * w
            if 11 * w >= 465:
                oxi = 20
                temp = 30
                e = 465 / 11
            elif 11 * w >= 325:
                oxi = 30
                temp = 25
                e = 325 / 11
            else:
                oxi = 60
                temp = 10
                e = 55 / 11
            credits += 7 * oxi * t

            for i in range(t):
                sh = 8 + 8 * (i + 1)
                raspisanie.append({'fuel_consumption': w,
                                   'engine_consumption': w - e,
                                   'elecricity_consumption': e,
                                   'elecricity': 11 * e,
                                   'ship_mass': 192 + sh,
                                   'oxygen_consumption': oxi * sh,
                                   'SH_start': raspisanie[-1]['SH_end'],
                                   'SH_end': sh,
                                   'temperature': temp})
                Day.objects.create(fuel_consumption=w,
                                   engine_consumption=w - e,
                                   electricity_consumption=e,
                                   electricity=11 * e,
                                   ship_mass=192 + sh,
                                   oxygen_consumption=oxi * sh,
                                   SH_start=raspisanie[-1]['SH_end'],
                                   SH_end=sh,
                                   temperature=temp,
                                   waypoint_id=n)

        return JsonResponse(True, safe=False)

