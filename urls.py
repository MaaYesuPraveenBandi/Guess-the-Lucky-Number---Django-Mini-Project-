from django.contrib import admin
from django.urls import path
from home.views import miniProject


urlpatterns = [path('miniProject/', miniProject , name = "miniProject")]
