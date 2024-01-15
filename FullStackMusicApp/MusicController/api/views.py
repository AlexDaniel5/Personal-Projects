from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all() # Return all of the room objects
    serializer_class = RoomSerializer # Use the serializer to convert the rooms into the correct format (maybe json)