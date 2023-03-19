from django.urls import path
from API.views import get_init_waypoints, get_days, get_waypoints

urlpatterns = [
    path('get_init_waypoints/', get_init_waypoints.as_view()),
    path('get_waypoints/', get_waypoints.as_view()),
    path('get_days/', get_days.as_view())
]