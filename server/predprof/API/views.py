from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
import requests


class getData(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        headers = {'X-Auth-Token': '7vt3qmhc'}
        response = requests.get('https://dt.miet.ru/ppo_it_final', headers=headers)
        return JsonResponse(response.json(), safe=False)

