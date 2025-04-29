from django.shortcuts import render
from rest_framework import generics
from .models import Room

class RoomList(generics.ListAPIView):
    