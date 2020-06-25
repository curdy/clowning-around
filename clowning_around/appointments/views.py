
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, permissions
from clowning_around.appointments.models import Appointment
from clowning_around.appointments.serializers import AppointmentSerializer, RequestContactSerializer, AppointmentIssueSerializer
from rest_framework.decorators import api_view
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics
from django.contrib.auth import get_user_model


User = get_user_model()

class AppointmentList(generics.ListCreateAPIView, generics.DestroyAPIView):  # handles GETs

    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #queryset = Appointment.objects.all()
    
    def get_queryset(self):
        
        print(self.request.user)
        
        appointments = Appointment.objects.all()
        
        return appointments
    
    def perform_create(self, serializer):
        if self.request.user.is_troupe_leader:
            serializer.save(owner=self.request.user)


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):  # handles GETs

    serializer_class = AppointmentSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Appointment.objects.all()
    
class LogIssueTicket(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = AppointmentIssueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        
        if self.request.user.is_clown == True:
            return Appointment.objects.all()
        
        return HttpResponse("Clowns only")
    
    
class RequestContact(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = RequestContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    def get_queryset(self):
        return Appointment.objects.all()
